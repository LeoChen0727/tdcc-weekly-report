"""Opt-in, same-model horizon extension; immutable v1 signals, never promotion evidence."""
from __future__ import annotations

import bisect
import csv
import gzip
import io
import json
import statistics
from array import array
from collections import Counter
from contextlib import contextmanager
from decimal import Decimal, localcontext
from pathlib import Path

import build_tdcc_stealth_accumulation_current_version_annual_replay as base

CONTRACT_FILE = "config/tdcc_stealth_accumulation_current_version_horizon_extension_v1.json"
CONTRACT_SHA256 = "92b3ecd136ac2d70ffcdf575a836f4a5a68767bbbe6fbfb351cf5c158f24abdc"
BASE_REF = "d2f3ccfaf95562b5179f433af0b4b41d62bfee17"
PREFIX = "tdcc_stealth_accumulation_current_version_horizon_extension_"
VERSION = PREFIX + "v1"
DIRECTORY = base.DIRECTORY
PROFILES = {"full_period": [30, 40, 60], "common_d60": [5, 10, 20, 30, 40, 60]}
HORIZONS = [5, 10, 20, 30, 40, 60]
KINDS = ("source_manifest", "trades", "blocked", "summary", "anomalies", "paired_summary", "report")
NAMES = {kind: PREFIX + kind + "_v1." + (
    "json" if kind == "source_manifest" else "md" if kind == "report" else
    "csv.gz" if kind in {"trades", "blocked"} else "csv") for kind in KINDS}
GENERATED = frozenset(NAMES.values())
SCHEMAS = {
    "trades": ["profile"] + base.CSV_FIELDS["trades"] + ["entry_index", "exit_target_index"],
    "blocked": ["profile"] + base.CSV_FIELDS["blocked"] + ["entry_index", "exit_target_index"],
    "summary": ["profile", "signal_cutoff"] + base.CSV_FIELDS["summary"],
    "anomalies": ["profile"] + base.CSV_FIELDS["anomalies"],
    "paired_summary": "profile,horizon,slippage_bps,event_count,eventset_sha256,common_signal_count,excluded_missing_entry_or_exit_events,anomaly_candidate_events,possible_TDR_events,win_count,neutral_count,failure_count,mean_net_return_pct,median_net_return_pct,win_rate_pct,neutral_rate_pct,failure_rate_pct,high_return_ge10_rate_pct,loss_le_minus10_rate_pct,min_net_return_pct,max_net_return_pct,reference_horizon,mean_paired_delta_vs_D20_pct,median_paired_delta_vs_D20_pct,paired_delta_positive_count,paired_delta_zero_count,paired_delta_negative_count,primary_row_retained,overlapping_events_allowed,portfolio_performance,formal_use,promotion_evidence_allowed,caveat".split(","),
}
FALSE_FLAGS = ("formal_use", "promotion_evidence_allowed", "input_availability_proven",
               "full_period_pit_complete", "calendar_complete_coverage_verified",
               "corporate_action_complete_coverage_verified", "ordinary_stock_universe_certified",
               "private_raw_publication_allowed")


def validate_extension_contract(contract):
    base.require(base.sha(base.json_bytes(contract)) == CONTRACT_SHA256,
                 "Frozen horizon extension contract changed")
    base.require(contract["base_artifact_ref"] == BASE_REF and contract["profiles"] == PROFILES,
                 "Frozen base ref or horizon profiles changed")
    base.require(all(contract.get(field) is False for field in FALSE_FLAGS),
                 "Research-only extension flags must remain false")


