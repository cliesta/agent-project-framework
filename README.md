# Agent Project Framework

A reusable Manager / Implementer workflow for agent-assisted projects.

Install into a new project directory:

```sh
./bootstrap.sh /path/to/new-project
```

The target directory must be empty or not yet exist. Installation refuses
non-empty directories, including those containing only hidden entries such as
`.git`, without modifying their contents.
