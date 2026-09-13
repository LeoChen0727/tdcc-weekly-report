"""Bounded single-condition, time-split research; no model promotion or source writes."""
from __future__ import annotations

import bisect
import csv
import gzip
import io
import json
import statistics
from collections import Counter
from contextlib import contextmanager
from decimal import Decimal, localcontext
from pathlib import Path

import build_tdcc_stealth_accumulation_current_version_annual_replay as base

CONTRACT_FILE = "config/tdcc_stealth_accumulation_condition_stratification_v1.json"
CONTRACT_SHA256 = "1449b79b9778e7b1ecdf39f874f90e29d970fa1e728ae4427dddfcd0683e191d"
PREFIX = "tdcc_stealth_accumulation_condition_stratification_"
VERSION = PREFIX + "v1"
DIRECTORY = base.DIRECTORY
HORIZON_PREFIX = "tdcc_stealth_accumulation_current_version_horizon_extension_"
VARIANTS = ("baseline", "tdcc_both_net_positive", "tdcc_both_up_count_ge2", "price_5obs_nonnegative",
            "range_20obs_le_training_q75", "no_new_low_previous20obs")
PARTITIONS = ("all", "training", "purged_cross_split", "validation")
FALSE_FLAGS = ("formal_use", "promotion_evidence_allowed", "input_availability_proven", "full_period_pit_complete",
               "calendar_complete_coverage_verified", "corporate_action_complete_coverage_verified",
               "ordinary_stock_universe_certified", "private_raw_publication_allowed")
KINDS = ("source_manifest", "features", "training_contrasts", "candidate_rules", "trades", "blocked", "summary", "anomalies", "report")
NAMES = {k:PREFIX+k+"_v1."+("json" if k in {"source_manifest","candidate_rules"} else "md" if k=="report" else
                          "csv.gz" if k in {"features","trades","blocked"} else "csv") for k in KINDS}
GENERATED = frozenset(NAMES.values())
STATS_FIELDS = "win_count,neutral_count,failure_count,win_rate_pct,neutral_rate_pct,failure_rate_pct,mean_net_return_pct,median_net_return_pct,high_return_ge10_rate_pct,loss_le_minus10_rate_pct,min_net_return_pct,max_net_return_pct".split(",")
DERIVED = "range_20obs_pct,previous_20obs_low_ex_today,current_low,no_new_low_previous20obs,price_state,stratification_feature_supported,stratification_unsupported_reasons".split(",")
SCHEMAS = {
    "features": base.CSV_FIELDS["features"] + DERIVED,
    "trades": ["variant","partition","feature_id"] + base.CSV_FIELDS["trades"] + ["entry_index","exit_target_index"],
    "blocked": ["variant","partition","feature_id"] + base.CSV_FIELDS["blocked"] + ["entry_index","exit_target_index"],
    "training_contrasts": "population,feature_name,outcome_group,samples,valid_samples,missing_samples,mean,median,q25,q75,minimum,maximum".split(","),
    "summary": "variant,horizon,slippage_bps,partition,population,samples,stocks,signal_dates,entry_dates,total_input_signals,condition_passed_signals,unsupported_signals,filter_rejected_signals,overlap_blocked_signals,missing_entry_signals,entry_after_as_of_signals,immature_positions,missing_exit_positions,purged_positions,anomaly_candidate_positions".split(",") + STATS_FIELDS + ["formal_use","promotion_evidence_allowed"],
    "anomalies": ["variant","partition","slippage_bps"] + base.CSV_FIELDS["anomalies"],
}
CONTRAST_FIELDS = ("tdcc_400_change_sum","tdcc_1000_change_sum","tdcc_400_up_weeks","tdcc_1000_up_weeks",
                   "tdcc_both_net_positive","tdcc_both_up_count_ge2","return_5d","return_20d",
                   "range_20obs_pct","no_new_low_previous20obs","history_gap_count",
                   "price_state_falling","price_state_short_rebound_in_decline",
                   "price_state_nonnegative_short_and_medium","price_state_short_pullback")


def decimal(value):
    try:
        result = Decimal(str(value))
        return result if result.is_finite() else None
    except ArithmeticError:
        return None


def quantile_type7(values, probability):
    if not values:
        return None
    with localcontext() as context:
        context.prec = 50
        ordered = sorted(values)
        index = Decimal(len(ordered)-1) * Decimal(str(probability))
        lo = int(index)
        return ordered[lo] + (ordered[min(lo+1,len(ordered)-1)]-ordered[lo])*(index-lo)


def validate_contract(contract):
    base.require(base.sha(base.json_bytes(contract)) == CONTRACT_SHA256, "Frozen stratification contract changed")
    base.require(tuple(r["variant_id"] for r in contract["variants"]) == VARIANTS
                 and contract["horizons"] == [20,60], "Bounded variants/horizons changed")
    base.require(all(contract.get(f) is False for f in FALSE_FLAGS), "Research-only flags must remain false")
    base.require(set(contract["artifact_filenames"]) == GENERATED, "Exact-nine filename contract changed")
    projection=contract["published_warmup_low_projection"]
    base.require(projection["row_count"]==44 and projection["missing_pair_count"]==65,
                 "Frozen warmup projection scope changed")


