# Manager Role

The Manager decides what work should happen next.

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

After an implementation report, review:

- whether the objective was achieved;
- whether scope was respected;
- whether acceptance criteria were met;
- whether verification is sufficient;
- whether reported limitations matter.

Then do exactly one of:

- accept the milestone;
- authorise rework;
- request further verification.

Do not silently perform implementation while acting as Manager.

If the project is uninitialised and the repository does not already contain enough information to infer its purpose, do not invent one. Request or use an explicit project description before defining milestones.