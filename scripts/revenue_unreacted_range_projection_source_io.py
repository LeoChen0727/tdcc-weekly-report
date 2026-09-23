"""Model-owned, business-neutral Git bytes for versioned revenue research."""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path
import re
import subprocess

V2_SOURCE_COMMIT = "4bcaa07123ef4a000c187dc2f19caefbec4cf252"
V3_SOURCE_COMMIT = "231d2e279a99a89f1888ece0361ea64d45f69ecd"
REVENUE_REL = "data/monthly_revenue_history/monthly_revenue_history.csv"
MONTHLY_RESOLUTION_REL = "config/revenue_unreacted_range_monthly_revenue_cross_market_resolution.csv"
PRICE_RESOLUTION_REL = "config/revenue_unreacted_range_price_comparability_resolution.csv"
PRICE_PREFIX = "data/stock_price_history/"
SOURCE_PATHS = (REVENUE_REL, MONTHLY_RESOLUTION_REL, PRICE_RESOLUTION_REL)


def _git(repository_root: Path, *args: str, input_bytes: bytes | None = None) -> bytes:
    try:
        return subprocess.run(
            ["git", "--no-replace-objects", "-C", str(repository_root), *args],
            input=input_bytes, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            check=True, timeout=300,
        ).stdout
    except (OSError, subprocess.SubprocessError) as exc:
        raise RuntimeError(f"cannot read versioned projection Git source: {args}") from exc


def ensure_source_commit(repository_root: Path, source_commit: str) -> None:
    if re.fullmatch(r"[0-9a-f]{40}", source_commit) is None:
        raise RuntimeError("projection source requires an exact full commit")
    # Existing official validation jobs use fetch-depth: 0. Missing history is
    # an explicit checkout prerequisite, never an implicit validator fetch.
    observed = _git(repository_root, "rev-parse", "--verify", f"{source_commit}^{{commit}}")
    if observed.decode("ascii").strip() != source_commit:
        raise RuntimeError("projection source commit identity mismatch")


def read_git_payloads(repository_root: Path, source_commit: str, paths: tuple[str, ...]) -> dict[str, bytes]:
    """Read exact regular-file Git blobs in one batch, without materialization."""
    ensure_source_commit(repository_root, source_commit)
    if not paths or any(
        not path or path.startswith(("/", "-")) or "\\" in path
        or any(part in {"", ".", ".."} for part in path.split("/"))
        for path in paths
    ):
        raise RuntimeError("projection source paths must be repository-relative")
    tree = _git(repository_root, "ls-tree", "-r", "-z", source_commit, "--", *paths)
    entries: list[tuple[str, str]] = []
    for item in tree.split(b"\0"):
        if not item:
            continue
        metadata, raw_path = item.split(b"\t", 1)
        mode, kind, oid = metadata.decode("ascii").split()
        path = raw_path.decode("utf-8")
        if mode != "100644" or kind != "blob":
            raise RuntimeError(f"projection source is not a regular Git blob: {path}")
        entries.append((path, oid))
    request = "".join(f"{oid}\n" for _, oid in entries).encode("ascii")
    output = _git(repository_root, "cat-file", "--batch", input_bytes=request)
    cursor = 0
    payloads: dict[str, bytes] = {}
    for path, expected_oid in entries:
        newline = output.index(b"\n", cursor)
        oid, kind, length = output[cursor:newline].decode("ascii").split()
        if oid != expected_oid or kind != "blob":
            raise RuntimeError(f"projection source batch identity mismatch: {path}")
        start = newline + 1
        end = start + int(length)
        if end >= len(output) or output[end:end + 1] != b"\n":
            raise RuntimeError(f"projection source truncated Git blob: {path}")
        payloads[path] = output[start:end]
        cursor = end + 1
    if cursor != len(output):
        raise RuntimeError("projection source has unexpected batch bytes")
    return payloads


@lru_cache(maxsize=2)
def _load_source_payloads(repository_root: Path, source_commit: str) -> dict[str, bytes]:
    payloads = read_git_payloads(repository_root, source_commit, (*SOURCE_PATHS, PRICE_PREFIX.rstrip("/")))
    missing = set(SOURCE_PATHS) - payloads.keys()
    if missing:
        raise RuntimeError(f"projection source is incomplete: {sorted(missing)}")
    prices = [path for path in payloads if path.startswith(PRICE_PREFIX)]
    if not prices or any(re.fullmatch(r"data/stock_price_history/[^/]+\.csv", path) is None for path in prices):
        raise RuntimeError("projection source price filename universe is invalid")
    return payloads


def load_source_payloads(
    repository_root: Path, source_commit: str, *, price_stock_ids: set[str] | None = None,
) -> dict[str, bytes]:
    payloads = _load_source_payloads(Path(repository_root).resolve(), source_commit)
    if price_stock_ids is None:
        return dict(payloads)
    selected = set(SOURCE_PATHS) | {f"{PRICE_PREFIX}{stock_id}.csv" for stock_id in price_stock_ids}
    missing = selected - payloads.keys()
    if missing:
        raise RuntimeError(f"bound projection source is missing requested prices: {sorted(missing)[:3]}")
    return {path: payloads[path] for path in selected}
