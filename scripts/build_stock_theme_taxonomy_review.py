from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import LATEST_DIR, now_text, read_csv, safe_str, write_csv  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
DOCS_LATEST_DIR = ROOT / "docs" / "latest"

ALL_CANDIDATES = LATEST_DIR / "all_candidates_latest.csv"
TAXONOMY = LATEST_DIR / "stock_theme_taxonomy_latest.csv"

REVIEW_CSV = LATEST_DIR / "stock_theme_taxonomy_review_latest.csv"
REVIEW_MD = LATEST_DIR / "stock_theme_taxonomy_review_latest.md"
DOCS_REVIEW_CSV = DOCS_LATEST_DIR / "stock_theme_taxonomy_review_latest.csv"
DOCS_REVIEW_MD = DOCS_LATEST_DIR / "stock_theme_taxonomy_review_latest.md"


CORE_STRUCTURAL_BUCKETS = {
    "ai_server_ipc_theme",
    "ai_server_mechanical_theme",
    "ai_server_pc_theme",
    "ai_pc_consumer_theme",
    "memory_hbm_theme",
    "memory_packaging_testing_theme",
    "semiconductor_theme",
    "semiconductor_equipment_material_theme",
    "semiconductor_test_interface_theme",
    "semiconductor_testing_theme",
    "ai_chip_testing_theme",
    "asic_advanced_process_theme",
    "advanced_packaging_cowos_theme",
    "abf_substrate_theme",
    "pcb_ccl_theme",
    "glass_fiber_ccl_theme",
    "high_speed_ccl_satellite_theme",
    "fpc_flexible_pcb_theme",
    "low_earth_orbit_satellite_theme",
    "network_optical_datacenter_theme",
    "network_communication_theme",
    "optical_communication_cpo_theme",
    "high_speed_interconnect_theme",
    "passive_component_theme",
    "power_supply_theme",
    "thermal_solution_theme",
    "robotics_precision_motion_theme",
    "robotics_automation_theme",
    "robotics_ipc_edge_ai_theme",
    "robotics_ai_manufacturing_theme",
    "robotics_component_theme",
    "robotics_optics_sensor_theme",
}


def norm_id(value: object) -> str:
    text = safe_str(value).strip()
    if not text:
        return ""
    return text.zfill(4)


def classify_review_status(row: pd.Series) -> str:
    bucket = safe_str(row.get("effective_structural_theme_bucket", ""))
    status = safe_str(row.get("effective_theme_structural_status", ""))
    raw_status = safe_str(row.get("theme_structural_status", ""))
    if not bucket and raw_status == "core_mainstream_theme":
        return "industry_core_needs_market_theme"
    if not bucket and raw_status == "non_mainstream_theme":
        return "industry_non_mainstream_only"
    if not bucket:
        return "needs_market_theme_mapping"
    if bucket in CORE_STRUCTURAL_BUCKETS and status == "core_mainstream_theme":
        return "core_ai_related_theme"
    if status == "non_mainstream_theme":
        return "non_mainstream_theme"
    return "mapped_needs_review"


