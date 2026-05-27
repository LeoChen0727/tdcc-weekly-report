#!/usr/bin/env bash
set -euo pipefail

branch="${1:-${TARGET_BRANCH:-main}}"
max_attempts="${2:-5}"

git config user.name "github-actions"
git config user.email "github-actions@github.com"

git gc --auto || true

for attempt in $(seq 1 "$max_attempts"); do
  echo "Push attempt ${attempt}/${max_attempts} to ${branch}"

  git fetch origin "$branch"
  git rebase --autostash "origin/${branch}"

  if git push origin "HEAD:${branch}"; then
    echo "Push succeeded"
    exit 0
  fi

  echo "Push failed on attempt ${attempt}"
  git status --short || true
  sleep_seconds=$((attempt * 20))
  echo "Sleeping ${sleep_seconds}s before retry"
  sleep "$sleep_seconds"
done

echo "Push failed after ${max_attempts} attempts"
exit 1