def prepare_warmup_projection(projection, original):
    """Validate the pre-performance derived reference, never create price inputs."""
    rows=projection["rows"]
    base.require(len(rows)==projection["row_count"] and base.sha(base.json_bytes(rows))==projection["rows_sha256"],
                 "Warmup projection rows/count/digest mismatch")
    sources={r["path"]:r["sha256"] for r in original["external_files"] if r["kind"]=="price_warmup"}
    index={};pairs=set()
    for row in rows:
        key=row["feature_id"];dates=row["observed_dates"];missing=row["missing_observation_dates"]
        base.require(key==row["signal_date"]+":"+row["stock_id"] and key not in index,
                     "Warmup projection duplicate or incorrect identity")
        base.require(len(dates)==21 and dates==sorted(set(dates)) and dates[-1]==row["signal_date"]
                     and base.sha(base.json_bytes(dates))==row["observed_dates_sha256"],
                     "Warmup projection observed dates mismatch")
        base.require(missing and missing==sorted(set(missing)) and set(missing)<=set(dates),
                     "Warmup projection missing-date set invalid")
        refs=row["warmup_sources"]
        base.require(refs and len({r["path"] for r in refs})==len(refs)
                     and all(sources.get(r["path"])==r["sha256"] for r in refs),
                     "Warmup projection original source hash mismatch")
        value=decimal(row["previous_20obs_low_ex_today"])
        base.require(value is not None and value>0,"Warmup projection low invalid")
        pairs.update((d,row["stock_id"]) for d in missing);index[key]=row
    base.require(len(pairs)==projection["missing_pair_count"],"Warmup projection missing-pair count mismatch")
    return dict(index=index,seen=set(),pairs=set(),expected_pairs=pairs)


def verify_raw_warmup_projection(row, prices, audit):
    """Compare independently frozen lows with raw-derived values; no fallback."""
    dates=row["observed_history_dates"].split(";");sid=row["stock_id"];key=row["feature_id"]
    warm=[(d,prices.get(d,{}).get(sid)) for d in dates]
    warm=[(d,p) for d,p in warm if p and p.get("source")=="TPEx_OFFICIAL_MONTHLY_CURRENT_VERSION"]
    if not warm:
        base.require(key not in audit["index"],"Expected warmup projection has no raw warmup observations")
        return
    base.require(key in audit["index"] and key not in audit["seen"],"Unexpected or duplicate raw warmup projection identity")
    expected=audit["index"][key]
    base.require(row["signal_date"]==expected["signal_date"] and sid==expected["stock_id"]
                 and dates==expected["observed_dates"] and [d for d,_ in warm]==expected["missing_observation_dates"],
                 "Raw warmup projection observed-date set mismatch")
    actual_sources={(p["source_path"],p["source_sha256"]) for _,p in warm}
    expected_sources={("external:"+r["path"],r["sha256"]) for r in expected["warmup_sources"]}
    base.require(actual_sources==expected_sources,"Raw warmup projection source hash mismatch")
    base.require(decimal(row["previous_20obs_low_ex_today"])==decimal(expected["previous_20obs_low_ex_today"]),
                 "Raw warmup projection minimum mismatch")
    audit["seen"].add(key);audit["pairs"].update((d,sid) for d,_ in warm)


def finish_warmup_projection(audit):
    base.require(audit["seen"]==set(audit["index"]) and audit["pairs"]==audit["expected_pairs"],
                 "Raw warmup projection exact identity coverage mismatch")
    return dict(raw_verified_rows=len(audit["seen"]),raw_verified_missing_pairs=len(audit["pairs"]),
                projection_used_as_price_fallback=False)


def read_immutable_inputs(source, contract):
    ref = contract["base_artifact_ref"]
    original = json.loads(source.blob(ref, base.CONTRACT_FILE))
    base.validate_contract(original)
    manifest = json.loads(source.blob(ref, DIRECTORY+"/"+base.NAMES["source_manifest"]))
    base.require(manifest["contract"] == original and manifest["contract_sha256"] == base.CONTRACT_SHA256,
                 "Immutable annual manifest contract mismatch")
    data = {}
    for kind in ("signals","features","anomalies"):
        name = base.NAMES[kind]
        data[kind] = source.blob(ref, DIRECTORY+"/"+name)
        base.require(manifest["hashes"][name] == dict(bytes=len(data[kind]),sha256=base.sha(data[kind])), "Immutable annual digest mismatch")
    href = contract["protected_artifact_ref"]
    hcontract = json.loads(source.blob(href, contract["horizon_contract_file"]))
    base.require(base.sha(base.json_bytes(hcontract)) == contract["horizon_contract_sha256"], "Immutable horizon contract mismatch")
    hmanifest = json.loads(source.blob(href,DIRECTORY+"/"+HORIZON_PREFIX+"source_manifest_v1.json"))
    hname = HORIZON_PREFIX+"anomalies_v1.csv"
    hdata = source.blob(href,DIRECTORY+"/"+hname)
    base.require(hmanifest["hashes"][hname] == dict(bytes=len(hdata),sha256=base.sha(hdata)), "Immutable horizon anomalies digest mismatch")
    retained = base.records(data["anomalies"]) + [r for r in base.records(hdata)
                if r["profile"]=="full_period" and int(r["horizon"])==60]
    return original, manifest, data["signals"], retained


