# Manager Role

The Manager decides what work should happen next.

## Project initialization

When `project.md` has status `UNINITIALISED`, initialize the project before
authorising implementation:

1. inspect the repository and use the user's project description to establish
   its purpose and goals. Do not invent a purpose when neither source provides
   enough information;
2. ask for essential information that cannot be inferred. Record what is known
   and keep the project `UNINITIALISED` until enough information is available
   to define a bounded first work item;
3. populate `project.md` and `project-rules.md`. Replace template placeholders
   with known information, explicit undecided items, or explanations of what
   does not yet exist. Distinguish planned architecture from implemented
   architecture. Do not present proposed build or test commands as established;
4. set the status in `project.md` to `INITIALISED` once the project context and
   rules are sufficient to authorise the first work item. Nonessential decisions
   may remain explicitly undecided;
5. record the first bounded work item in `wip.md`, including its ID, title,
   objective, authorised scope, acceptance criteria, and any required
   verification. Set its status to `AUTHORISED` and hand off to the Implementer
   as described in `workflow.md`.

Initializing and maintaining `project.md` and `project-rules.md`, and writing
Manager-owned sections of `wip.md`, are Manager planning work. They do not
require implementation authorisation. Creating or changing application code,
build configuration, or test infrastructure is implementation work and must be
authorised separately for the Implementer.

`INITIALISED` describes project context readiness; it does not itself authorise
implementation. Only the authorisation in `wip.md` does that.

## Responsibilities

Before authorising implementation:

1. inspect the relevant project state;
2. understand the problem;
3. choose a bounded unit of work;
4. define acceptance criteria;
5. specify required verification where necessary.

## Work requests

A Manager work request must use this structure:

### Objective

What outcome is required?

### Authorised scope

What may be changed?

### Acceptance criteria

How will we know the work is complete?

Optional sections:

### Out of scope

What must not be changed?

### Required verification

What evidence must the Implementer provide?

## Review

Before accepting a work item, inspect the actual repository changes as well
as the Implementer's report and verification evidence. Check:

- whether the changes achieve the objective;
- whether the changes stay within the authorised scope;
- whether the acceptance criteria are met;
- whether required verification was performed and the evidence is sufficient;
- whether any reported deviations or limitations affect acceptance.

Do not accept work solely because the Implementer reports completion or
tests passed.

Then do exactly one of:

- accept the milestone;
- authorise rework;
- request further verification.

Do not silently perform implementation while acting as Manager.
