# Make a small plan you can check

**A specification, or spec, says what the app should do and how you will know it works.** Start from your existing SPEC and reviewed LEARNING. Update the same project record rather than writing another report.

## Plan one useful task

1. **Name the user and need.** What are they trying to do? Which facts support it, and what are you assuming?
2. **Compare two feasible approaches.** Change one useful workflow or presentation decision. Share code and data where sensible.
3. **Choose a small scope.** List what is included and deferred. Use the posted Studio brief as a boundary.
4. **Write three to five stories and checks.** “As a [user], I want [action], so [benefit].” Give each an observable expected result and a relevant failure case.
5. **Get a second reading.** Can a classmate explain what passes? Resolve unclear wording before asking AI to build.

**Teaching example — review a content draft**

> As a member, I want to save a plain-text draft so an authorized reviewer can decide whether to publish it.
>
> **Checks:** a permitted member saves a draft; an unprivileged request cannot publish it; an authorized reviewer can publish the valid draft. Check the server response and stored result.

Compare inline review controls with a separate review screen. Share content and data. A static role selector only demonstrates the interface; it does not pass server-permission checks.

## Turn the plan into work

For a group, name an owner and a different reviewer for each meaningful slice. Everyone contributes design, development and QA. Agree how the parts connect; integrate early.

Link the story in an issue, make a bounded branch/change, run its checks, then use a PR and the required review/CI steps before merging. Record actual results and limits in the same spec. A useful spec changes when you learn; it is not a large document written once and ignored.

[Copy the existing record](/templates/project-record) · [Review together](/process/collaboration) · [Check the work](/process/quality) · [Posted versus planned scope](/projects/studios).