def calendar_sessions(original, source, payloads):
    closures = set()
    for item in original["external_files"]:
        if item["kind"] == "calendar":
            closures.update(r["date"] for r in base.records(payloads[item["path"]]) if r["scheduled_closed"] == "True")
    for path in ("config/twse_non_trading_days.csv","data/market_calendar/exceptional_non_trading_days.csv"):
        closures.update(r["date"] for r in base.records(source.blob(original["price_source_ref"],path)))
    return [d for d,w in base.date_range(original["history_start"],original["calendar_end"]) if w<5 and d not in closures], sorted(closures)


def derive_feature(row, prices):
    """Only ex-ante observations; retain every frozen field and every signal."""
    result = dict(row)
    reasons = []
    high, low = decimal(row.get("high_20")), decimal(row.get("low_20"))
    width = None
    if high is not None and low is not None and high >= low > 0:
        with localcontext() as context:
            context.prec = 50
            width = (high/low-1)*100
    else:
        reasons.append("range_frozen_high_low_missing")
    dates = row["observed_history_dates"].split(";")
    previous = current = None
    if len(dates) != 21 or len(set(dates)) != 21 or dates != sorted(dates) or dates[-1] != row["signal_date"]:
        reasons.append("observed_history_dates_invalid")
    else:
        window = [prices.get(d,{}).get(row["stock_id"]) for d in dates]
        if not all(r and base.valid_price(r) for r in window):
            reasons.append("observed_window_price_missing_or_invalid")
        else:
            previous = min(decimal(r["low"]) for r in window[:-1])
            current = decimal(window[-1]["low"])
    r5,r20 = decimal(row.get("return_5d")),decimal(row.get("return_20d"))
    state = "unsupported"
    if r5 is not None and r20 is not None:
        state = ("falling" if r5<0 else "short_rebound_in_decline") if r20<0 else ("short_pullback" if r5<0 else "nonnegative_short_and_medium")
    result.update(range_20obs_pct="" if width is None else str(width),
        previous_20obs_low_ex_today="" if previous is None else str(previous), current_low="" if current is None else str(current),
        no_new_low_previous20obs="" if current is None or previous is None else current>=previous,
        price_state=state,stratification_feature_supported=not reasons,stratification_unsupported_reasons=";".join(reasons))
    return result


def condition(row, variant, threshold):
    if variant == "baseline":
        return True, True
    if variant == "tdcc_both_net_positive":
        a,b=decimal(row.get("tdcc_400_change_sum")),decimal(row.get("tdcc_1000_change_sum"))
        return (a>0 and b>0, True) if a is not None and b is not None else (False,False)
    if variant == "tdcc_both_up_count_ge2":
        a,b=decimal(row.get("tdcc_400_up_weeks")),decimal(row.get("tdcc_1000_up_weeks"))
        return (a>=2 and b>=2,True) if a is not None and b is not None else (False,False)
    if variant == "price_5obs_nonnegative":
        v=decimal(row.get("return_5d"));return (v>=0,True) if v is not None else (False,False)
    if variant == "range_20obs_le_training_q75":
        v=decimal(row.get("range_20obs_pct"));return (v<=threshold,True) if v is not None and threshold is not None else (False,False)
    if variant == "no_new_low_previous20obs":
        a,b=decimal(row.get("current_low")),decimal(row.get("previous_20obs_low_ex_today"))
        return (a>=b,True) if a is not None and b is not None else (False,False)
    raise ValueError("Unregistered single-feature variant")


def target(calendar, sd, horizon, asof, split):
    i=bisect.bisect_right(calendar,sd);j=i+horizon
    ed=calendar[i] if i<len(calendar) else "";xd=calendar[j] if j<len(calendar) else ""
    partition = "validation" if not ed or ed>=split else "training" if xd and xd<split else "purged_cross_split"
    return dict(entry_index=i,exit_target_index=j,entry_date=ed,exit_date=xd,partition=partition), j<=bisect.bisect_right(calendar,asof)-1


