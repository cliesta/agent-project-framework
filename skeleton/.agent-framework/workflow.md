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
- accepts or cancels the work, requests rework, or defines the next milestone.

Only the Manager may authorise new implementation work.

The Manager owns initialization and maintenance of `project.md` and
`project-rules.md`. This and the Manager-owned portions of `wip.md` are planning
work, not implementation, and do not require implementation authorisation.
Follow the initialization procedure in `manager.md` before authorising the
first work item. Project status `INITIALISED` does not replace work-item
authorisation in `wip.md`.

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
criteria, review baseline, authorisation, and review. The Implementer owns its progress,
blockers, and completion report.

The Implementer must not modify its own authorised scope or other
Manager-owned instructions.

Implementation may proceed only when the status is `AUTHORISED` and the
recorded objective, scope, acceptance criteria, and review baseline are sufficiently complete
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

When the Manager decides to abandon a work item:

`UNAUTHORISED | AUTHORISED | BLOCKED | READY_FOR_REVIEW → CANCELLED`

Status ownership and meaning:

- `UNAUTHORISED`: initial state; no implementation is authorised.
- `AUTHORISED`: set by the Manager after recording actionable instructions;
  hands control to the Implementer.
- `BLOCKED`: set by the Implementer after recording an issue requiring
  Manager input; hands control to the Manager.
- `READY_FOR_REVIEW`: set by the Implementer after completing the authorised
  work and recording its completion report; hands control to the Manager.
- `ACCEPTED`: set only by the Manager after review; closes the work item.
- `CANCELLED`: set only by the Manager after recording the cancellation reason
  and the disposition of any partial changes; closes the item without acceptance
  and ends its implementation authorisation.

To unblock work or request rework or further verification, the Manager
records its decision, updates the authorisation as needed, and sets the
status to `AUTHORISED`.

Acceptance or cancellation does not authorise further implementation. Any subsequent work
requires a new explicit Manager authorisation.

Before cancelling an item whose Implementer is still active, arrange for it
to stop and confirm that it has stopped before editing the work record. The
prohibition on concurrent Manager/Implementer edits still applies.

The Manager records the cancellation decision and reason under Manager review
in `wip.md`. Under `Partial changes on cancellation`, record what changes
remain, their verification state and any uncertainty, and whether they are
being retained or need separately authorised follow-up. Explicitly record
when no implementation changes were made. Preserve existing progress and
reports; cancellation does not require a fabricated completion report or
successful verification.

Cancellation does not accept partial work or authorise reverting, deleting,
or cleaning it up. Any such implementation requires a new bounded work item
after rollover. Include retained partial changes in the next item's review
baseline. `ACCEPTED` and `CANCELLED` are terminal states; further work receives
a new ID rather than reopening or relabelling a closed item.

### 4.2. Work-item history and rollover

The Manager owns work-item IDs, the previous-closed-item link, and rollover.
Assign each new work item a unique, filename-safe ID using letters, digits,
hyphens, or underscores (for example, `work-001`). Never reuse an ID from an
earlier item. Rework and unblocking retain the current item's ID and record.

Before replacing an `ACCEPTED` or `CANCELLED` item with a new work item, the Manager must:

1. ensure `wip.md` contains the closing decision and status. An accepted item
   must contain its complete completion report and review decision; a cancelled
   item must contain its cancellation reason and partial-change disposition,
   along with any existing Implementer records;
2. create `work-history/` if needed and copy the complete, unchanged `wip.md`
   to `work-history/<ID>.md`. Never overwrite or edit an existing history
   record. If the destination already exists, proceed only after verifying
   that it is identical to the current closed record; otherwise stop and
   report the conflict;
3. verify the archive matches the closed record before replacing `wip.md`.
   If archiving fails, leave `wip.md` intact;
4. create the next `wip.md` from `.agent-framework/templates/wip.md`, assigning
   a new unique ID and setting `Previous closed item` to a Markdown link
   such as `[work-001](work-history/work-001.md)`. Do not carry forward the
   previous item's authorisation, progress, blockers, report, or review;
