# Deferred Issues

Recorded following the repository review on 2026-09-22. All items below are
deferred; this list does not authorise implementation or change the installed
workflow. It tracks framework development, not work items in projects that
install the framework.

The review found the normal workflow suitable for a manually supervised pilot
with one active agent session at a time. These findings are not blockers for
that pilot. Recovery and continuity need more attention before unattended use;
packaging and documentation need attention before broad distribution.

## Higher priority: recovery and continuity

### ISSUE-001: Interrupted-session recovery and session ownership

- **Gap:** `AUTHORISED` does not distinguish work waiting to start from work
  already being executed. Concurrent Manager/Implementer edits are prohibited,
  but session ownership, multiple simultaneous Implementers, and recovery from
  a disappeared session are not explicitly addressed. Cancellation requires
  confirming that the Implementer stopped without defining this recovery case.
- **Impact:** A replacement session may overlap an active agent or proceed
  without reconciling partial work. Manual session management reduces the risk.
- **Possible resolution:** Define a restart procedure that establishes the
  previous session has stopped, inspects partial changes, reconciles progress,
  preserves the original baseline, and resumes or returns control to the
  Manager. Explicitly prohibit simultaneous Implementers. A locking system is
  not necessarily required.
- **Relevant file:** [workflow.md](skeleton/.agent-framework/workflow.md).

### ISSUE-002: Decision history can be overwritten during rework

- **Gap:** Rework retains the item and original baseline, but earlier
  authorisations, scope, acceptance criteria, review decisions, and verification
  attempts do not have an explicit preservation requirement. The template has
  single sections that can be overwritten.
- **Impact:** A closed record can show the final agreement without explaining
  how it changed.
- **Possible resolution:** Add a lightweight append-only decision and rework
  log, particularly for scope and acceptance-criteria changes.
- **Relevant files:** [workflow.md](skeleton/.agent-framework/workflow.md),
  [WIP template](skeleton/templates/wip.md).

### ISSUE-003: Unresolved discoveries have no defined follow-up destination

- **Gap:** Implementers must report unrelated discoveries, but rollover clears
  the active record without requiring the Manager to triage those discoveries.
  They remain in archives but may never receive further attention.
- **Impact:** Follow-up obligations can be forgotten across work items.
- **Possible resolution:** Introduce a small backlog or require a disposition
  before closure: scheduled, deferred, dismissed, or linked to subsequent work.
- **Relevant file:** [workflow.md](skeleton/.agent-framework/workflow.md).

## Medium priority: validation and operational defects

### ISSUE-004: Validation covers installation rather than workflow usability

- **Gap:** The 10 installer regression tests passed at review time, but they
  verify copying and rejection behaviour rather than the main workflow. Exact
  source comparisons also accept an empty instruction file as valid payload.
- **Impact:** Passing tests do not demonstrate that agents can complete the
  lifecycle or recover from exceptional situations.
- **Possible resolution:** Add worked scenarios covering initialisation,
  blocking, rework, cancellation with partial changes, interruption recovery,
  and rollover. Consider structural checks for required sections, references,
  and status consistency, alongside actual agent walkthroughs.
- **Relevant file:** [test_bootstrap.py](tests/test_bootstrap.py).

### ISSUE-005: Failed installation can leave a target that rejects retries

- **Confirmed behaviour:** In a temporary framework copy, removing the required
  `project.md` source template caused installation to fail after writing part of
  the payload. Restoring the source and retrying failed because the destination
  was now non-empty.
- **Impact:** A failed installation requires manual recovery. This does not
  affect the ordinary successful installation path.
- **Possible resolution:** Preflight required sources, stage the payload before
  installing it, and define safe recovery from partial failure.
- **Relevant file:** [bootstrap.sh](bootstrap.sh).

### ISSUE-006: Archived Markdown links resolve incorrectly

- **Gap:** A link such as `work-history/work-001.md` works in root-level
  `wip.md`, but resolves to `work-history/work-history/work-001.md` after the
  record is copied unchanged into `work-history/`. The documented convention
  that archive paths refer to the project root does not fix ordinary Markdown
  link rendering.
- **Impact:** Humans cannot reliably navigate history through those links.
- **Possible resolution:** Choose a link convention that works in both
  locations, or provide a navigable history index while retaining unchanged
  archive records.
- **Relevant file:** [workflow.md](skeleton/.agent-framework/workflow.md).

## Lower priority: payload and maintenance

### ISSUE-007: Leading-hyphen relative installation targets fail

- **Confirmed behaviour:** Passing `-project` as the target causes `mkdir` to
  interpret it as an option and fail.
- **Possible resolution:** Use `--` where appropriate for commands receiving
  paths and cover this target form in installer tests.
- **Relevant file:** [bootstrap.sh](bootstrap.sh).

### ISSUE-008: Empty, unused change guidelines are installed

- **Gap:** `change-guidelines.md` is empty, is installed into every project,
  and is not included in required reading.
- **Possible resolution:** Remove it or give it a defined purpose and content.
- **Relevant files:**
  [change-guidelines.md](skeleton/.agent-framework/change-guidelines.md),
  [installed AGENTS.md](skeleton/AGENTS.md).

### ISSUE-009: Repeated normative instructions create maintenance risk

- **Gap:** Request structure, completion reporting, and acceptance rules are
  repeated across workflow instructions, role documents, and the template.
  They largely agree today, but may drift as the framework changes.
- **Possible resolution:** Keep normative lifecycle rules in one place and
  use role documents as concise operational checklists with references.
- **Relevant files:** [workflow.md](skeleton/.agent-framework/workflow.md),
  [manager.md](skeleton/.agent-framework/manager.md),
  [implementer.md](skeleton/.agent-framework/implementer.md),
  [WIP template](skeleton/templates/wip.md).

## Reuse and distribution decisions

### ISSUE-010: Installed version and upgrade policy are missing

Installed projects do not identify their framework version or have a documented
way to receive fixes while preserving customisations. Define a version marker
and an upgrade policy before supporting a growing population of installations;
an automated updater is not necessarily needed.

### ISSUE-011: Reuse licence is missing

The repository has no licence defining reuse rights. Choose and add an
appropriate licence before public distribution.

### ISSUE-012: Adoption into existing projects is unsupported

The installer intentionally refuses all non-empty directories, including those
containing only `.git`. This is a documented constraint, not an installer bug.
Decide whether existing projects are an intended audience; if so, document a
safe migration path that preserves existing instructions and project files.

### ISSUE-013: Post-closure evidence retention is undefined

The workflow requires baseline evidence to be preserved until acceptance or
cancellation, but does not define retention afterwards. If history is intended
to support later audits, specify what baseline and verification evidence must
remain available and how archived records reference it.
