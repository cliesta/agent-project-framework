# Agent Project Framework

A reusable Manager / Implementer workflow for agent-assisted projects.

Known limitations and deferred improvements are tracked in [ISSUES.md](ISSUES.md).

Install into a new project directory:

```sh
./bootstrap.sh /path/to/new-project
```

The target directory must be empty or not yet exist. Installation refuses
non-empty directories, including those containing only hidden entries such as
`.git`, without modifying their contents.

## First use

Open an agent session in the installed project and explicitly assign the
Manager role, including a description of what you want to build. For example:

> Act as Manager. Follow AGENTS.md and initialize this project. I want to build
> a command-line tool that tracks personal reading notes in local Markdown
> files. Ask for any essential missing information, then authorise the first
> bounded work item in wip.md.

The Manager fills in `project.md` and `project-rules.md`, marks unresolved
decisions explicitly, and sets the project status to `INITIALISED` when there
is enough context to begin. It then records the first authorisation in
`wip.md`. Creating build or test infrastructure is separate Implementer work.

Once the Manager hands off an `AUTHORISED` item, open an Implementer session:

> Act as Implementer. Follow AGENTS.md and carry out the authorised work item
> in wip.md.

When the item is `READY_FOR_REVIEW`, return to the Manager for review. Handoff
messages do not launch another agent; you must start or resume the appropriate
session. The project status alone does not authorise implementation.

## Handoff commits

In Git projects, agents automatically create local commits at handoffs after
updating `wip.md`. This includes authorisation, blocking, completion, rework,
acceptance, and cancellation. Commit messages identify the work item, role,
and status; handoff messages include the commit ID. A commit is a checkpoint,
not acceptance of the work.

Agents include only the outgoing role's changes and preserve unrelated or
pre-existing changes. They do not push automatically. If a commit cannot be
made safely or fails, the agent records the reason and explicitly hands off
the uncommitted state. Projects without Git continue using file-based
handoffs. Details are in `.agent-framework/workflow.md` section 8.1.

To use this change in an existing installation, apply the updated `workflow.md`,
`manager.md`, and `implementer.md` from `skeleton/.agent-framework/` to its
`.agent-framework/` directory, preserving project-specific customisations.
The installer does not update non-empty projects.

## Starting the next work item

Before replacing an accepted or cancelled item, the Manager preserves its complete record
in `work-history/<ID>.md`, without overwriting existing history. The next
`wip.md` starts from the clean template installed at
`.agent-framework/templates/wip.md`, receives a new unique ID, and links to
the previous closed item. It requires a fresh Manager authorisation.

If no next item is needed, the closed record stays in `wip.md`. Rework stays
in the current record with the same ID. The detailed rollover procedure is in
`.agent-framework/workflow.md` in the installed project.

Only the Manager may cancel work, recording the reason and what happened to
any partial changes before setting `CANCELLED`. Cancellation does not accept
those changes or permit automatic reversal; cleanup requires a new authorised
work item. Cancelled records are archived under the same rules as accepted ones.

## Testing

Run the installer regression tests from the framework repository root:

```sh
python3 tests/test_bootstrap.py
```

The tests require Bash and Python 3, with no third-party packages. They install
into temporary directories, verify the installed payload and clean WIP
template, and check that rejected installations preserve existing contents.

## Goal alignment and investigations

Every project defines completion evidence, non-goals, and constraints in
`project.md`. Its outcome (`ONGOING`, `SATISFIED`, or `STOPPED`) is separate
from its initialization status. Every work item links to a goal and explains
why it is needed now. The Manager reviews project progress separately from
whether the work item was carried out correctly, and finishes once agreed
completion evidence is sufficient.

Planning is proportional to the item. Delivery work such as adding a specified
CSV export needs scope, acceptance criteria, and verification; it does not need
an approach portfolio. An investigation such as deciding which storage design
can meet a latency target additionally needs a decision question, expected
evidence, actions for positive/negative/inconclusive results, an observable
budget, and stopping rules. A project can use both kinds of work item.

At the first investigation, the Manager creates `strategy.md` from
`.agent-framework/templates/strategy.md`. It tracks alternatives, evidence,
cumulative budgets, choices, and reopening conditions. The Manager screens a
bounded set of plausible alternatives before investing deeply, or records why
existing evidence justifies focusing on one. Further experiments must justify
their value relative to alternatives and concluding now. New work-item IDs and
rework do not reset exploration budgets.

A negative experiment can be accepted while its approach is rejected. An
inconclusive experiment does not automatically earn another run. Newly found
avenues are triaged, not automatically added to the project's obligations.
For delivery, exhausted resources with unmet requirements mean reporting the
shortfall and seeking a user decision, not relaxing the definition of success.
Normative rules are in `workflow.md` sections 5.1 and 9.1.

### Applying these changes to an existing installation

The installer still refuses non-empty directories. Merge the updated
`skeleton/AGENTS.md` and the workflow, Manager, and Implementer instructions
under `skeleton/.agent-framework/` into the installation, preserving local
customisations. Update `.agent-framework/templates/wip.md` from
`skeleton/templates/wip.md` and install `skeleton/templates/strategy.md` at
`.agent-framework/templates/strategy.md`.

Have the Manager merge the new goal/completion/constraint/outcome/revision
sections from `skeleton/templates/project.md` into the existing `project.md`;
do not overwrite project content. Preserve active WIP records and immutable
archives. At the next Manager handoff, with the Implementer stopped, add the
new WIP planning/review fields and reconcile investigation evidence and usage
from existing records. Unknown prior usage must be marked unknown and resolved
or conservatively accounted for before further budget is authorised; installing
a template does not reset it. Delivery-only projects need no `strategy.md`.

## Workflow validation

[Worked scenarios](tests/workflow-scenarios.md) describe expected behaviour for
bounded delivery, investigations, budget exhaustion, switching, and completion.
Use them for manual walkthroughs against an installed payload. Installer tests
check packaging, not agent adherence to these behavioural rules.