def replay_variant(features, prices, calendar, contract, variant, threshold, emit_block):
    trades=[];counts=Counter()
    def emit(row):
        counts[row["partition"],row["horizon"],row["record_type"],row["reasons"]]+=1
        emit_block(row)
    for horizon in (20,60):
        held={}
        for f in features:
            sd,sid=f["signal_date"],f["stock_id"]
            dates,mature=target(calendar,sd,horizon,contract["as_of"],contract["validation_entry_start"])
            common=dict(variant=variant,feature_id=f["feature_id"],signal_date=sd,stock_id=sid,horizon=horizon,**dates)
            passed,supported=condition(f,variant,threshold)
            if not supported or not passed:
                emit(dict(common,record_type="condition_unavailable" if not supported else "condition_rejected",
                          reasons="required_feature_unsupported" if not supported else "single_condition_false",primary_row_retained=True))
                continue
            ed,xd=dates["entry_date"],dates["exit_date"]
            er=prices.get(ed,{}).get(sid);xr=prices.get(xd,{}).get(sid)
            strict="blocked_entry_after_as_of" if not ed or ed>contract["as_of"] else "blocked_entry_price" if not er or not base.valid_price(er) else "blocked_input_availability_unproven"
            emit(dict(common,record_type="strict_ledger_decision",reasons=strict,strict_v3_status=strict,
                      entry_open=er["open"] if er else "",strict_entry_established=False,strict_prior_position_locked=False,
                      proxy_result_must_not_release_strict_lock=True))
            reason=""
            if sid in held and sd<=held[sid]:reason="blocked_exit_day" if sd==held[sid] else "blocked_active_position"
            if not reason and (not ed or ed>contract["as_of"]):reason="entry_after_as_of"
            if not reason and (not er or not base.valid_price(er)):reason="entry_price_missing_or_invalid"
            if reason:
                emit(dict(common,record_type="operation_no_entry",reasons=reason,strict_v3_status=strict));continue
            held[sid]=xd if mature and xr and base.valid_price(xr) else "99999999"
            if not mature or not xr or not base.valid_price(xr):
                emit(dict(common,record_type="operation_censored",reasons="open_immature" if not mature else "open_unresolved_exit_price",entry_open=er["open"],strict_v3_status=strict));continue
            for slip in (0,10,20):
                trades.append(dict(common,trade_id=f"{variant}:{sd}:{sid}:D{horizon}:S{slip}",
                    stock_name=f["stock_name"],market=f["market"],slippage_bps=slip,**base.cost_cashflows(er["open"],xr["close"],slip),
                    simulation_status="realized_raw_price_proxy",strict_v3_status=strict,
                    strict_missing_evidence="corporate_action_complete_coverage;calendar_event_full_audit",
                    ca_cashflow_assumption="not_applied_not_asserted_absent",total_return_verified=False,
                    input_ref=f["input_ref"],receipt_id=f["receipt_id"],outcome_ref=contract["price_source_ref"],
                    entry_source_path=er["source_path"],entry_source_sha256=er["source_sha256"],
                    exit_source_path=xr["source_path"],exit_source_sha256=xr["source_sha256"],
                    history_gap_count=int(f["history_gap_count"]),anomaly_candidate=False,primary_row_retained=True,
                    formal_use=False,promotion_evidence_allowed=False))
    return trades,counts


def training_material(baseline, by_id, contract, retained=()):
    train=[t for t in baseline if t["horizon"]==20 and t["slippage_bps"]==10 and t["partition"]=="training"]
    widths=[decimal(by_id[t["feature_id"]]["range_20obs_pct"]) for t in train]
    widths=[v for v in widths if v is not None]
    threshold=quantile_type7(widths,"0.75")
    old={(r["signal_date"],r["stock_id"],int(r["horizon"])) for r in retained if int(r["horizon"])==20}
    contrasts=[]
    for population in ("primary","immutable_prior_candidate_exclusion_sensitivity"):
      population_rows=[t for t in train if population=="primary" or (t["signal_date"],t["stock_id"],20) not in old]
      for group in ("all_training","high","low","middle"):
        selected=[t for t in population_rows if group=="all_training" or
                  ("high" if decimal(t["net_return_pct"])>=10 else "low" if decimal(t["net_return_pct"])<=-10 else "middle")==group]
        for field in CONTRAST_FIELDS:
            vals=[]
            for t in selected:
                f=by_id[t["feature_id"]]
                if field in ("tdcc_both_net_positive","tdcc_both_up_count_ge2","no_new_low_previous20obs"):
                    passed,supported=condition(f,field,None);v=Decimal(int(passed)) if supported else None
                elif field.startswith("price_state_"):
                    v=None if f["price_state"]=="unsupported" else Decimal(int(f["price_state"]==field[len("price_state_"):]))
                else:v=decimal(f.get(field))
                if v is not None:vals.append(v)
            with localcontext() as context:
                context.prec=50
                contrasts.append(dict(population=population,feature_name=field,outcome_group=group,samples=len(selected),valid_samples=len(vals),missing_samples=len(selected)-len(vals),
                    mean=str(sum(vals)/len(vals)) if vals else "",median=str(quantile_type7(vals,"0.5")) if vals else "",
                    q25=str(quantile_type7(vals,"0.25")) if vals else "",q75=str(quantile_type7(vals,"0.75")) if vals else "",
                    minimum=str(min(vals)) if vals else "",maximum=str(max(vals)) if vals else ""))
    rules=dict(artifact_version=VERSION,training_partition="training",training_horizon=20,training_slippage_bps=10,
        training_positions=len(train),training_stocks=len({t["stock_id"] for t in train}),
        training_signal_dates=len({t["signal_date"] for t in train}),training_width_samples=len(widths),
        threshold_feature="range_20obs_pct",quantile_algorithm="Hyndman-Fan type 7",quantile_probability="0.75",
        training_q75="" if threshold is None else str(threshold),threshold_supported=threshold is not None,
        training_trade_keys_sha256=base.sha(base.json_bytes([t["trade_id"] for t in train])),
        training_widths_sha256=base.sha(base.json_bytes([str(v) for v in widths])),
        training_outcome_group_counts=dict(Counter("high" if decimal(t["net_return_pct"])>=10 else "low" if decimal(t["net_return_pct"])<=-10 else "middle" for t in train)),
        immutable_training_candidate_group_counts=dict(Counter("high" if decimal(t["net_return_pct"])>=10 else "low" if decimal(t["net_return_pct"])<=-10 else "middle"
            for t in train if (t["signal_date"],t["stock_id"],20) in old)),
        variants=contract["variants"],selection_uses_validation=False,selection_uses_anomaly_exclusion=False,
        formal_use=False,promotion_evidence_allowed=False)
    return threshold,contrasts,rules