def load_base(source, contract):
    """Pin the complete signal population, not an already locked v1 trade ledger."""
    ref = contract["base_artifact_ref"]
    original = json.loads(source.blob(ref, base.CONTRACT_FILE))
    base.validate_contract(original)
    manifest_path = DIRECTORY + "/" + base.NAMES["source_manifest"]
    manifest = json.loads(source.blob(ref, manifest_path))
    base.require(manifest["contract"] == original
                 and manifest["contract_sha256"] == base.CONTRACT_SHA256,
                 "Immutable base manifest/contract mismatch")
    base.require(all(manifest.get(k) is False for k in
                     ("formal_use", "promotion_evidence_allowed", "full_period_pit_complete")),
                 "Base manifest research flags changed")
    blobs = {}
    for kind in ("signals", "anomalies"):
        name = base.NAMES[kind]
        data = source.blob(ref, DIRECTORY + "/" + name)
        base.require(manifest["hashes"][name] == dict(bytes=len(data), sha256=base.sha(data)),
                     "Immutable base artifact digest mismatch: " + kind)
        blobs[kind] = data
    # Bind the published-only validator's exact, sole recovered-day evidence.
    name = base.NAMES["features"]
    data = source.blob(ref, DIRECTORY + "/" + name)
    base.require(manifest["hashes"][name] == dict(bytes=len(data), sha256=base.sha(data)),
                 "Immutable base features digest mismatch")
    signals, keys = [], set()
    with io.TextIOWrapper(gzip.GzipFile(fileobj=io.BytesIO(blobs["signals"])), encoding="utf-8", newline="") as stream:
      for row in csv.DictReader(stream):
        base.require(row["selected"] == "True" and row["feature_supported"] == "True"
                     and row["formal_use"] == "False" and row["promotion_evidence_allowed"] == "False"
                     and row["input_availability_proven"] == "False"
                     and row["input_ref"] == original["price_source_ref"], "Base signal contract mismatch")
        key = (row["signal_date"], row["stock_id"])
        base.require(key not in keys, "Duplicate base signal identity")
        keys.add(key)
        signals.append({k:row[k] for k in ("signal_date", "stock_id", "stock_name", "market",
                                          "input_ref", "receipt_id", "history_gap_count")})
    base.require(len(signals) == manifest["counts"]["signals"], "Base signal count mismatch")
    return original, manifest, signals, base.records(blobs["anomalies"])


def session_calendar(original, payloads, source):
    closures = set()
    for item in original["external_files"]:
        if item["kind"] == "calendar":
            closures.update(r["date"] for r in base.records(payloads[item["path"]])
                            if r["scheduled_closed"] == "True")
    for path in ("config/twse_non_trading_days.csv", "data/market_calendar/exceptional_non_trading_days.csv"):
        closures.update(r["date"] for r in base.records(source.blob(original["price_source_ref"], path)))
    calendar = [d for d, w in base.date_range(original["history_start"], original["calendar_end"])
                if w < 5 and d not in closures]
    return calendar, sorted(closures)


def target_dates(calendar, signal_date, horizon, as_of):
    entry_index = bisect.bisect_right(calendar, signal_date)
    target_index = entry_index + horizon
    asof_index = bisect.bisect_right(calendar, as_of) - 1
    mature = target_index <= asof_index
    return dict(entry_index=entry_index, exit_target_index=target_index,
                entry_date=calendar[entry_index] if entry_index < len(calendar) else "",
                exit_date=calendar[target_index] if target_index < len(calendar) else "",
                mature=mature)


def select_profiles(signals, calendar, original):
    eligible_dates = [d for d in calendar if original["requested_signal_start"] <= d <= original["requested_signal_end"]
                      and target_dates(calendar, d, 60, original["as_of"])["mature"]]
    cutoff = max(eligible_dates, default="")
    return {"full_period": list(signals),
            "common_d60": [s for s in signals if cutoff and s["signal_date"] <= cutoff]}, cutoff


