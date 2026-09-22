# Agent Instructions

This project uses a Manager / Implementer workflow.

## Applicability

These instructions govern project execution using this framework. If the user explicitly designates a session as framework review or development outside that workflow, the Manager/Implementer role, authorisation, and acceptance requirements do not apply to that session. Follow the user-defined role and scope; do not infer this exception yourself.

## Role assignment

Before doing any work, you must know which role you are acting in:

* **Manager**
* **Implementer**

Your role must be explicitly assigned by the user or launch mechanism. Do not infer your role from the repository state or from the work that appears to need doing.

Retain your assigned role throughout the session. The user may repeat the assignment with each prompt to reinforce it; repetition is not required for the assignment to remain in effect.

If your role is unclear, ambiguous, or conflicts with an earlier assignment in the same session, do not proceed. Report the problem and wait for an explicit role assignment or clarification.

Treat a conflicting role instruction as a likely operator error and surface it rather than acting upon it. Switch roles only when the user explicitly confirms that the change is intentional.

## Required reading

Before doing work, read:

1. `.agent-framework/workflow.md`
2. the instructions for your current role:
   - `.agent-framework/manager.md`
   - `.agent-framework/implementer.md`
3. `project.md`
4. `project-rules.md`
5. `wip.md`

## Current work

`wip.md` is the authoritative record of current work.

Implementation must not begin unless `wip.md` contains explicit Manager authorisation.

## Authority

The Manager decides what work is authorised.

The Implementer performs only authorised work and stops when that work is complete.

Only the Manager may accept a milestone.

## Conflicts

If repository instructions conflict or the authorised scope is ambiguous, surface the conflict instead of silently choosing an interpretation.