def mark_anomalies(trades, retained):
    old={(r["signal_date"],r["stock_id"],int(r["horizon"])) for r in retained}
    keys=set();rows=[]
    for horizon in (20,60):
        group=[t for t in trades if t["horizon"]==horizon and t["slippage_bps"]==10]
        vals=[float(t["net_return_pct"]) for t in group]
        limits=None
        if len(vals)>=4:
            q1,_,q3=statistics.quantiles(vals,n=4,method="inclusive");limits=(q1-3*(q3-q1),q3+3*(q3-q1))
        for t in group:
            key=(t["signal_date"],t["stock_id"],horizon);v=float(t["net_return_pct"])
            previous=key in old
            if not previous and (limits is None or limits[0]<=v<=limits[1]):continue
            keys.add(key)
            rows.append(dict(variant=t["variant"],partition=t["partition"],slippage_bps=10,signal_date=key[0],stock_id=key[1],horizon=horizon,
                net_return_pct=t["net_return_pct"],reason="immutable_previous_candidate_retained" if previous else "ledger_Q1_Q3_plus_3IQR_descriptive_candidate",
                disposition="unresolved_anomaly_candidate",primary_row_retained=True,exclusion_allowed_only_as_sensitivity=True,
                entry_date=t["entry_date"],exit_date=t["exit_date"],represented_in_current_proxy_trade=True))
    for t in trades:t["anomaly_candidate"]=(t["signal_date"],t["stock_id"],t["horizon"]) in keys
    return rows


def stats(values):
    n=len(values)
    return dict(win_count=sum(v>0 for v in values),neutral_count=sum(v==0 for v in values),failure_count=sum(v<0 for v in values),
        win_rate_pct=sum(v>0 for v in values)/n*100 if n else "",neutral_rate_pct=sum(v==0 for v in values)/n*100 if n else "",
        failure_rate_pct=sum(v<0 for v in values)/n*100 if n else "",mean_net_return_pct=statistics.mean(values) if n else "",
        median_net_return_pct=statistics.median(values) if n else "",high_return_ge10_rate_pct=sum(v>=10 for v in values)/n*100 if n else "",
        loss_le_minus10_rate_pct=sum(v<=-10 for v in values)/n*100 if n else "",min_net_return_pct=min(values) if n else "",max_net_return_pct=max(values) if n else "")


def summaries(trades,counts,features,calendar,contract,variant,threshold):
    rows=[]
    for h in (20,60):
        input_counts=Counter(target(calendar,f["signal_date"],h,contract["as_of"],contract["validation_entry_start"])[0]["partition"] for f in features)
        for partition in PARTITIONS:
            c=Counter()
            for (p,horizon,kind,reason),n in counts.items():
                if horizon==h and (partition=="all" or p==partition):c[kind,reason]+=n
            count=lambda kind,reason=None:sum(n for (k,r),n in c.items() if k==kind and (reason is None or r==reason))
            for slip in (0,10,20):
                for population in ("primary","sensitivity_excluding_candidates"):
                    group=[t for t in trades if t["horizon"]==h and t["slippage_bps"]==slip and (partition=="all" or t["partition"]==partition)
                           and (population=="primary" or not t["anomaly_candidate"])]
                    rows.append(dict(variant=variant,horizon=h,slippage_bps=slip,partition=partition,population=population,
                        samples=len(group),stocks=len({t["stock_id"] for t in group}),signal_dates=len({t["signal_date"] for t in group}),entry_dates=len({t["entry_date"] for t in group}),
                        total_input_signals=sum(input_counts.values()) if partition=="all" else input_counts[partition],
                        condition_passed_signals=count("strict_ledger_decision"),unsupported_signals=count("condition_unavailable"),filter_rejected_signals=count("condition_rejected"),
                        overlap_blocked_signals=count("operation_no_entry","blocked_active_position")+count("operation_no_entry","blocked_exit_day"),
                        missing_entry_signals=count("operation_no_entry","entry_price_missing_or_invalid"),entry_after_as_of_signals=count("operation_no_entry","entry_after_as_of"),
                        immature_positions=count("operation_censored","open_immature"),missing_exit_positions=count("operation_censored","open_unresolved_exit_price"),
                        purged_positions=sum(t["partition"]=="purged_cross_split" for t in group),anomaly_candidate_positions=sum(t["anomaly_candidate"] for t in group),
                        **stats([float(t["net_return_pct"]) for t in group]),formal_use=False,promotion_evidence_allowed=False))
    return rows


