# Git Worktree Materialization Safety

## Scope

This contract protects registered production, research, and maintenance
worktrees from large in-place ref transitions. These fixed worktrees can contain
thousands of tracked market-data, packet, signal, history, and published-output
files. Moving a fixed worktree to another commit can therefore rewrite many
thousands of files even when the requested task only needs a few source files.

## Fixed Worktree Rule

In a registered fixed worktree, fetches and ref reads are allowed, but a Codex
agent must not run an in-place command that can materialize another commit:

- `git switch`
- `git checkout`
- `git pull`
- `git rebase`
- `git reset --hard` to another commit

Read-only latest-main audit uses refs directly:

```text
git fetch origin main
git rev-parse HEAD
git rev-parse origin/main
git rev-list --left-right --count HEAD...origin/main
git show origin/main:<path>
git diff --stat HEAD origin/main
```

Before any user-approved in-place exception, run the non-mutating impact audit:

```text
python scripts/git_worktree_safety.py audit --repo-root . --target-ref origin/main
```

Any protected-path change or more than 250 changed paths is a hard block. A
smaller transition still requires explicit user approval in the current task.
The normal solution is a temporary sparse worktree, not an override.

## Sparse Task Worktree

Code edits, PR preparation, and code-only post-merge validators must use a
temporary sparse worktree when the fixed worktree is not already at the
required commit:

```text
python scripts/git_worktree_safety.py create-sparse \
  --repo-root . \
  --source-ref origin/main \
  --destination <system-temp-path> \
  --branch codex/<lane-task-name> \
  --include .github \
  --include AGENTS.md \
  --include config \
  --include docs \
  --include rules \
  --include scripts \
  --include tests
```

The helper registers the worktree with `--no-checkout`, configures sparse paths
before materialization, uses one checkout worker, serializes materialization per
repository, rejects high-churn paths, verifies the materialized-file limit, and
requires a clean result. It does not modify the fixed source worktree.

## Full Checkout Exceptions

Only consumers registered in
`config/git_worktree_materialization_contract.csv` may create a complete source
worktree. Full materialization must be temporary, under the system temp root,
serialized to one process per repository, and executed with one checkout
worker. Current approved consumers are the official daily six-PDF entrypoint,
the official TDCC weekly entrypoint, and the daily PDF replay validator.

The approved full-checkout exception does not permit an in-place ref transition
inside a registered fixed worktree.

Validators that require protected production data, history, or output artifacts
run in the official remote main workflow or through a registered official
entrypoint. An ordinary sparse task must not add protected roots merely to make
such a validator pass locally.

## Crash And Cleanup Boundary

The serialization lock is an operating-system file lock, so process termination
or a forced reboot releases the lock automatically. A failed helper removes
only the newly registered temporary worktree. It refuses to recursively delete
an unregistered path. Existing fixed worktrees, user changes, and unrelated Git
processes are outside its cleanup scope.

## Enforcement Boundary

Git has no native pre-checkout hook. This contract therefore enforces Codex
instructions, repository entrypoints, CI validators, and the supported helper;
it does not intercept a person who deliberately invokes `git.exe switch` or
another raw Git executable outside those paths. Installing a global Git wrapper
or modifying the user's PowerShell profile would affect unrelated repositories
and requires a separate explicit user decision.