def replay_positions(signals, prices, calendar, original, profiles=PROFILES, blocked_sink=None):
    """One fresh lock per profile/horizon; dates are exchange-session indices."""
    groups, cutoff = select_profiles(signals, calendar, original)
    trades, blocked = [], []
    block_counts = Counter()
    def emit_block(row):
        block_counts[row["profile"], row["horizon"], row["record_type"], row["reasons"]] += 1
        if blocked_sink is None:
            blocked.append(row)
        else:
            blocked_sink(row)
    for profile, horizons in profiles.items():
        for horizon in horizons:
            held = {}
            for signal in sorted(groups[profile], key=lambda r: (r["signal_date"], r["stock_id"])):
                sd, sid = signal["signal_date"], signal["stock_id"]
                target = target_dates(calendar, sd, horizon, original["as_of"])
                mature = target.pop("mature")
                ed, xd = target["entry_date"], target["exit_date"]
                er = prices.get(ed, {}).get(sid)
                xr = prices.get(xd, {}).get(sid)
                if not ed or ed > original["as_of"]:
                    strict, strict_reason = "blocked_entry_after_as_of", "entry_after_as_of"
                elif not er or not base.valid_price(er):
                    strict, strict_reason = "blocked_entry_price", "entry_price_missing_or_invalid"
                else:
                    strict, strict_reason = "blocked_input_availability_unproven", "current_acquired_historical_versions_not_event_time_receipts"
                common = dict(profile=profile, signal_date=sd, stock_id=sid, horizon=horizon,
                              strict_v3_status=strict, **target)
                emit_block(dict(common, record_type="strict_ledger_decision", reasons=strict_reason,
                    entry_open=er["open"] if er else "", strict_entry_established=False,
                    strict_prior_position_locked=False, proxy_result_must_not_release_strict_lock=True))
                reason = ""
                if sid in held and sd <= held[sid]:
                    reason = "blocked_exit_day" if sd == held[sid] else "blocked_active_position"
                if not reason and (not ed or ed > original["as_of"]):
                    reason = "entry_after_as_of"
                if not reason and (not er or not base.valid_price(er)):
                    reason = "entry_price_missing_or_invalid"
                if reason:
                    emit_block(dict(common, record_type="operation_no_entry", reasons=reason))
                    continue
                held[sid] = xd if mature and xr and base.valid_price(xr) else "99999999"
                if not mature or not xr or not base.valid_price(xr):
                    emit_block(dict(common, record_type="operation_censored", entry_open=er["open"],
                                        reasons="open_immature" if not mature else "open_unresolved_exit_price"))
                    continue
                for slip in (0, 10, 20):
                    trades.append(dict(common, trade_id=f"{profile}:{sd}:{sid}:D{horizon}:S{slip}",
                        stock_name=signal["stock_name"], market=signal["market"], slippage_bps=slip,
                        **base.cost_cashflows(er["open"], xr["close"], slip),
                        simulation_status="realized_raw_price_proxy", strict_missing_evidence="corporate_action_complete_coverage;calendar_event_full_audit",
                        ca_cashflow_assumption="not_applied_not_asserted_absent", total_return_verified=False,
                        input_ref=signal["input_ref"], receipt_id=signal["receipt_id"], outcome_ref=original["price_source_ref"],
                        entry_source_path=er["source_path"], entry_source_sha256=er["source_sha256"],
                        exit_source_path=xr["source_path"], exit_source_sha256=xr["source_sha256"],
                        history_gap_count=int(signal["history_gap_count"]), anomaly_candidate=False,
                        primary_row_retained=True, formal_use=False, promotion_evidence_allowed=False))
            group = [float(t["net_return_pct"]) for t in trades
                     if t["profile"] == profile and t["horizon"] == horizon and t["slippage_bps"] == 10]
            print(json.dumps(dict(progress="horizon_raw_primary", profile=profile, horizon=horizon,
                                  positions=len(group), **return_stats(group)), ensure_ascii=False), flush=True)
    return trades, blocked if blocked_sink is None else block_counts, groups, cutoff


