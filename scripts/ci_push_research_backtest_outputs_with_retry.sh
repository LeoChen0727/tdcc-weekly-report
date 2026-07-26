#!/usr/bin/env bash
set -euo pipefail

branch="${1:-${TARGET_BRANCH:-main}}"
max_attempts="${2:-5}"

generated_prefixes=(
  "data/msci_index_reviews/"
  "docs/latest/"
  "output/history/catalyst_performance/"
  "output/history/daily_signals/"
  "output/history/market_timing/"
  "output/history/msci_index_reviews/"
  "output/history/research/"
  "output/history/surge_model/"
  "output/history/tdcc_signals/"
  "output/history/volume_breakout/"
  "output/latest/"
)

git config user.name "github-actions"
git config user.email "github-actions@github.com"

git gc --auto || true

path_is_generated_output() {
  local path="$1"
  local prefix
  for prefix in "${generated_prefixes[@]}"; do
    if [[ "$path" == "$prefix"* ]]; then
      return 0
    fi
  done
  return 1
}

resolve_research_output_rebase_conflicts() {
  local conflicted path
  mapfile -t conflicted < <(git diff --name-only --diff-filter=U)

  if [[ "${#conflicted[@]}" -eq 0 ]]; then
    return 0
  fi

  echo "Rebase conflicts detected; validating generated output paths"
  for path in "${conflicted[@]}"; do
    if ! path_is_generated_output "$path"; then
      echo "Unexpected rebase conflict outside research-generated outputs: $path" >&2
      git rebase --abort || true
      return 1
    fi
  done

  echo "Resolving generated output conflicts in favor of this run"
  for path in "${conflicted[@]}"; do
    git checkout --theirs -- "$path"
    git add "$path"
  done

  GIT_EDITOR=true git rebase --continue
}

finish_rebase_if_needed() {
  while [[ -d .git/rebase-merge || -d .git/rebase-apply ]]; do
    resolve_research_output_rebase_conflicts
  done
}

for attempt in $(seq 1 "$max_attempts"); do
  echo "Research output push attempt ${attempt}/${max_attempts} to ${branch}"

  git fetch origin "$branch"
  if ! git rebase --autostash "origin/${branch}"; then
    finish_rebase_if_needed
  fi

  if git push origin "HEAD:${branch}"; then
    echo "Research output push succeeded"
    exit 0
  fi

  echo "Research output push failed on attempt ${attempt}"
  git status --short || true
  sleep_seconds=$((attempt * 20))
  echo "Sleeping ${sleep_seconds}s before retry"
  sleep "$sleep_seconds"
done

echo "Research output push failed after ${max_attempts} attempts"
exit 1
