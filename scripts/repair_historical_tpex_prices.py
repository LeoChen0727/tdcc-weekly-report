"""Bounded repair of separately authorized TPEx historical daily batches."""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import backfill_official_daily_price as backfill

DATES = tuple("20250901 20250902 20250903 20250904 20250905 20250909 20250910 "
              "20250911 20250917 20250918 20250919 20250922 20250923 20250924 "
              "20250925 20250926 20250930".split())
EVIDENCE = Path("retained-evidence/tpex-history-repair-202509")
MANIFEST = Path("config/tpex_historical_price_repair_202509.csv")
COLUMNS = ["date", "ticker", "name", "market", "open", "high", "low", "close", "volume", "turnover"]
BATCHES = {
    "202509": (DATES, EVIDENCE, MANIFEST),
    "202510": (
        tuple("20251001 20251002 20251003 20251007 20251008 20251009 "
              "20251013 20251014 20251016 20251020 20251021 20251022 "
              "20251023 20251027 20251028 20251029 20251030 20251031".split()),
        Path("retained-evidence/tpex-history-repair-202510"),
        Path("config/tpex_historical_price_repair_202510.csv"),
    ),
}


def batch_spec(batch: str) -> tuple[tuple[str, ...], Path, Path]:
    if batch not in BATCHES:
        raise ValueError(f"unauthorized TPEx repair batch: {batch}")
    return BATCHES[batch]