def apply_anomalies(trades, retained, profiles=PROFILES):
    """Keep every old unresolved candidate; distribution only adds candidates."""
    anomalies, keys = [], set()
    current = {(t["profile"], t["signal_date"], t["stock_id"], t["horizon"]) for t in trades}
    for profile in profiles:
        for row in retained:
            key = (profile, row["signal_date"], row["stock_id"], int(row["horizon"]))
            if key in keys or key not in current:
                continue
            keys.add(key)
            anomalies.append(dict(profile=profile, signal_date=key[1], stock_id=key[2], horizon=key[3],
                net_return_pct=row["net_return_pct"], reason="previously_observed_candidate_retained_not_reclassified_by_larger_sample",
                disposition="unresolved_anomaly_candidate", primary_row_retained=True,
                exclusion_allowed_only_as_sensitivity=True, entry_date=row["entry_date"], exit_date=row["exit_date"]))
        for horizon in profiles[profile]:
            group = [t for t in trades if t["profile"] == profile and t["horizon"] == horizon and t["slippage_bps"] == 10]
            values = sorted(float(t["net_return_pct"]) for t in group)
            if len(values) < 4:
                continue
            q1, _, q3 = statistics.quantiles(values, n=4, method="inclusive")
            for row in group:
                value = float(row["net_return_pct"])
                key = (profile, row["signal_date"], row["stock_id"], horizon)
                if key in keys or q1 - 3 * (q3-q1) <= value <= q3 + 3 * (q3-q1):
                    continue
                keys.add(key)
                anomalies.append(dict(profile=profile, signal_date=key[1], stock_id=key[2], horizon=horizon,
                    net_return_pct=row["net_return_pct"], reason="outside_Q1_Q3_plus_3IQR_descriptive_candidate",
                    disposition="unresolved_anomaly_candidate", primary_row_retained=True,
                    exclusion_allowed_only_as_sensitivity=True, entry_date=row["entry_date"], exit_date=row["exit_date"]))
    for row in trades:
        row["anomaly_candidate"] = (row["profile"], row["signal_date"], row["stock_id"], row["horizon"]) in keys
    for row in anomalies:
        row["represented_in_current_proxy_trade"] = (row["profile"], row["signal_date"], row["stock_id"], row["horizon"]) in current
    return anomalies


def return_stats(values):
    n = len(values)
    return dict(win_count=sum(x > 0 for x in values), neutral_count=sum(x == 0 for x in values),
        failure_count=sum(x < 0 for x in values), mean_net_return_pct=statistics.mean(values) if n else "",
        median_net_return_pct=statistics.median(values) if n else "", win_rate_pct=sum(x>0 for x in values)/n*100 if n else "",
        neutral_rate_pct=sum(x==0 for x in values)/n*100 if n else "", failure_rate_pct=sum(x<0 for x in values)/n*100 if n else "",
        high_return_ge10_rate_pct=sum(x>=10 for x in values)/n*100 if n else "",
        loss_le_minus10_rate_pct=sum(x<=-10 for x in values)/n*100 if n else "",
        min_net_return_pct=min(values) if n else "", max_net_return_pct=max(values) if n else "")


def summarize(trades, blocked, groups, cutoff, original):
    rows = []
    for profile, horizons in PROFILES.items():
        for horizon in horizons:
            if isinstance(blocked, Counter):
                counts = Counter({(kind, reason): count for (p, h, kind, reason), count in blocked.items()
                                  if p == profile and h == horizon})
            else:
                counts = Counter((r["record_type"], r["reasons"]) for r in blocked
                                 if r["profile"] == profile and r["horizon"] == horizon)
            for slip in (0, 10, 20):
                for population in ("primary_including_anomaly_candidates", "sensitivity_excluding_anomaly_candidates"):
                    group = [r for r in trades if r["profile"] == profile and r["horizon"] == horizon and r["slippage_bps"] == slip
                             and (population.startswith("primary") or not r["anomaly_candidate"])]
                    values = [float(r["net_return_pct"]) for r in group]
                    row = dict(profile=profile, signal_cutoff=cutoff if profile == "common_d60" else original["requested_signal_end"],
                        horizon=horizon, slippage_bps=slip, population=population, realized_raw_price_proxy_positions=len(group),
                        total_input_signals=len(groups[profile]), proxy_no_entry_signals=sum(n for (kind, _), n in counts.items() if kind=="operation_no_entry"),
                        proxy_immature_positions=counts["operation_censored", "open_immature"],
                        proxy_unresolved_exit_positions=counts["operation_censored", "open_unresolved_exit_price"],
                        strict_verified_total_return_positions=0, denominator="realized_raw_price_proxy_positions",
                        anomaly_candidate_positions=sum(r["anomaly_candidate"] for r in group),
                        caveat="raw_unadjusted_price_proxy_not_verified_total_return;not_performance_promotion_evidence", **return_stats(values))
                    for label, has_gap in (("gap_present", True), ("gap_absent", False)):
                        subset = [float(r["net_return_pct"]) for r in group if (r["history_gap_count"]>0) == has_gap]
                        row.update({label+"_positions":len(subset), label+"_mean_return_pct":statistics.mean(subset) if subset else "",
                                    label+"_median_return_pct":statistics.median(subset) if subset else "",
                                    label+"_win_rate_pct":sum(x>0 for x in subset)/len(subset)*100 if subset else ""})
                    rows.append(row)
    return rows