5. record the new authorisation and set `AUTHORISED` only when the normal
   authorisation requirements are met. Until then, keep `UNAUTHORISED`.

The first item has `Previous closed item: None`. Archived files are exact
snapshots of the former root-level `wip.md`; paths recorded within those
snapshots refer to the project root.

Do not replace an unfinished item to start another one. When no next item is
being created, leave the closed record in `wip.md`. Archiving and creating a
new work record are Manager planning work and do not authorise implementation
by themselves. Keep the installed template clean for subsequent rollovers.

### 4.3. Review baseline

Before first authorising a work item, the Manager records a review baseline
in `wip.md` containing:

- the starting commit ID when one exists, or an explicit statement that the
  repository has no commits or does not use Git;
- pre-existing changes, including staged, unstaged, and untracked files when
  using Git, or an explicit statement that there are none;
- how the Manager will identify this work item's changes during review.

A commit ID is sufficient for a clean Git starting state. If pre-existing
changes overlap the work, preserve enough before-state evidence to separate
them, such as a saved patch and copies of relevant untracked files. Without
a usable commit, use a snapshot of the relevant starting files or another
explicit comparison method. Record where supporting evidence is retained;
a list of modified filenames alone does not preserve their starting contents.
Account for Manager planning edits separately from Implementer changes.

The baseline remains the original starting point through blocking, rework,
and further verification. Preserve its evidence until acceptance or cancellation so review
covers the entire item, not just the latest revision. If evidence is missing
or the comparison is ambiguous, the Manager must resolve that limitation
before accepting the item. A new work item receives a new baseline.

This does not require a branch, a commit, or a clean working tree. Do not
discard existing changes to create a baseline.

## 5. Every implementation request must contain

At minimum:

- an objective;
- authorised scope;
- acceptance criteria;
- a review baseline.

It should also contain explicit exclusions and required verification when these matter.

## 6. Scope discipline

Newly discovered work is not automatically authorised.

The Implementer may perform work that is clearly necessary to complete the
task and remains within the authorised scope.

Work that would expand or materially reinterpret the authorised scope
requires a Manager decision, even if it is necessary to complete the task.
Before performing that work, the Implementer must record the issue in
`wip.md`, set the status to `BLOCKED`, and return control to the Manager.

If it is unclear whether necessary work falls within the authorised scope,
the Implementer must follow the same blocking procedure.

Unrelated discoveries that do not prevent completion must be reported to
the Manager without being implemented. They do not require blocking the
authorised work.

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
- files added, modified, deleted, or renamed, and any difficulty separating
  the item's changes from pre-existing changes;
- verification performed;
- results;
- deviations from the authorised scope;
- known limitations or unresolved issues.

The Implementer then sets the status to `READY_FOR_REVIEW` and stops.
Setting `BLOCKED` also ends the Implementer's current action.

The Manager's current action ends only after it has fully persisted the review decision and any resulting authorisation changes and status transition required by the workflow.
Neither role continues into the other role's work.

## 9. Acceptance

Before accepting a work item, the Manager must inspect the actual repository
changes as well as the Implementer's report and verification evidence.
Use the recorded review baseline and its supporting evidence to distinguish
the item's changes from pre-existing changes, covering the original work and
all rework.

The review must check the changes against the objective, authorised scope,
acceptance criteria, and required verification, and assess any reported
deviations or limitations.

The Manager must not accept work solely because the Implementer reports
completion or tests passed.

The Manager may:

- accept the milestone;
- authorise specific rework;
- request additional verification;
- cancel the item using the procedure in section 4.1.

The Implementer must not mark its own work item accepted or cancelled.

## 10. Repository state

The repository must contain enough persistent information for a fresh agent session to determine:

- what project this is;
- what rules apply;
- what work is currently authorised;
- what has most recently been closed, and whether it was accepted or cancelled.

Conversation history must not be required to reconstruct the current working state.
