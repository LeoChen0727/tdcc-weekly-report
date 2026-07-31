#!/usr/bin/env bash
set -euo pipefail

branch="${1:-${TARGET_BRANCH:-main}}"
max_attempts="${2:-5}"
expected_remote_sha="${CI_PUSH_EXPECTED_REMOTE_SHA:-}"

git config user.name "github-actions"
git config user.email "github-actions@github.com"

git gc --auto || true

if [ -n "$expected_remote_sha" ]; then
  if [[ ! "$expected_remote_sha" =~ ^[0-9a-f]{40}$ ]]; then
    echo "CI_PUSH_EXPECTED_REMOTE_SHA must be an exact 40-character Git SHA"
    exit 1
  fi
  remote_sha="$(git ls-remote origin "refs/heads/${branch}" | awk '{print $1}')"
  if [ -z "$remote_sha" ] || [ "$remote_sha" != "$expected_remote_sha" ]; then
    echo "Remote ${branch} drifted from CI_PUSH_EXPECTED_REMOTE_SHA; refusing rebase or push"
    exit 1
  fi
  if ! git merge-base --is-ancestor "$expected_remote_sha" HEAD; then
    echo "Local HEAD is not a descendant of CI_PUSH_EXPECTED_REMOTE_SHA"
    exit 1
  fi
  local_commit_count="$(git rev-list --count "${expected_remote_sha}..HEAD")"
  if [ "$local_commit_count" -ne 1 ]; then
    echo "Immutable-base push requires exactly one local commit; observed ${local_commit_count}"
    exit 1
  fi
  git push origin "HEAD:${branch}"
  pushed_sha="$(git rev-parse HEAD)"
  remote_sha="$(git ls-remote origin "refs/heads/${branch}" | awk '{print $1}')"
  if [ -z "$remote_sha" ] || [ "$remote_sha" != "$pushed_sha" ]; then
    echo "Remote ${branch} does not equal the pushed immutable-base commit"
    exit 1
  fi
  echo "Immutable-base push succeeded"
  exit 0
fi

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