def paired_summary(signals, prices, calendar, original, retained=(), anomaly_sink=None):
    """Observational common complete-case events; deliberately no position locks."""
    values = {(h, s): array("d") for h in HORIZONS for s in (0, 10, 20)}
    differences = {(h, s): array("d") for h in HORIZONS for s in (0, 10, 20)}
    keys = []
    for signal in sorted(signals, key=lambda r: (r["signal_date"], r["stock_id"])):
        targets = {h: target_dates(calendar, signal["signal_date"], h, original["as_of"]) for h in HORIZONS}
        ed = targets[20]["entry_date"]
        er = prices.get(ed, {}).get(signal["stock_id"])
        exits = {h: prices.get(targets[h]["exit_date"], {}).get(signal["stock_id"]) for h in HORIZONS}
        if not er or not base.valid_price(er) or not all(targets[h]["mature"] and exits[h] and base.valid_price(exits[h]) for h in HORIZONS):
            continue
        keys.append([signal["signal_date"], signal["stock_id"], ed])
        for slip in (0, 10, 20):
            returns = {h: base.cost_cashflows(er["open"], exits[h]["close"], slip)["net_return_pct"] for h in HORIZONS}
            for horizon in HORIZONS:
                values[horizon, slip].append(float(returns[horizon]))
                with localcontext() as context:
                    context.prec = 50
                    differences[horizon, slip].append(float(Decimal(returns[horizon])-Decimal(returns[20])))
        if len(keys) % 25000 == 0:
            print(f"paired complete-case events processed: {len(keys)}", flush=True)
    digest = base.sha(base.json_bytes(keys))
    old_keys = {(r["signal_date"], r["stock_id"], int(r["horizon"])) for r in retained}
    candidate_counts = Counter()
    for horizon in HORIZONS:
        vals = values[horizon, 10]
        bounds = None
        if len(vals) >= 4:
            q1, _, q3 = statistics.quantiles(vals, n=4, method="inclusive")
            bounds = (q1-3*(q3-q1), q3+3*(q3-q1))
        for event, value in zip(keys, vals):
            sd, sid, ed = event
            old = (sd, sid, horizon) in old_keys
            if not old and (bounds is None or bounds[0] <= value <= bounds[1]):
                continue
            candidate_counts[horizon] += 1
            if anomaly_sink is not None:
                anomaly_sink(dict(profile="paired_common_d60", signal_date=sd, stock_id=sid, horizon=horizon,
                    net_return_pct=value, reason="previously_observed_candidate_retained_not_reclassified_by_larger_sample" if old else "outside_Q1_Q3_plus_3IQR_descriptive_candidate",
                    disposition="unresolved_anomaly_candidate", primary_row_retained=True,
                    exclusion_allowed_only_as_sensitivity=True, entry_date=ed,
                    exit_date=target_dates(calendar, sd, horizon, original["as_of"])["exit_date"],
                    represented_in_current_proxy_trade=False))
    rows = []
    for horizon in HORIZONS:
        for slip in (0, 10, 20):
            delta = differences[horizon, slip]
            rows.append(dict(profile="paired_common_d60", horizon=horizon, slippage_bps=slip,
                event_count=len(keys), eventset_sha256=digest, common_signal_count=len(signals),
                excluded_missing_entry_or_exit_events=len(signals)-len(keys), anomaly_candidate_events=candidate_counts[horizon],
                possible_TDR_events=sum(sid.startswith("91") for _, sid, _ in keys), **return_stats(values[horizon, slip]),
                reference_horizon=20, mean_paired_delta_vs_D20_pct=statistics.mean(delta) if delta else "",
                median_paired_delta_vs_D20_pct=statistics.median(delta) if delta else "",
                paired_delta_positive_count=sum(x>0 for x in delta), paired_delta_zero_count=sum(x==0 for x in delta),
                paired_delta_negative_count=sum(x<0 for x in delta), primary_row_retained=True, overlapping_events_allowed=True,
                portfolio_performance=False, formal_use=False, promotion_evidence_allowed=False,
                caveat="same_complete_case_eventset;observational_selection;overlapping_events_not_portfolio;raw_price_proxy_not_promotion"))
    return rows