@contextmanager
def gzip_writer(fields):
    sink=io.BytesIO()
    with io.TextIOWrapper(gzip.GzipFile(fileobj=sink,mode="wb",mtime=0),encoding="utf-8",newline="") as stream:
        writer=csv.DictWriter(stream,fieldnames=fields,lineterminator="\n");writer.writeheader()
        yield writer,sink


def report_bytes(contract,rules,summary,anomalies,contrasts):
    lines=["# TDCC 潛伏吸籌：固定單項條件分層研究 v1","",
        "research_only；formal_use=False；promotion_evidence_allowed=False；不是strict PIT、已核實total-return或正式操作勝率。",
        "20260401起為entry-date time-split validation；已看過全年aggregate，不是完全盲測。D20主要、D60僅robustness。",
        f"訓練baseline D20/10bps：{rules['training_positions']}部位、{rules['training_stocks']}股、{rules['training_signal_dates']}訊號日期；寬度有效分母{rules['training_width_samples']}；type7 Q75={rules['training_q75']}。",
        "先baseline訓練對照再凍結Q75，再跑固定五個single filters，不組合、不調參、不依後段結果選優。",
        "training_contrasts的敏感性只採immutable annual D20原候選，與新帳本全期variant/horizon IQR候選分開；所有訓練閾值使用primary全部有效寬度。",
        "窗口是frozen 21個有效觀測；保留history_gap_count，不宣稱連續20交易日。雙增持為各自四批淨增；up是三區間增加次數，不是同週或連續增加。",
        "每variant/horizon完整chronology獨立持倉鎖，切分不重置。D0 next open、Dh entry_index+h close；1000股、雙邊0.001425/min20、sell tax0.003、slippage0/10/20bps。",
        "", "## 固定五個單項條件","",
        "| variant | 單項含義 |","|---|---|",
        "| tdcc_both_net_positive | 400／1000四批各自淨增；不要求同週，兩級距非互斥 |",
        "| tdcc_both_up_count_ge2 | 三區間各至少兩次增加；不要求連續、同週或淨增 |",
        "| price_5obs_nonnegative | 凍結近5有效觀測報酬不負；不宣稱底部確認 |",
        "| range_20obs_le_training_q75 | 寬度不超過訓練primary Q75；不是連續20交易日保證 |",
        "| no_new_low_previous20obs | 今日low不低於前20有效觀測low；不稱底部完成 |",
        "", "## 訓練高／低報酬特徵對照（D20／10 bps）","",
        "高報酬>=10%、低報酬<=-10%，其餘middle；布林mean為成立比例（0至1），width及return5呈中位數%。兩種population只作描述，不以敏感性調整Q75。",
        "| population | feature | statistic | high | low | middle |",
        "|---|---|---|---:|---:|---:|"]
    lookup={(r["population"],r["feature_name"],r["outcome_group"]):r for r in contrasts}
    for population in ("primary","immutable_prior_candidate_exclusion_sensitivity"):
        for field in ("tdcc_both_net_positive","tdcc_both_up_count_ge2","no_new_low_previous20obs","range_20obs_pct","return_5d"):
            statistic="median" if field in {"range_20obs_pct","return_5d"} else "mean"
            values=[lookup[population,field,group][statistic] for group in ("high","low","middle")]
            lines.append(f"| {population} | {field} | {statistic} | {' | '.join(values)} |")
    lines += ["", "## 訓練／驗證主要與敏感性對照（10 bps）","",
        "完整0／10／20bps、all／training／purged／validation的分母與全部rates見同批summary CSV；空值表示無有效分母。",
        "| variant | horizon | partition | population | n | 股票 | 訊號日 | 入場日 | 正/零/負 | 正/零/負率% | 平均% | 中位% | >=10% | <=-10% |",
        "|---|---:|---|---|---:|---:|---:|---:|---|---|---:|---:|---:|---:|"]
    for r in summary:
        if r["slippage_bps"]==10 and r["partition"] in {"training","validation"}:
            lines.append(f"| {r['variant']} | {r['horizon']} | {r['partition']} | {r['population']} | {r['samples']} | {r['stocks']} | {r['signal_dates']} | {r['entry_dates']} | {r['win_count']}/{r['neutral_count']}/{r['failure_count']} | {r['win_rate_pct']}/{r['neutral_rate_pct']}/{r['failure_rate_pct']} | {r['mean_net_return_pct']} | {r['median_net_return_pct']} | {r['high_return_ge10_rate_pct']} | {r['loss_le_minus10_rate_pct']} |")
    lines += ["", "## 缺證、未成熟與重疊（10 bps primary）","",
        "| variant | horizon | partition | unsupported | rejected | overlap | missing entry | immature | missing exit | purged |",
        "|---|---:|---|---:|---:|---:|---:|---:|---:|---:|"]
    for r in summary:
        if r["slippage_bps"]==10 and r["population"]=="primary" and r["partition"]!="all":
            lines.append(f"| {r['variant']} | {r['horizon']} | {r['partition']} | {r['unsupported_signals']} | {r['filter_rejected_signals']} | {r['overlap_blocked_signals']} | {r['missing_entry_signals']} | {r['immature_positions']} | {r['missing_exit_positions']} | {r['purged_positions']} |")
    lines += ["",f"未解數值候選{len(anomalies)}列，全部保留primary。IQR只觸發調查，不是資料錯誤判決；排除候選僅sensitivity，不是corrected/cleaned performance。",
        "訓練閾值未使用全年異常旗標或排除候選分母。purged_cross_split既不屬訓練也不屬validation分母，但持倉鎖仍延續。",
        "未成熟、缺價、unsupported與filter-rejected不算失敗。零分母為空／資料不足。D20與D60分母不同，不把不同樣本差解讀成同筆交易持有期效果。",
        "公開模式對精確44個warmup缺口使用獨立預先凍結的衍生low projection；完整模式從原65份私有來源重建，producer從不消費projection替代raw價格。",
        "不使用月營收；EPS、毛利率、營益率、營業利益、業外損益、淨利、季／年財報均排除。無PDF、正式selector、adapter、readiness、approval或workflow改動。",
        "這些是有限事前假說的描述結果，不自動推薦任何條件進正式模型；若無可重現改善應結論為目前無證據支持改條件。",""]
    return "\n".join(lines).encode("utf-8")


