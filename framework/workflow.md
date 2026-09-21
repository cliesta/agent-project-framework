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

## 4. Work must be explicitly authorised

Implementation begins only when there is a written Manager instruction describing the authorised work.

If no implementation work is currently authorised, the Implementer must not make changes.

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

When authorised work is complete, the Implementer stops and returns control to the Manager.

The implementation report must summarise:

- what changed;
- verification performed;
- results;
- deviations from the authorised scope;
- known limitations or unresolved issues.

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