def report_bytes(original, groups, cutoff, summary, paired, anomalies, blocked_counts, baseline_candidate_count):
    lines = ["# TDCC 目前版本：D30／D40／D60 有界研究延伸 v1", "",
        "research_only；formal_use=False；promotion_evidence_allowed=False；full_period_pit_complete=False。",
        "不是 strict PIT、正式操作勝率、已核實 total-return 或模型 promotion evidence。",
        f"原始訊號區間 {original['requested_signal_start']}–{original['requested_signal_end']}；as_of={original['as_of']}；D60共同訊號截止={cutoff or '無'}。",
        f"全區間原始訊號 {len(groups['full_period'])}；共同區間原始訊號 {len(groups['common_d60'])}。",
        "來源、selector／features、1000股、雙邊0.001425/min20、sell tax0.003、slippage0/10/20bps完全沿用凍結v1。",
        "D0為訊號後下一session open；D+h為entry_index+h close。各profile/horizon由原始訊號獨立重建非重疊帳本；出場日訊號仍阻擋。",
        "未成熟、缺入場、缺出場與持倉阻擋分列，不算失敗；未成熟且超過既有calendar的exit_date留空並保留target index，不假造未來日曆。",
        "", "## 主要結果（10 bps，保留所有未解候選）", "",
        "| 區間 | D+h | 部位 | 平均淨proxy% | 中位% | proxy正報酬% | 未成熟／缺出場 |",
        "|---|---:|---:|---:|---:|---:|---:|"]
    for r in summary:
        if r["slippage_bps"] == 10 and r["population"].startswith("primary"):
            lines.append(f"| {r['profile']} | {r['horizon']} | {r['realized_raw_price_proxy_positions']} | {r['mean_net_return_pct']} | {r['median_net_return_pct']} | {r['win_rate_pct']} | {r['proxy_immature_positions']}／{r['proxy_unresolved_exit_positions']} |")
    lines += ["", "## 排除候選敏感性對照（10 bps，不取代primary）", "",
              "| 區間 | D+h | sensitivity部位 | 平均淨proxy% | 中位% | proxy正報酬% |",
              "|---|---:|---:|---:|---:|---:|"]
    for r in summary:
        if r["slippage_bps"] == 10 and r["population"].startswith("sensitivity"):
            lines.append(f"| {r['profile']} | {r['horizon']} | {r['realized_raw_price_proxy_positions']} | {r['mean_net_return_pct']} | {r['median_net_return_pct']} | {r['win_rate_pct']} |")
    lines += ["", "## 未入場／未成熟／缺出場原因分布", "",
              "| 區間 | D+h | 類別 | 原因 | 訊號數 |", "|---|---:|---|---|---:|"]
    for (profile, horizon, kind, reason), count in sorted(blocked_counts.items()):
        if kind != "strict_ledger_decision":
            lines.append(f"| {profile} | {horizon} | {kind} | {reason} | {count} |")
    lines += ["", f"immutable v1 baseline候選 {baseline_candidate_count} 列維持原SHA來源；僅新profile實際匹配的同日／同股／同horizon延續旗標，未代表候選不灌入新分母。",
              f"新anomalies共 {len(anomalies)} 列（含paired觀察候選）；old candidates與Q1/Q3±3IQR只觸發調查，全部保留primary；排除版只作sensitivity，不是corrected/cleaned performance。",
              "54組完整成本與primary/sensitivity、勝／平／負、>=10%／<=-10%、極值、缺日分組見summary；不同帳本分母不能合成單一策略績效。",
              "", "## 新帳本數值調查候選（10 bps，每組列出最高與最低）", "",
              "| 區間 | D+h | 訊號日 | 股票 | 淨proxy% | 狀態 |", "|---|---:|---|---|---:|---|"]
    for profile in PROFILES:
        for horizon in PROFILES[profile]:
            candidates = [r for r in anomalies if r["profile"] == profile and r["horizon"] == horizon]
            if candidates:
                chosen = [min(candidates, key=lambda r:float(r["net_return_pct"])), max(candidates, key=lambda r:float(r["net_return_pct"]))]
                for r in chosen if chosen[0] != chosen[1] else chosen[:1]:
                    lines.append(f"| {profile} | {horizon} | {r['signal_date']} | {r['stock_id']} | {r['net_return_pct']} | unresolved_anomaly_candidate；保留primary |")
    lines += [
              "", "## 同事件配對觀察（10 bps）", "",
              "配對採common原始signals，同股同entry且六種horizon都有有效exit的相同事件集。事件可以重疊，屬觀察性complete-case選樣、不是portfolio績效；不影響主帳本。",
              "| D+h | 同事件數 | 平均淨proxy% | 對D20平均差（百分點） | 對D20中位差 |", "|---|---:|---:|---:|---:|"]
    for r in paired:
        if r["slippage_bps"] == 10:
            lines.append(f"| {r['horizon']} | {r['event_count']} | {r['mean_net_return_pct']} | {r['mean_paired_delta_vs_D20_pct']} | {r['median_paired_delta_vs_D20_pct']} |")
    lines += ["", "paired_summary保留全部事件，不依異常幅度刪除；沒有配對sensitivity。18列使用完全相同eventset_sha256。零事件表示資料不足，不阻塞主帳本。",
              f"配對common原始訊號 {paired[0]['common_signal_count']}；六horizon共同有效事件 {paired[0]['event_count']}；缺有效入場／任一出場排除 {paired[0]['excluded_missing_entry_or_exit_events']}；可能91開頭TDR事件 {paired[0]['possible_TDR_events']}。候選數逐horizon列在paired_summary，不轉為錯誤資料判決。",
              "原發布版本可得性、普通股身分、完整休市與公司行動coverage均未認證；strict ledger仍blocked_input_availability_unproven，proxy出場不解除strict鎖。",
              "不調參、不新增選股或風控gate，不使用月營收；EPS、毛利率、營益率、營業利益、業外損益、淨利、季度及年度財報全部排除。",
              "不生成PDF、formal adapter、readiness、approval、Pages或workflow。原v1九檔保持不變。", ""]
    return "\n".join(lines).encode("utf-8")


