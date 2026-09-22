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
