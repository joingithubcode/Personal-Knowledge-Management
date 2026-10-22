#!/usr/bin/env bash
# bash test/run-tests.sh        -> escalate, stop at first passing tier
# ALL=1 bash test/run-tests.sh  -> run every tier
set -u
cd "$(dirname "$0")/.."

TIERS=(
  "1-haiku|opencode/claude-haiku-5-5|"
  "2-sonnet-medium|opencode/claude-sonnet-5-5|medium"
  "3-sonnet-high|opencode/claude-sonnet-5-5|high"
  "4-opus-medium|opencode/claude-opus-5-5|medium"
  "5-opus-high|opencode/claude-opus-5-5|high"
)
TESTS=(
  "pkm-architect|## Plan|Where should notes about postgres indexing go? Return your structured plan."
  "pkm-writer|## Result|DRY RUN: write a short atomic note about B-tree indexes in PostgreSQL. Do not create files."
  "pkm-reviewer|## Verdict|Review the 3 most recently changed notes in pkm/."
)
PROOF_MODEL="${PROOF_MODEL:-opencode/claude-sonnet-5-5}"

mkdir -p test/responses test/proofreading
SUM=test/summary.md
{ echo "# Agent test summary ($(date '+%F %H:%M'))"
  echo "| Agent | Tier | Format | Proofread |"
  echo "|---|---|---|---|"; } > "$SUM"

run() {
  local a=(run --agent "$1" --model "$2")
  [ -n "$3" ] && a+=(--variant "$3")
  timeout 300 opencode "${a[@]}" "$4" > "$5" 2> "$5.err"
}

for t in "${TESTS[@]}"; do
  IFS='|' read -r agent heading prompt <<< "$t"
  for tier in "${TIERS[@]}"; do
    IFS='|' read -r name model variant <<< "$tier"
    mkdir -p "test/responses/$name"
    f="test/responses/$name/$agent.md"
    echo ">> $agent @ $name"
    run "$agent" "$model" "$variant" "$prompt" "$f"
    if [ -s "$f" ] && grep -qF "$heading" "$f"; then fmt=PASS; else fmt=FAIL; fi
    pf="test/proofreading/$name-$agent.md"
    run pkm-proofreader "$PROOF_MODEL" medium "Proofread the agent response in $f. The agent was $agent and its task was: $prompt" "$pf"
    if grep -q "^VERDICT: APPROVE" "$pf" 2>/dev/null; then pr=APPROVE; else pr=REVISE; fi
    echo "| $agent | $name | $fmt | $pr |" >> "$SUM"
    if [ "${ALL:-0}" != 1 ] && [ "$fmt" = PASS ] && [ "$pr" = APPROVE ]; then
      echo "   passed, stopping ladder for $agent"; break
    fi
  done
done
cat "$SUM"