def gzip_rows(rows, fields):
    sink = io.BytesIO()
    with io.TextIOWrapper(gzip.GzipFile(fileobj=sink, mode="wb", mtime=0), encoding="utf-8", newline="") as text:
        writer = csv.DictWriter(text, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return sink.getvalue()


def build_extension(repository_root, extension_contract, input_root):
    validate_extension_contract(extension_contract)
    source = base.GitSource(Path(repository_root))
    original, manifest, signals, retained = load_base(source, extension_contract)
    print(f"immutable v1 signals verified: signals={len(signals)} retained_candidates={len(retained)}", flush=True)
    payloads = base.external_inputs(Path(input_root), original)
    prices, _, supplemental = base.read_current_prices(source, original, payloads)
    print(f"fixed source prices verified: dates={len(prices)} external_files={len(payloads)}", flush=True)
    calendar, closures = session_calendar(original, payloads, source)
    base.require(closures == manifest["evidence"]["calendar_closures"], "Base calendar dependency changed")
    blocked_buffer = io.BytesIO()
    with io.TextIOWrapper(gzip.GzipFile(fileobj=blocked_buffer, mode="wb", mtime=0), encoding="utf-8", newline="") as text:
        writer = csv.DictWriter(text, fieldnames=SCHEMAS["blocked"], lineterminator="\n")
        writer.writeheader()
        trades, blocked, groups, cutoff = replay_positions(signals, prices, calendar, original, blocked_sink=writer.writerow)
    anomalies = apply_anomalies(trades, retained)
    summary = summarize(trades, blocked, groups, cutoff, original)
    print(f"portfolio ledgers summarized: common_cutoff={cutoff} trade_rows={len(trades)}; paired observation begins", flush=True)
    paired = paired_summary(groups["common_d60"], prices, calendar, original, retained, anomalies.append)
    rows = dict(trades=trades, summary=summary, anomalies=anomalies, paired_summary=paired)
    artifacts = {NAMES["blocked"]: blocked_buffer.getvalue()}
    for kind, records in rows.items():
        artifacts[NAMES[kind]] = gzip_rows(records, SCHEMAS[kind]) if kind == "trades" else base.csv_bytes(records, SCHEMAS[kind])
    artifacts[NAMES["report"]] = report_bytes(original, groups, cutoff, summary, paired, anomalies, blocked, len(retained))
    extension_manifest = dict(model_id=base.MODEL_ID, owner_id=base.OWNER_ID, artifact_version=VERSION,
        contract_file=CONTRACT_FILE, contract=extension_contract, contract_sha256=base.sha(base.json_bytes(extension_contract)),
        base_artifact_ref=BASE_REF, base_contract=original, base_contract_sha256=base.CONTRACT_SHA256,
        sources=sorted(source.sources.values(), key=lambda r: (r["ref"], r["path"])),
        external_sources=[dict(item, bytes=len(payloads[item["path"]])) for item in original["external_files"]],
        calendar=dict(history_start=original["history_start"], calendar_end=original["calendar_end"],
                      closures=closures, sessions=calendar, target_index_basis="zero_based_from_history_start"),
        baseline_anomaly_audit=dict(candidate_rows=len(retained), retained_in_immutable_base=True,
            sha256=manifest["hashes"][base.NAMES["anomalies"]]["sha256"],
            unrepresented_candidates_not_copied_to_extension_profiles=True),
        validation_scope="immutable_v1_signals_and_independent_horizon_source_replay_not_selector_revalidation",
        common_signal_cutoff=cutoff, counts=dict(base_signals=len(signals), common_signals=len(groups["common_d60"]),
            trade_rows=len(trades), blocked_rows=sum(blocked.values()), anomaly_rows=len(anomalies), summary_rows=len(summary),
            paired_summary_rows=len(paired), paired_event_count=paired[0]["event_count"], supplemental=supplemental),
        hashes={name: dict(bytes=len(data), sha256=base.sha(data)) for name, data in artifacts.items()},
        **{flag:False for flag in FALSE_FLAGS})
    artifacts[NAMES["source_manifest"]] = base.json_bytes(extension_manifest)
    base.require(set(artifacts) == GENERATED, "Extension must emit exactly seven artifacts")
    return artifacts


def v1_snapshot(root):
    """Protect v1 physical presence/bytes AND Git mapping, including sparse absence."""
    source = base.GitSource(Path(root))
    tree = source.tree(BASE_REF)
    actual_tree = source._git("ls-tree", "-r", "HEAD", "--", DIRECTORY).decode("utf-8")
    physical = {}
    for name in sorted(base.GENERATED):
        relative = DIRECTORY + "/" + name
        base.require(relative in tree, "Immutable v1 artifact absent")
        path = Path(root) / relative
        base.require(not path.is_symlink(), "v1 artifact symlinks forbidden")
        physical[relative] = base.sha(path.read_bytes()) if path.is_file() else None
    mapping = {line.split("\t")[1]:line.split()[2] for line in actual_tree.splitlines()
               if line.split("\t")[1] in physical}
    return dict(physical=physical, mapping=mapping)


@contextmanager
def preserve_v1(root):
    before = v1_snapshot(root)
    try:
        yield
    finally:
        base.require(v1_snapshot(root) == before, "v1 nine-artifact mapping/physical bytes changed")


def write_extension_outputs(repository_root, artifacts, output_root=None):
    root = Path(repository_root).resolve()
    output = Path(output_root).resolve() if output_root is not None else root / DIRECTORY
    base.require(output == (root / DIRECTORY).resolve(), "Extension output must use registered directory")
    sealed = base.SEALED_ROOT.resolve()
    base.require(output != sealed and sealed not in output.parents, "Sealed retained evidence cannot be output")
    base.require(set(artifacts) == GENERATED and all(isinstance(v, bytes) for v in artifacts.values()), "Extension exact-seven byte allowlist mismatch")
    base.require(not any((output / name).is_symlink() for name in GENERATED), "Extension artifact symlinks forbidden")
    with preserve_v1(root):
        output.mkdir(parents=True, exist_ok=True)
        for name in sorted(GENERATED):
            (output / name).write_bytes(artifacts[name])
