from __future__ import annotations

import csv
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PIN_REGISTRY = ROOT / "config/formal_model_evidence_pins.csv"


@dataclass(frozen=True)
class FormalEvidencePin:
    model_id: str
    approval_version: str
    evidence_path: str
    evidence_format: str
    evidence_version: str
    evidence_version_column: str
    canonical_sha256: str
    pin_status: str


def canonical_artifact_sha256(path: Path, evidence_format: str) -> str:
    if evidence_format == "csv":
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            columns = [column for column in (reader.fieldnames or []) if column != "generated_at"]
            rows = [{column: row.get(column, "") for column in columns} for row in reader]
        payload = json.dumps(
            {"columns": columns, "rows": rows},
            ensure_ascii=False,
            separators=(",", ":"),
        ).encode("utf-8")
    elif evidence_format == "text":
        text = path.read_text(encoding="utf-8-sig")
        normalized = "\n".join(line.rstrip() for line in text.splitlines()).strip() + "\n"
        payload = normalized.encode("utf-8")
    else:
        raise RuntimeError(f"unsupported formal evidence format: {evidence_format}")
    return hashlib.sha256(payload).hexdigest()


def load_evidence_pins(path: Path = PIN_REGISTRY) -> list[FormalEvidencePin]:
    if not path.exists():
        raise RuntimeError(f"missing formal model evidence pin registry: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    required = {
        "model_id",
        "approval_version",
        "evidence_path",
        "evidence_format",
        "evidence_version",
        "evidence_version_column",
        "canonical_sha256",
        "pin_status",
    }
    if not rows or not required.issubset(rows[0]):
        raise RuntimeError("formal model evidence pin registry schema is incomplete")
    return [
        FormalEvidencePin(
            model_id=row["model_id"].strip(),
            approval_version=row["approval_version"].strip(),
            evidence_path=Path(row["evidence_path"].strip()).as_posix(),
            evidence_format=row["evidence_format"].strip(),
            evidence_version=row["evidence_version"].strip(),
            evidence_version_column=row["evidence_version_column"].strip(),
            canonical_sha256=row["canonical_sha256"].strip().lower(),
            pin_status=row["pin_status"].strip(),
        )
        for row in rows
    ]


def validate_evidence_pin(pin: FormalEvidencePin, root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    path = root / pin.evidence_path
    if pin.pin_status != "pinned_formal_evidence":
        errors.append(f"{pin.model_id} pin_status must be pinned_formal_evidence")
    if not pin.evidence_version:
        errors.append(f"{pin.model_id} evidence_version must be populated")
    if len(pin.canonical_sha256) != 64 or any(char not in "0123456789abcdef" for char in pin.canonical_sha256):
        errors.append(f"{pin.model_id} canonical_sha256 must be a sha256 hex digest")
    if not path.exists():
        errors.append(f"{pin.model_id} evidence path missing: {pin.evidence_path}")
        return errors

    actual_hash = canonical_artifact_sha256(path, pin.evidence_format)
    if actual_hash != pin.canonical_sha256:
        errors.append(
            f"{pin.model_id} formal evidence canonical hash drift: "
            f"expected={pin.canonical_sha256}; actual={actual_hash}; path={pin.evidence_path}"
        )

    if pin.evidence_format == "csv":
        if not pin.evidence_version_column:
            errors.append(f"{pin.model_id} CSV pin requires evidence_version_column")
        else:
            with path.open("r", encoding="utf-8-sig", newline="") as handle:
                rows = list(csv.DictReader(handle))
            if not rows or pin.evidence_version_column not in rows[0]:
                errors.append(
                    f"{pin.model_id} evidence version column missing: {pin.evidence_version_column}"
                )
            else:
                versions = {row.get(pin.evidence_version_column, "").strip() for row in rows}
                if versions != {pin.evidence_version}:
                    errors.append(
                        f"{pin.model_id} evidence version drift: expected={pin.evidence_version}; "
                        f"actual={sorted(versions)}"
                    )
    return errors


def evidence_pin_for_model(
    model_id: str,
    approval_version: str,
    *,
    root: Path = ROOT,
) -> FormalEvidencePin:
    pins = [pin for pin in load_evidence_pins() if pin.model_id == model_id]
    if len(pins) != 1:
        raise RuntimeError(f"formal evidence registry must contain exactly one {model_id} pin")
    pin = pins[0]
    if pin.approval_version != approval_version:
        raise RuntimeError(
            f"{model_id} approval version does not match evidence pin: "
            f"approval={approval_version}; pin={pin.approval_version}"
        )
    errors = validate_evidence_pin(pin, root)
    if errors:
        raise RuntimeError("; ".join(errors))
    return pin
