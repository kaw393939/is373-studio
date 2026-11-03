"""Keep the downloadable teaching source identical to the checked source."""
from pathlib import Path
from zipfile import ZipFile

root = Path(__file__).resolve().parents[1] / 'docs/public/examples/content-desk'
excluded = {'.venv', '.git', '__pycache__', '.pytest_cache', 'instance', 'runtime'}
source = {
    'content-desk/' + p.relative_to(root).as_posix(): p.read_bytes()
    for p in root.rglob('*')
    if p.is_file() and not excluded.intersection(p.relative_to(root).parts)
    and p.suffix not in {'.zip', '.pyc', '.sqlite', '.db'}
}
with ZipFile(root / 'content-desk-source.zip') as archive:
    packaged = {n: archive.read(n) for n in archive.namelist() if not n.endswith('/')}
assert source == packaged, 'Source download is stale or includes unexpected files; regenerate the ZIP.'
print(f'Checked {len(source)} source files against the downloadable archive.')
