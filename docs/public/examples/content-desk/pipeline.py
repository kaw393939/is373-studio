"""Bounded ETL: supplied synthetic documents only; no network or model calls."""
import hashlib
import json
from pathlib import Path
import re
import unicodedata
from store import connect

PERMISSION = 'classroom-synthetic'
CATEGORIES = {'Events', 'Learning', 'Opportunities'}


def clean(value):
    if not isinstance(value, str):
        raise ValueError('Fields must contain text.')
    return ' '.join(unicodedata.normalize('NFKC', value).split())


def normalize(document):
    if not isinstance(document, dict):
        raise ValueError('A document must be an object.')
    key = clean(document.get('source_id'))
    title, body = clean(document.get('title')), clean(document.get('body'))
    category = clean(document.get('category'))
    if not re.fullmatch(r'[a-z0-9-]{3,60}', key):
        raise ValueError('Invalid source ID.')
    if not 3 <= len(title) <= 100 or not 20 <= len(body) <= 4000:
        raise ValueError('Use a title of 3–100 and body of 20–4,000 characters.')
    if category not in CATEGORIES or document.get('permission') != PERMISSION:
        raise ValueError('Use a supported category and permitted synthetic source.')
    digest = hashlib.sha256((title.casefold() + '\n' + body.casefold()).encode()).hexdigest()
    return dict(source_key=key, title=title, body=body, category=category,
                permission=PERMISSION, fingerprint=digest)


def extract_fixtures():
    return [json.loads(p.read_text()) for p in sorted((Path(__file__).parent / 'fixtures').glob('*.json'))]


def import_documents(path, owner_id, documents):
    """Reject bad rows; load all accepted rows and provenance atomically.

    Duplicate content shares one draft, while every distinct permitted source is retained.
    A reused source ID with changed content is rejected rather than silently overwritten.
    """
    if not isinstance(documents, list) or not 1 <= len(documents) <= 20:
        raise ValueError('Import 1–20 documents at a time.')
    report = dict(added=0, linked=0, skipped=0, rejected=[])
    prepared = []
    for index, document in enumerate(documents, 1):
        try:
            prepared.append(normalize(document))
        except ValueError as error:
            report['rejected'].append(f'Document {index}: {error}')
    with connect(path) as db:
        # The same write transaction covers draft + source, including duplicate checks.
        db.execute('BEGIN IMMEDIATE')
        for row in prepared:
            previous = db.execute('SELECT fingerprint FROM sources WHERE source_key=?', (row['source_key'],)).fetchone()
            if previous:
                if previous['fingerprint'] == row['fingerprint']:
                    report['skipped'] += 1
                else:
                    report['rejected'].append(f"{row['source_key']}: source changed; review it manually.")
                continue
            article = db.execute('SELECT id FROM articles WHERE fingerprint=?', (row['fingerprint'],)).fetchone()
            if article:
                article_id = article['id']
                report['linked'] += 1
            else:
                cursor = db.execute('INSERT INTO articles(owner_id,title,body,category,fingerprint) VALUES(?,?,?,?,?)',
                                    (owner_id,row['title'],row['body'],row['category'],row['fingerprint']))
                article_id = cursor.lastrowid
                report['added'] += 1
            db.execute('INSERT INTO sources(source_key,source_title,permission,fingerprint,article_id) VALUES(?,?,?,?,?)',
                       (row['source_key'],row['title'],row['permission'],row['fingerprint'],article_id))
    return report
