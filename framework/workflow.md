# Manager / Implementer Workflow

## 1. Roles

Work is divided between two roles:

- **Manager** — decides what should be done.
- **Implementer** — performs explicitly authorised work.

An agent must know which role it is currently performing.

## 2. Manager authority

The Manager:

- analyses the current state of the project;
- chooses the next unit of work;
- defines the objective and acceptance criteria;
- authorises implementation;
- reviews the Implementer's report;
- accepts the work, requests rework, or defines the next milestone.

Only the Manager may authorise new implementation work.

## 3. Implementer authority

The Implementer may:

- inspect the repository as needed;
- modify files necessary to complete the authorised work;
- run tests, builds, analysis, and other verification required by the task.

The Implementer must not:

- choose a new milestone;
- broaden the scope of the task;
- perform unrelated cleanup or refactoring;
- continue into additional work after completing the authorised task.

## 4. Authorisation and active work

`wip.md` is the authoritative record of one active work item.

The Manager owns the work item's objective, authorised scope, acceptance
criteria, authorisation, and review. The Implementer owns its progress,
blockers, and completion report.

The Implementer must not modify its own authorised scope or other
Manager-owned instructions.

Implementation may proceed only when the status is `AUTHORISED` and the
recorded objective, scope, and acceptance criteria are sufficiently complete
and non-contradictory to carry out the work. A status value alone does not
authorise implementation.

If the Implementer finds that these conditions are not met for an item
marked `AUTHORISED`, it must record the problem, set the status to `BLOCKED`,
and return control to the Manager.

Concurrent Manager/Implementer edits are prohibited in v0.1.

### 4.1. Work-item lifecycle

The normal lifecycle is:

`UNAUTHORISED → AUTHORISED → READY_FOR_REVIEW → ACCEPTED`

When Manager input is required during implementation:

`AUTHORISED → BLOCKED → AUTHORISED`

When review requires rework or further verification:

`READY_FOR_REVIEW → AUTHORISED`

Status ownership and meaning:

- `UNAUTHORISED`: initial state; no implementation is authorised.
- `AUTHORISED`: set by the Manager after recording actionable instructions;
  hands control to the Implementer.
- `BLOCKED`: set by the Implementer after recording an issue requiring
  Manager input; hands control to the Manager.
- `READY_FOR_REVIEW`: set by the Implementer after completing the authorised
  work and recording its completion report; hands control to the Manager.
- `ACCEPTED`: set only by the Manager after review; closes the work item.

To unblock work or request rework or further verification, the Manager
records its decision, updates the authorisation as needed, and sets the
status to `AUTHORISED`.

Acceptance does not authorise further implementation. Any subsequent work
requires a new explicit Manager authorisation.

## 5. Every implementation request must contain

At minimum:

- an objective;
- authorised scope;
- acceptance criteria.

It should also contain explicit exclusions and required verification when these matter.

## 6. Scope discipline

While implementing, newly discovered work is not automatically authorised.

If the Implementer discovers:

- another bug;
- desirable refactoring;
- missing functionality;
- architectural problems;
- unrelated failing tests;

it should report them to the Manager unless they directly prevent completion of the authorised task.

## 7. Verification

Implementation is not complete merely because code has been written.

The Implementer must perform reasonable verification appropriate to the task and report:

- what was verified;
- how it was verified;
- whether it passed;
- any limitations or uncertainty.

## 8. Handoff

Before announcing a handoff conversationally, the agent must persist the
relevant instructions, report, or decision and the resulting status in
`wip.md`.

The handoff message must identify the work item, its status, and the role
that should act next. A handoff does not itself launch another agent.

When authorised work is complete, the Implementer records a completion
report summarising:

- what changed;
- verification performed;
- results;
- deviations from the authorised scope;
- known limitations or unresolved issues.

The Implementer then sets the status to `READY_FOR_REVIEW` and stops.
Setting `BLOCKED` also ends the Implementer's current action.

The Manager's current action ends only after it has fully persisted the review decision and any resulting authorisation changes and status transition required by the workflow.
Neither role continues into the other role's work.

## 9. Acceptance

The Manager reviews the implementation and evidence.

The Manager may:

- accept the milestone;
- authorise specific rework;
- request additional verification.

The Implementer must not mark its own milestone accepted.

## 10. Repository state

The repository must contain enough persistent information for a fresh agent session to determine:

- what project this is;
- what rules apply;
- what work is currently authorised;
- what has most recently been completed.

Conversation history must not be required to reconstruct the current working state.
