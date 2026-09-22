# Agent Project Framework

A reusable Manager / Implementer workflow for agent-assisted projects.

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