def coalesce_columns(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    pairs = [
        ("effective_primary_theme", ["taxonomy_primary_theme", "taxonomy_primary_theme_y", "taxonomy_primary_theme_x", "primary_theme"]),
        ("effective_secondary_themes", ["taxonomy_secondary_themes", "taxonomy_secondary_themes_y", "taxonomy_secondary_themes_x", "secondary_themes"]),
        ("effective_structural_theme_bucket", ["taxonomy_structural_theme_bucket", "taxonomy_structural_theme_bucket_y", "taxonomy_structural_theme_bucket_x", "structural_theme_bucket"]),
        ("effective_theme_structural_status", ["taxonomy_theme_structural_status", "taxonomy_theme_structural_status_y", "taxonomy_theme_structural_status_x", "theme_structural_status"]),
        ("effective_theme_mainstream_label", ["taxonomy_theme_mainstream_label", "taxonomy_theme_mainstream_label_y", "taxonomy_theme_mainstream_label_x", "theme_mainstream_label"]),
        ("effective_taxonomy_source", ["taxonomy_source", "taxonomy_source_y", "taxonomy_source_x", "theme_taxonomy_source"]),
        ("effective_confidence", ["taxonomy_confidence", "taxonomy_confidence_y", "taxonomy_confidence_x", "theme_taxonomy_confidence", "confidence"]),
        ("effective_notes", ["taxonomy_notes", "taxonomy_notes_y", "taxonomy_notes_x", "theme_taxonomy_note", "notes"]),
    ]
    for target, sources in pairs:
        out[target] = ""
        for source in sources:
            if source in out.columns:
                values = out[source].fillna("").astype(str)
                out[target] = out[target].where(out[target].astype(str).str.strip().ne(""), values)
        out[target] = out[target].fillna("")
    return out


def build_review() -> pd.DataFrame:
    candidates = read_csv(ALL_CANDIDATES, dtype=str, keep_default_na=False)
    taxonomy = read_csv(TAXONOMY, dtype=str, keep_default_na=False)
    if candidates.empty:
        return pd.DataFrame()

    candidates = candidates.copy()
    candidates["stock_id"] = candidates["stock_id"].map(norm_id)
    if not taxonomy.empty:
        taxonomy = taxonomy.copy()
        taxonomy["stock_id"] = taxonomy["stock_id"].map(norm_id)
        keep_cols = [
            "stock_id",
            "primary_theme",
            "secondary_themes",
            "structural_theme_bucket",
            "theme_structural_status",
            "theme_mainstream_label",
            "taxonomy_source",
            "confidence",
            "notes",
        ]
        taxonomy = taxonomy[[col for col in keep_cols if col in taxonomy.columns]]
        rename_map = {
            "primary_theme": "taxonomy_primary_theme",
            "secondary_themes": "taxonomy_secondary_themes",
            "structural_theme_bucket": "taxonomy_structural_theme_bucket",
            "theme_structural_status": "taxonomy_theme_structural_status",
            "theme_mainstream_label": "taxonomy_theme_mainstream_label",
            "notes": "taxonomy_notes",
        }
        taxonomy = taxonomy.rename(columns=rename_map)
        merged = candidates.merge(taxonomy, on="stock_id", how="left", suffixes=("", "_review"))
    else:
        merged = candidates

    for col in [
        "primary_theme",
        "secondary_themes",
        "structural_theme_bucket",
        "theme_structural_status",
        "theme_mainstream_label",
        "taxonomy_source",
        "confidence",
        "notes",
        "taxonomy_primary_theme",
        "taxonomy_secondary_themes",
        "taxonomy_structural_theme_bucket",
        "taxonomy_theme_structural_status",
        "taxonomy_theme_mainstream_label",
        "taxonomy_confidence",
        "taxonomy_notes",
    ]:
        if col not in merged.columns:
            merged[col] = ""
        merged[col] = merged[col].fillna("")

    merged = coalesce_columns(merged)
    merged["taxonomy_review_status"] = merged.apply(classify_review_status, axis=1)
    merged["review_priority"] = 3
    merged.loc[
        merged["taxonomy_review_status"].isin(["needs_market_theme_mapping", "industry_core_needs_market_theme"]),
        "review_priority",
    ] = 1
    merged.loc[merged["taxonomy_review_status"].eq("mapped_needs_review"), "review_priority"] = 2
    merged.loc[
        merged["taxonomy_review_status"].eq("core_ai_related_theme")
        & merged["effective_confidence"].astype(str).str.lower().isin(["", "low"]),
        "review_priority",
    ] = 2
    merged.loc[merged["taxonomy_review_status"].eq("industry_non_mainstream_only"), "review_priority"] = 4

    output_cols = [
        "review_priority",
        "taxonomy_review_status",
        "stock_id",
        "stock_name",
        "industry",
        "category",
        "decision_priority",
        "decision_score",
        "risk_handling_bucket",
        "effective_primary_theme",
        "effective_secondary_themes",
        "effective_structural_theme_bucket",
        "effective_theme_structural_status",
        "effective_theme_mainstream_label",
        "effective_taxonomy_source",
        "effective_confidence",
        "volume_ratio",
        "return_5d",
        "return_20d",
        "why_selected",
        "downgrade_flags",
        "effective_notes",
    ]
    for col in output_cols:
        if col not in merged.columns:
            merged[col] = ""
    out = merged[output_cols].drop_duplicates(["stock_id", "category", "decision_priority", "risk_handling_bucket"])
    out["_score"] = pd.to_numeric(out["decision_score"], errors="coerce").fillna(0)
    out["_vol"] = pd.to_numeric(out["volume_ratio"], errors="coerce").fillna(0)
    out = out.sort_values(["review_priority", "_score", "_vol", "stock_id"], ascending=[True, False, False, True])
    return out.drop(columns=["_score", "_vol"]).reset_index(drop=True)


def build_markdown(df: pd.DataFrame) -> str:
    lines = [
        "# Stock Theme Taxonomy Review",
        "",
        f"- generated_at: {now_text()}",
        f"- source_candidates: {ALL_CANDIDATES.as_posix()}",
        f"- source_taxonomy: {TAXONOMY.as_posix()}",
        "",
        "## Usage",
        "",
        "- `needs_market_theme_mapping`: today has a signal but no usable market-theme taxonomy. Do not route to the main attack list until reviewed.",
        "- `industry_core_needs_market_theme`: official industry is electronic/semiconductor-like, but market theme is still missing. This is not enough for mainstream routing.",
        "- `core_ai_related_theme`: explicitly mapped to AI/electronics/robotics/passive/PCB/LEO/optical/semiconductor theme buckets.",
        "- `industry_non_mainstream_only`: official industry is non-mainstream and no market-theme override exists.",
        "- `non_mainstream_theme`: explicitly mapped to a non-core/non-AI market theme.",
        "- `mapped_needs_review`: mapped but low confidence or outside the core bucket list.",
        "",
    ]
    if df.empty:
        lines.append("_No rows._")
        return "\n".join(lines) + "\n"

    summary = df.groupby("taxonomy_review_status").size().reset_index(name="count")
    lines.extend(["## Summary", "", summary.to_markdown(index=False), ""])

    view_cols = [
        "stock_id",
        "stock_name",
        "industry",
        "category",
        "decision_priority",
        "risk_handling_bucket",
        "effective_primary_theme",
        "effective_structural_theme_bucket",
        "effective_confidence",
    ]
    for status, title, limit in [
        ("needs_market_theme_mapping", "Needs Market Theme Mapping", 120),
        ("industry_core_needs_market_theme", "Industry Core But Market Theme Missing", 120),
        ("core_ai_related_theme", "Core AI-Related Theme", 120),
        ("industry_non_mainstream_only", "Industry Non-Mainstream Only", 80),
        ("non_mainstream_theme", "Non-Mainstream Theme", 80),
        ("mapped_needs_review", "Mapped But Needs Review", 80),
    ]:
        part = df[df["taxonomy_review_status"].eq(status)]
        lines.extend(["", f"## {title}", ""])
        if part.empty:
            lines.append("_No rows._")
        else:
            lines.append(part[view_cols].head(limit).to_markdown(index=False))
    return "\n".join(lines) + "\n"


def main() -> int:
    df = build_review()
    write_csv(df, REVIEW_CSV)
    write_csv(df, DOCS_REVIEW_CSV)
    md = build_markdown(df)
    REVIEW_MD.write_text(md, encoding="utf-8")
    DOCS_REVIEW_MD.write_text(md, encoding="utf-8")
    print(f"Saved: {REVIEW_CSV} rows={len(df)}")
    print(f"Saved: {REVIEW_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