def build_stratification(repository_root,contract,input_root):
    validate_contract(contract)
    source=base.GitSource(Path(repository_root))
    original,manifest,signals_bytes,retained=read_immutable_inputs(source,contract)
    payloads=base.external_inputs(Path(input_root),original)
    external=[dict(item,bytes=len(payloads[item["path"]])) for item in original["external_files"]]
    prices,_,supplemental=base.read_current_prices(source,original,payloads)
    projection_audit=prepare_warmup_projection(contract["published_warmup_low_projection"],original)
    calendar,closures=calendar_sessions(original,source,payloads)
    base.require(closures==manifest["evidence"]["calendar_closures"],"Frozen calendar changed")
    del payloads
    features=[];seen=set()
    keep=("feature_id","signal_date","stock_id","stock_name","market","input_ref","receipt_id","history_gap_count",
          "tdcc_400_change_sum","tdcc_1000_change_sum","tdcc_400_up_weeks","tdcc_1000_up_weeks","return_5d","return_20d",*DERIVED)
    with gzip_writer(SCHEMAS["features"]) as (writer,features_buffer):
        with io.TextIOWrapper(gzip.GzipFile(fileobj=io.BytesIO(signals_bytes)),encoding="utf-8",newline="") as stream:
            for row in csv.DictReader(stream):
                base.require(row["selected"]=="True" and row["feature_supported"]=="True" and row["formal_use"]=="False"
                             and row["promotion_evidence_allowed"]=="False", "Frozen signal flags changed")
                base.require(row["feature_id"] not in seen,"Duplicate frozen signal");seen.add(row["feature_id"])
                derived=derive_feature(row,prices)
                verify_raw_warmup_projection(derived,prices,projection_audit)
                writer.writerow(derived)
                features.append({k:derived[k] for k in keep})
    base.require(len(features)==manifest["counts"]["signals"],"Frozen signal count mismatch")
    projection_result=finish_warmup_projection(projection_audit)
    features.sort(key=lambda r:(r["signal_date"],r["stock_id"]))
    by_id={r["feature_id"]:r for r in features}
    print(f"stratification immutable signals/features verified: {len(features)}",flush=True)
    all_summary=[];all_anomalies=[];trade_count=blocked_count=0
    with gzip_writer(SCHEMAS["blocked"]) as (blocked_writer,blocked_buffer), gzip_writer(SCHEMAS["trades"]) as (trade_writer,trades_buffer):
        baseline,counts=replay_variant(features,prices,calendar,contract,"baseline",None,blocked_writer.writerow)
        threshold,contrasts,rules=training_material(baseline,by_id,contract,retained)
        print(json.dumps(dict(progress="training_rules_frozen",**rules),ensure_ascii=False),flush=True)
        for variant in VARIANTS:
            if variant=="baseline":trades=baseline
            else:trades,counts=replay_variant(features,prices,calendar,contract,variant,threshold,blocked_writer.writerow)
            anomalies=mark_anomalies(trades,retained);all_anomalies.extend(anomalies)
            summary=summaries(trades,counts,features,calendar,contract,variant,threshold);all_summary.extend(summary)
            trade_writer.writerows(trades);trade_count+=len(trades);blocked_count+=sum(counts.values())
            print(json.dumps(dict(progress="variant_finished",variant=variant,trade_rows=len(trades),blocked_rows=sum(counts.values())),ensure_ascii=False),flush=True)
    artifacts={NAMES["features"]:features_buffer.getvalue(),NAMES["trades"]:trades_buffer.getvalue(),NAMES["blocked"]:blocked_buffer.getvalue(),
        NAMES["training_contrasts"]:base.csv_bytes(contrasts,SCHEMAS["training_contrasts"]),NAMES["candidate_rules"]:base.json_bytes(rules),
        NAMES["summary"]:base.csv_bytes(all_summary,SCHEMAS["summary"]),NAMES["anomalies"]:base.csv_bytes(all_anomalies,SCHEMAS["anomalies"]),
        NAMES["report"]:report_bytes(contract,rules,all_summary,all_anomalies,contrasts)}
    artifacts[NAMES["source_manifest"]]=base.json_bytes(dict(model_id=base.MODEL_ID,owner_id=base.OWNER_ID,artifact_version=VERSION,
        contract_file=CONTRACT_FILE,contract=contract,contract_sha256=base.sha(base.json_bytes(contract)),base_contract=original,
        sources=sorted(source.sources.values(),key=lambda r:(r["ref"],r["path"])),external_sources=external,
        calendar=dict(sessions=calendar,closures=closures,history_start=original["history_start"],calendar_end=original["calendar_end"]),
        warmup_projection_audit=projection_result,
        candidate_rules=rules,counts=dict(signals=len(features),trades=trade_count,blocked=blocked_count,summary=len(all_summary),anomalies=len(all_anomalies),
            training_contrasts=len(contrasts),baseline_candidate_source_rows=len(retained),supplemental=supplemental),
        hashes={n:dict(bytes=len(v),sha256=base.sha(v)) for n,v in artifacts.items()},**{f:False for f in FALSE_FLAGS}))
    base.require(set(artifacts)==GENERATED,"Stratification exact-nine artifacts mismatch")
    return artifacts


