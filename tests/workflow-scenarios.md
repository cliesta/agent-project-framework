# Goal convergence scenarios

These are manual review scenarios, not automated agent evaluations. Install
into an empty temporary directory and walk each scenario through the Manager
and Implementer instructions. Check persistent records and lifecycle transitions;
no particular conversational wording is required. Numerical budgets below are
scenario inputs, not framework defaults.

## 1. Bounded delivery remains lightweight

Given a project requiring a CSV export with specified columns and escaping,
the Manager authorises a delivery item linked to that goal. The investigation
fields say Not applicable and no root `strategy.md` is created. The Implementer
implements and verifies the required cases. The Manager accepts against the
original criteria, records sufficient project completion evidence, marks the
outcome SATISFIED, and creates no further item. A discovered optional JSON
export is dismissed or deferred; it does not prevent completion.

Check: no artificial hypotheses, approach comparison, or research budget;
INITIALISED remains distinct from SATISFIED; acceptance and strategic finish
are both persisted.

## 2. Delivery can include an investigative spike

Given a fixed latency requirement and uncertainty about two storage options,
the Manager authorises an investigation with one comparable screening run per
option and capacity reserved for synthesis. It creates `strategy.md`, records
the shared measurement conditions and outcome branches, and accounts for both
runs. Evidence selects one option. A later implementation item is delivery,
links to the selection evidence, and still must satisfy the latency requirement.

Check: changing item type does not reset budgets or erase alternatives; the
spike's acceptance does not itself establish delivery success. Probing several
options occurs inside a bounded authorisation or sequential authorised items,
not simultaneous uncoordinated Implementers.

## 3. A negative result is useful completed work

Given an experiment with a two-run cap, a memory ceiling, and instructions to
stop after a valid measurement exceeds that ceiling, the first run exceeds it.
The Implementer stops, records the measurement and one run consumed, completes
the authorised report, and sets READY_FOR_REVIEW. The Manager inspects the
evidence, accepts the experiment, rejects the approach, and records a switch
rationale. It archives the closed item before authorising an alternative.

Check: no rework merely to obtain a positive result; the unused run is not
permission to keep searching; project requirements remain unchanged.

## 4. Inconclusive evidence does not earn unlimited retries

Given an investigation capped at three runs, all three leave the decision
unresolved. The agreed acceptance criteria allow an inconclusive report with
uncertainty and usage recorded. The Implementer sets READY_FOR_REVIEW without
a fourth run. The Manager can accept the report but must reassess before
continuation. An extension needs a concrete reason the next probe will be more
decisive and must fit the cumulative user limit; retain old limits and usage.

Check: neither a new ID, rework, nor switching options resets the cumulative
budget. If a user-set limit is exhausted, report the unmet outcome and await
a user decision, or record STOPPED under an already agreed stopping limit.

## 5. Budget reached before completion criteria are met

Given a two-run limit and a required result that cannot be produced within it,
the Implementer records partial evidence, usage, and unmet criteria and sets
BLOCKED. The Manager may clarify within constraints, request a user decision,
or cancel with partial-change disposition. It must not accept solely because
the budget ran out or silently weaken the criterion. If cancelled, consumed
runs remain charged in `strategy.md` before rollover.

Check: a blocked unfinished item is not overwritten to try another approach;
a cancellation does not authorise cleanup.

## 6. Interesting discoveries compete for attention

Given a completed probe that reveals five new avenues, the Manager records a
disposition for each. Deferred investigation avenues have a goal relevance and
reopening condition in `strategy.md`. The next selection compares decision
value and cost with existing alternatives and synthesis. A parked avenue with
no changed evidence stays parked even if a later session finds it interesting.

Check: fresh agents can reconstruct the selection without conversational
history; discoveries do not automatically become authorised work.

## 7. Stop despite unanswered questions

Given sufficient evidence to answer the project's agreed decision question,
the Manager records SATISFIED with references and finishes, even though some
mechanisms remain unexplained. If the question was whether any option is
feasible, a well-supported negative answer may satisfy it. If the project goal
was to deliver a working option, the same evidence leaves that goal unmet.

Check: project completion uses the original goal and evidence, not the
experiment's local acceptance or a retrospectively changed goal. Any necessary
new synthesis code or verification requires a separate authorised item;
summarising existing evidence is Manager planning.

## 8. Fixed delivery requirements survive resource exhaustion

Given a mandatory export correctness requirement and an exhausted user-set
resource limit, failing verification is not success. The Manager persists the
shortfall and returns to the user for a scope/resource decision. It does not
start new implementation while awaiting that decision. If the agreed limit
requires stopping, record STOPPED and the unmet requirement. Preserve any later
user-approved revision and resumption in the project history.

Check: budgets bound work; they do not override requirements or confer approval
for extensions.