def sha(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def git_bytes(root: Path, ref: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{ref}:{path}"], cwd=root)


def rows(payload: bytes) -> list[dict[str, str]]:
    return list(csv.DictReader(io.StringIO(payload.decode("utf-8-sig"))))


def listed_bytes(payload: bytes) -> bytes:
    lines = payload.decode("utf-8-sig").splitlines(keepends=True)
    parsed = rows(payload)
    if len(lines) != len(parsed) + 1:
        raise ValueError("legacy CSV has multiline records; refusing physical-row rewrite")
    return "".join(line for line, row in zip(lines[1:], parsed) if row["market"] == "listed").encode("utf-8")


def build_replacement(before: bytes, document: dict, date: str) -> bytes:
    previous = rows(before)
    if not previous or list(previous[0]) != COLUMNS:
        raise ValueError("unexpected legacy daily CSV schema")
    if any(row["date"] != date or row["market"] not in {"otc", "listed"} for row in previous):
        raise ValueError("legacy daily CSV date/market mismatch")
    frame = backfill.parse_tpex_daily_price(document, date)
    if frame.empty:
        raise ValueError("official TPEx response has no eligible rows")
    listed_ids = {row["ticker"] for row in previous if row["market"] == "listed"}
    if listed_ids.intersection(frame["ticker"]):
        raise ValueError("cross-market security identity collision")
    header = before.decode("utf-8-sig").splitlines(keepends=True)[0].encode("utf-8")
    otc = frame[COLUMNS].to_csv(index=False, header=False, lineterminator="\n").encode("utf-8")
    result = (b"\xef\xbb\xbf" if before.startswith(b"\xef\xbb\xbf") else b"") + header + listed_bytes(before) + otc
    if listed_bytes(result) != listed_bytes(before):
        raise ValueError("listed rows changed")
    return result


def otc_batch(payload: bytes) -> str:
    batch = sorted(([row[key] for key in COLUMNS if key != "date"]
                    for row in rows(payload) if row["market"] == "otc"))
    return sha(json.dumps(batch, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))


def reject_repeated_batches(payloads: dict[str, bytes]) -> None:
    observed: dict[str, str] = {}
    for date, payload in payloads.items():
        digest = otc_batch(payload)
        if digest in observed:
            raise ValueError(f"TPEx batch repeats across dates: {observed[digest]}, {date}")
        observed[digest] = date


def collect(root: Path, reuse: Path | None, batch: str = "202509") -> None:
    """Only the selected authorized batch; verify and reuse existing raw."""
    dates, evidence, _ = batch_spec(batch)
    for date in dates:
        target = root / evidence / "raw" / f"{date}_TPEx_raw.json"
        receipt_path = target.with_name(f"{date}_TPEx_receipt.json")
        if target.exists() and receipt_path.exists():
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            if sha(target.read_bytes()) != receipt["sha256"]:
                raise ValueError(f"existing raw hash mismatch: {date}")
            continue
        if reuse and (reuse / target.name).is_file():
            raw = (reuse / target.name).read_bytes()
            receipt = json.loads((reuse / receipt_path.name).read_text(encoding="utf-8"))
            if sha(raw) != receipt["sha256"] or receipt["requested_date"] != date:
                raise ValueError(f"reused raw receipt mismatch: {date}")
        else:
            requested_at = datetime.now(timezone.utc).isoformat()
            url = f"https://www.tpex.org.tw/www/zh-tw/afterTrading/otc?date={date[:4]}/{date[4:6]}/{date[6:]}&type=EW&response=json"
            response = requests.get(url, timeout=40, headers={"User-Agent": "Mozilla/5.0"})
            response.raise_for_status()
            raw = response.content
            receipt = {"requested_date": date, "market": "TPEx", "url": url,
                       "requested_at": requested_at, "retrieved_at": datetime.now(timezone.utc).isoformat(),
                       "status_code": response.status_code, "final_url": response.url,
                       "sha256": sha(raw), "bytes": len(raw),
                       "current_retrieval_of_historical_data": True,
                       "original_publication_version_verified": False}
            time.sleep(1)
        document = json.loads(raw)
        if document.get("date") != date or document.get("stat") != "ok":
            raise ValueError(f"official response date/status mismatch: {date}")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
        receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"raw_received={date} bytes={len(raw)} sha256={sha(raw)}", flush=True)


def apply(root: Path, source_ref: str, batch: str = "202509") -> None:
    dates, evidence, manifest_path = batch_spec(batch)
    source_sha = subprocess.check_output(["git", "rev-parse", source_ref], cwd=root, text=True).strip()
    payloads: dict[str, bytes] = {}
    manifest = []
    for date in dates:
        path = f"data/daily_price/{date}.csv"
        before = git_bytes(root, source_sha, path)
        target = root / path
        if target.exists() and target.read_bytes() != before:
            raise ValueError(f"target differs from authorized source: {path}")
        raw_path = evidence / "raw" / f"{date}_TPEx_raw.json"
        receipt_path = raw_path.with_name(f"{date}_TPEx_receipt.json")
        raw = (root / raw_path).read_bytes()
        receipt = json.loads((root / receipt_path).read_text(encoding="utf-8"))
        if sha(raw) != receipt["sha256"]:
            raise ValueError(f"raw SHA mismatch: {date}")
        after = build_replacement(before, json.loads(raw), date)
        payloads[date] = after
        manifest.append({"date": date, "path": path, "source_sha": source_sha,
                         "before_sha256": sha(before), "after_sha256": sha(after),
                         "listed_sha256": sha(listed_bytes(before)),
                         "listed_rows": sum(row["market"] == "listed" for row in rows(before)),
                         "otc_before_rows": sum(row["market"] == "otc" for row in rows(before)),
                         "otc_after_rows": sum(row["market"] == "otc" for row in rows(after)),
                         "raw_path": raw_path.as_posix(), "raw_sha256": sha(raw),
                         "receipt_path": receipt_path.as_posix(), "url": receipt["url"],
                         "retrieved_at": receipt["retrieved_at"],
                         "original_publication_version_verified": "false"})
    reject_repeated_batches(payloads)
    for date, payload in payloads.items():
        target = root / "data/daily_price" / f"{date}.csv"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)
    with (root / manifest_path).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(manifest[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest)


def validate(root: Path, ref: str = "", batch: str = "202509") -> list[dict]:
    dates, _, manifest_path = batch_spec(batch)
    read = (lambda path: git_bytes(root, ref, path.as_posix())) if ref else (lambda path: (root / path).read_bytes())
    manifest = rows(read(manifest_path))
    if [row["date"] for row in manifest] != list(dates):
        raise ValueError(f"repair manifest must contain the exact authorized {len(dates)} dates")
    payloads = {}
    results = []
    for row in manifest:
        date = row["date"]
        if row["path"] != f"data/daily_price/{date}.csv":
            raise ValueError("repair path outside authorized date list")
        before = git_bytes(root, row["source_sha"], row["path"])
        raw = read(Path(row["raw_path"]))
        receipt = json.loads(read(Path(row["receipt_path"])))
        actual = read(Path(row["path"]))
        expected = build_replacement(before, json.loads(raw), date)
        if sha(before) != row["before_sha256"] or sha(raw) != row["raw_sha256"] or sha(raw) != receipt["sha256"]:
            raise ValueError(f"original/official raw SHA mismatch: {date}")
        if actual != expected or sha(actual) != row["after_sha256"]:
            raise ValueError(f"repaired rows differ from official raw: {date}")
        if listed_bytes(actual) != listed_bytes(before) or sha(listed_bytes(actual)) != row["listed_sha256"]:
            raise ValueError(f"listed physical rows changed: {date}")
        if receipt["requested_date"] != date or row["original_publication_version_verified"] != "false":
            raise ValueError(f"receipt date/PIT claim mismatch: {date}")
        payloads[date] = actual
        results.append({"date": date, "listed_rows_unchanged": int(row["listed_rows"]),
                        "otc_rows": sum(r["market"] == "otc" for r in rows(actual)), "official_parity": True})
    reject_repeated_batches(payloads)
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--batch", choices=tuple(BATCHES), default="202509")
    parser.add_argument("--source-ref", default="origin/main")
    parser.add_argument("--verify-ref", default="")
    parser.add_argument("--reuse-raw-root", type=Path)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--collect", action="store_true")
    mode.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    if args.collect:
        collect(args.repo_root, args.reuse_raw_root, args.batch)
    elif args.apply:
        apply(args.repo_root, args.source_ref, args.batch)
        print(json.dumps(validate(args.repo_root, batch=args.batch)))
    else:
        print(json.dumps(validate(args.repo_root, args.verify_ref, args.batch)))


if __name__ == "__main__":
    main()