def frozen_snapshot(root):
    source=base.GitSource(Path(root));ref="129b8669ef17cb1a678dd71b87097cbbff084c82"
    paths=[DIRECTORY+"/"+name for name in base.GENERATED]
    paths += [DIRECTORY+"/"+HORIZON_PREFIX+k+"_v1."+("json" if k=="source_manifest" else "md" if k=="report" else "csv.gz" if k in {"trades","blocked"} else "csv")
              for k in ("source_manifest","trades","blocked","summary","anomalies","paired_summary","report")]
    paths += [base.CONTRACT_FILE,"config/tdcc_stealth_accumulation_current_version_horizon_extension_v1.json"]
    before=source.tree(ref)
    current=source._git("ls-tree","-r","HEAD","--",*paths).decode().splitlines()
    mapping={line.split("\t")[1]:line.split()[2] for line in current}
    physical={}
    for rel in paths:
        base.require(rel in before,"Protected earlier version absent")
        path=Path(root)/rel;base.require(not path.is_symlink(),"Protected symlink forbidden")
        physical[rel]=base.sha(path.read_bytes()) if path.is_file() else None
    return dict(mapping=mapping,physical=physical)


@contextmanager
def preserve_previous_versions(root):
    before=frozen_snapshot(root)
    try:yield
    finally:base.require(frozen_snapshot(root)==before,"Annual9/horizon7 or old contracts changed")


def write_outputs(root,artifacts,output_root=None):
    root=Path(root).resolve();output=Path(output_root).resolve() if output_root else root/DIRECTORY
    base.require(output==(root/DIRECTORY).resolve(),"Exact registered output directory required")
    sealed=base.SEALED_ROOT.resolve();base.require(output!=sealed and sealed not in output.parents,"Sealed output forbidden")
    base.require(set(artifacts)==GENERATED and all(isinstance(v,bytes) for v in artifacts.values()),"Exact-nine byte allowlist required")
    base.require(not any((output/n).is_symlink() for n in GENERATED),"Artifact symlink forbidden")
    with preserve_previous_versions(root):
        output.mkdir(parents=True,exist_ok=True)
        for name in sorted(GENERATED):(output/name).write_bytes(artifacts[name])
