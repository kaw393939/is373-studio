# Check what you actually built

**A test needs an expected result you can explain.** Check the main task, a likely mistake and the result shown to the user. Record the revision, expected/actual result, command or task, and any fix/retest in your existing spec.

## Start with meaningful checks

| Check | What to establish |
| --- | --- |
| Roles and state | Check allowed and rejected server requests, the stored result, and draft/review/publish transitions. A hidden button alone is not authorization. |
| Content/ETL | Use small fixtures to check invalid input, deduplication, source trace and repeat-import behavior where specified. |
| Evidence layers | Label local, CI and actual hosted results separately; a green CI run is not a deployed-service check. |
| Existing services | Use the agreed delivery plan and preserve working services; do not start fresh-server setup over an existing deployment. |
| Interface | Try a narrow screen, keyboard controls, visible focus, labeled fields and clear errors. Check important links and setup steps. |
| Peer task | Let a real classmate try without coaching. Record the obstacle, choose a meaningful change and retest. |

**App Studio stays local.** Its original assessment does not require deployment. Use the documented fast-local/full-CI alternative for Server Studio when local Docker is unavailable, labeling unrun checks honestly. [Exact posted Studio scopes](/projects/studios).

## Keep evidence honest

- **Executed:** identify the command/task, revision and actual result.
- **Pending or failed:** say so and name the next action.
- **Limited:** explain what the check does not prove. A pure-function test does not prove a real browser task or deployed service works.

A passing build is not a usability check. A screenshot of a role or success message is not proof of server enforcement or persistence. Use synthetic data, and remove secrets/private information from public evidence.

For the group, each member checks someone else's work. Automated checks cover important behavior; a real walkthrough checks understanding and use. Keep the [issue → response → change → retest](/process/github-feedback) evidence linked from the same [project record](/templates/project-record).

[Review routine](/process/collaboration) · [Current Studio requirements](/projects/studios).
