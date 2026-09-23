"""One model-owned, frozen-method medium-term TDCC research entrypoint.

Current-version sources and raw-price cashflows are not PIT/promotion evidence.
Published weekly values are relative offsets, never paid absolute holding ratios.
"""
from __future__ import annotations

import argparse
import bisect
import csv
import gzip
import io
import json
import math
import re
import statistics
import subprocess
from collections import Counter, defaultdict
from contextlib import contextmanager, nullcontext
from datetime import datetime, timedelta
from decimal import Decimal, localcontext
from pathlib import Path

import build_tdcc_stealth_accumulation_current_version_annual_replay as annual
from model_research_artifact_guard import load_ownership_rules, load_protected_sentinels, model_owned_artifact_guard, validate_changed_paths

ROOT=Path(__file__).resolve().parents[1]
MODEL_ID="tdcc_stealth_accumulation"
OWNER_ID="tdcc_stealth_accumulation_medium_term_trend_research"
PRODUCER="scripts/build_tdcc_stealth_accumulation_medium_term_trend_research.py"
PREFIX=OWNER_ID+"_"
VERSION=PREFIX+"v1"
DIRECTORY=annual.DIRECTORY
CONTRACT_FILE="config/"+PREFIX+"v1.json"
CONTRACT_SHA256="fa38bab5d57e4b8a21984e568ce94eff8bcbdc4d69cbb45ed4fa24da29b63be6"
SOURCE_REF="847d774ca80f354253e4680e32bc1a46584e35c0"
BASE_REF="d2f3ccfaf95562b5179f433af0b4b41d62bfee17"
PRICE_REF="07d992bbd9afa283355d8828a294da4524efb56d"
STRATEGIES=("baseline_4","trend_8","trend_12")
PROFILES={"full_available":STRATEGIES,"common_8":STRATEGIES[:2],"common_12":STRATEGIES}
PARTITIONS=("all","training","purged_cross_split","validation")
FALSE_FLAGS=("formal_use","promotion_evidence_allowed","input_availability_proven","full_period_pit_complete",
             "calendar_complete_coverage_verified","corporate_action_complete_coverage_verified",
             "ordinary_stock_universe_certified","private_raw_publication_allowed")
LEVELS=("400,001-600,000","600,001-800,000","800,001-1,000,000","more than 1,000,001")
KINDS=("source_manifest","coverage","weekly_features","features","signals","trades","blocked","summary","feature_contrasts","anomalies","report")
GZIP_KINDS={"weekly_features","features","signals","trades","blocked"}
NAMES={k:PREFIX+k+"_v1."+("json" if k=="source_manifest" else "md" if k=="report" else "csv.gz" if k in GZIP_KINDS else "csv") for k in KINDS}
GENERATED=frozenset(NAMES.values())
WINDOW_FIELDS="supported,reasons,dates,span_days,missing_open_weeks,missing_batch_dates,net400_pp,net1000_pp,slope400_pp_per_week,slope1000_pp_per_week,numerator400,numerator1000,last400_pp,last1000_pp,max_positive_share400,max_positive_share1000,descriptive_missing_reasons,selected".split(",")
EXTRA_FIELDS="price_supported,price_unsupported_reasons,price_qualified,price_rejection_reasons,baseline_4_supported,baseline_4_selected".split(",")+[f"w{n}_{k}" for n in (8,12) for k in WINDOW_FIELDS]
METRICS="win_count,neutral_count,failure_count,win_rate_pct,neutral_rate_pct,failure_rate_pct,mean_net_return_pct,median_net_return_pct,high_return_ge10_rate_pct,loss_le_minus10_rate_pct,min_net_return_pct,max_net_return_pct".split(",")
SCHEMAS={
 "weekly_features":"stock_id,batch_date,source_path,source_sha256,complete,unsupported_reasons,anchor_date,offset400_pp,offset1000_pp,formal_use,promotion_evidence_allowed".split(","),
 "features":annual.CSV_FIELDS["features"]+EXTRA_FIELDS,
 "signals":["profile","strategy","feature_id","signal_date","stock_id","stock_name","market","history_gap_count","formal_use","promotion_evidence_allowed"],
 "coverage":"signal_date,raw_universe_rows,price_supported_rows,price_qualified_rows,baseline_4_supported_rows,baseline_4_signals,trend_8_supported_rows,trend_8_signals,trend_12_supported_rows,trend_12_signals,common_8_eligible_rows,common_12_eligible_rows,price_unsupported_reason_counts,trend_8_unsupported_reason_counts,trend_12_unsupported_reason_counts,possible_tdr_rows,formal_use,promotion_evidence_allowed".split(","),
 "trades":["profile","strategy","partition","feature_id"]+annual.CSV_FIELDS["trades"]+["entry_index","exit_target_index"],
 "blocked":["profile","strategy","partition","feature_id"]+annual.CSV_FIELDS["blocked"]+["entry_index","exit_target_index"],
 "summary":"profile,strategy,horizon,slippage_bps,partition,population,samples,stocks,signal_dates,entry_dates,price_qualified_rows,cohort_eligible_rows,strategy_supported_rows,selected_signals,unsupported_rows,cohort_ineligible_rows,rejected_rows,overlap_blocked_signals,missing_entry_signals,entry_after_as_of_signals,immature_positions,missing_exit_positions,purged_positions,anomaly_candidate_positions".split(",")+METRICS+["formal_use","promotion_evidence_allowed"],
 "feature_contrasts":"profile,strategy,horizon,slippage_bps,partition,population,feature_name,outcome_group,samples,valid_samples,missing_samples,mean,median,q25,q75,minimum,maximum".split(","),
 "anomalies":["profile","strategy","partition","slippage_bps"]+annual.CSV_FIELDS["anomalies"]+["detector_profile","detector_strategy","q1","q3","lower_fence","upper_fence"],
}
CONTRAST_FIELDS=("tdcc_400_change_sum","tdcc_1000_change_sum","tdcc_400_up_weeks","tdcc_1000_up_weeks",
                 "return_5d","return_20d","volume_ratio","history_gap_count")+tuple(
                 f"w{n}_{field}" for n in (8,12) for field in ("slope400_pp_per_week","slope1000_pp_per_week","net400_pp","net1000_pp","last400_pp","last1000_pp","max_positive_share400","max_positive_share1000","span_days"))


def decimal(value):
    try:
        v=Decimal(str(value).replace(",","").strip())
        return v if v.is_finite() else None
    except ArithmeticError:
        return None


def wire(value):
    return "" if value is None else str(value)


def validate_contract(contract):
    annual.require(annual.sha(annual.json_bytes(contract))==CONTRACT_SHA256,"Frozen medium-term contract changed")
    annual.require(contract["model_id"]==MODEL_ID and contract["owner_id"]==OWNER_ID,"Medium-term owner mismatch")
    annual.require(all(contract.get(k) is False for k in FALSE_FLAGS),"Research-only flags must remain false")
    annual.require(contract["price_source_ref"]==PRICE_REF and contract["base_artifact_ref"]==BASE_REF,"Frozen source refs changed")
    annual.require({PREFIX+k for k in contract["artifact_kinds"]}==GENERATED,"Exact eleven filenames required")


def load_tdcc_exact(original,payloads):
    """Retain exact vendor percentage decimals; never publish absolute ratios."""
    weeks={};total=0
    for item in original["external_files"]:
        if item["kind"]!="tdcc":continue
        stock_bins=defaultdict(dict);count=0
        for row in csv.DictReader(io.StringIO(payloads[item["path"]].decode("utf-8-sig"),newline="")):
            count+=1
            annual.require(row["日期"].replace("-","")==item["date"],"TDCC effective date mismatch")
            sid=row["股票代碼"].strip();level=row["持股分級"].strip()
            annual.require(level not in stock_bins[sid],"Duplicate stock/week/bin")
            stock_bins[sid][level]=decimal(row["比例"])
        annual.require(count==item["rows"],"TDCC raw row count mismatch");total+=count
        annual.require(item["date"] not in weeks,"Duplicate TDCC batch date")
        batch={}
        for sid,bins in stock_bins.items():
            if not re.fullmatch(r"[1-9][0-9]{3}",sid):continue
            with localcontext() as context:
                context.prec=50
                p400=sum((bins[x] for x in LEVELS),Decimal(0)) if all(bins.get(x) is not None for x in LEVELS) else None
            batch[sid]=dict(p400=p400,p1000=bins.get(LEVELS[-1]),path=item["path"],sha256=item["sha256"])
        weeks[item["date"]]=batch
    annual.require(len(weeks)==original["expected_tdcc_weeks"] and total==original["expected_tdcc_rows"],"TDCC exact batch scope mismatch")
    return weeks


def weekly_feature_rows(weeks):
    anchors={}
    for date in sorted(weeks):
        for sid,r in sorted(weeks[date].items()):
            complete=r["p400"] is not None and r["p1000"] is not None
            if complete and sid not in anchors:anchors[sid]=(date,r["p400"],r["p1000"])
            anchor=anchors.get(sid)
            with localcontext() as context:
                context.prec=50
                yield dict(stock_id=sid,batch_date=date,source_path=r["path"],source_sha256=r["sha256"],complete=complete,
                    unsupported_reasons="" if complete else "required_holding_bin_missing",anchor_date=anchor[0] if anchor else "",
                    offset400_pp=str(r["p400"]-anchor[1]) if complete else "",offset1000_pp=str(r["p1000"]-anchor[2]) if complete else "",
                    formal_use=False,promotion_evidence_allowed=False)


def monday(date):
    d=datetime.strptime(date,"%Y%m%d")
    return (d-timedelta(days=d.weekday())).strftime("%Y%m%d")


def missing_open_weeks(dates,calendar,signal_date):
    if not dates:return []
    covered={monday(d) for d in dates}
    opening={monday(d) for d in calendar if dates[0]<=d<signal_date
             and (datetime.strptime(monday(d),"%Y%m%d")+timedelta(days=6)).strftime("%Y%m%d")<signal_date}
    return sorted(opening-covered)


def exact_trend(dates,values):
    """Integer day spacing; exact Decimal numerator controls direction."""
    with localcontext() as context:
        context.prec=50
        origin=datetime.strptime(dates[0],"%Y%m%d")
        days=[(datetime.strptime(d,"%Y%m%d")-origin).days for d in dates]
        n=Decimal(len(days));sx=sum(days);den=n*sum(d*d for d in days)-sx*sx
        annual.require(den>0,"OLS requires distinct dates")
        numerator=n*sum((Decimal(d)*v for d,v in zip(days,values)),Decimal(0))-Decimal(sx)*sum(values,Decimal(0))
        diffs=[b-a for a,b in zip(values,values[1:])];positive=[d for d in diffs if d>0]
        return dict(numerator=numerator,slope=Decimal(7)*numerator/den,net=values[-1]-values[0],last=diffs[-1],
                    max_positive_share=max(positive)/sum(positive) if positive else None)


def window_context(weeks,date,n,calendar,calendar_start,calendar_end):
    dates=sorted(d for d in weeks if d<=date)[-n:]
    return dates,missing_open_weeks(dates,calendar,date),bool(dates and dates[0]>=calendar_start and date<=calendar_end)


def window_metrics(weeks,date,sid,n,calendar,calendar_start,calendar_end,prepared=None):
    dates,gaps,calendar_known=prepared or window_context(weeks,date,n,calendar,calendar_start,calendar_end)
    missing=[d for d in dates if sid not in weeks[d] or weeks[d][sid]["p400"] is None or weeks[d][sid]["p1000"] is None]
    reasons=[]
    if len(dates)!=n:reasons.append("insufficient_market_batches")
    if missing:reasons.append("stock_batch_or_ratio_missing")
    if gaps:reasons.append("missing_open_week_batch")
    if not calendar_known:reasons.append("calendar_evidence_insufficient")
    result={field:"" for field in WINDOW_FIELDS}
    result.update(supported=not reasons,reasons=";".join(reasons),dates=";".join(dates),
                  span_days=(datetime.strptime(dates[-1],"%Y%m%d")-datetime.strptime(dates[0],"%Y%m%d")).days if dates else "",
                  missing_open_weeks=";".join(gaps),missing_batch_dates=";".join(missing),selected=False)
    if not reasons:
        for bucket in (400,1000):
            trend=exact_trend(dates,[weeks[d][sid]["p"+str(bucket)] for d in dates])
            result.update({f"net{bucket}_pp":wire(trend["net"]),f"slope{bucket}_pp_per_week":wire(trend["slope"]),
                           f"numerator{bucket}":wire(trend["numerator"]),f"last{bucket}_pp":wire(trend["last"]),
                           f"max_positive_share{bucket}":wire(trend["max_positive_share"])})
        result["descriptive_missing_reasons"]=";".join(f"no_positive_change_{b}" for b in (400,1000) if result[f"max_positive_share{b}"]=="")
        result["selected"]=decimal(result["numerator400"])>0 and decimal(result["numerator1000"])>0
    return result


def baseline_four(weeks,date,sid,classify):
    dates=sorted(d for d in weeks if d<=date)[-4:]
    rows=[weeks[d][sid] for d in dates if sid in weeks[d]]
    supported=len(rows)==4 and all(r["p400"] is not None and r["p1000"] is not None for r in rows)
    if not supported:return dict(supported=False,dates=[d for d in dates if sid in weeks[d]],paths=[weeks[d][sid]["path"] for d in dates if sid in weeks[d]])
    # Preserve the old baseline's numeric interface; new trends never use it.
    p400=[float(r["p400"]) for r in rows];p1000=[float(r["p1000"]) for r in rows]
    a=p400[-1]-p400[0];b=p1000[-1]-p1000[0]
    u=sum(y>x for x,y in zip(p400,p400[1:]));v=sum(y>x for x,y in zip(p1000,p1000[1:]))
    enum,description=classify(4,a,b,u,v)
    return dict(supported=True,dates=dates,paths=[r["path"] for r in rows],enum=enum,description=description,
                delta400=round(a,4),delta1000=round(b,4),up400=u,up1000=v,
                selected=enum in {"strong_accumulation","mild_accumulation"})


def price_qualifier(row):
    value=lambda k:float(row[k]) if row.get(k)!="" else float("nan")
    close,op,hi,lo,prev=(value(k) for k in ("close","open","high","low","previous_close"))
    vol,ma,level=(value(k) for k in ("volume_ratio","volume_ma20_lots","previous_20d_high_ex_today"))
    bullish=close>op or (close==op and close>prev)
    normal=close>=level*1.02 and vol>=2 and ma>=1000 and bullish
    tight=hi==lo or (prev>0 and (hi-lo)/prev*100<=1)
    locked=close>=level*1.02 and value("daily_return_calc")>=9 and close>=hi*.995 and op>=close*.995 and tight
    flags=dict(attack_already_started=normal or locked,volume_below_2_5=math.isnan(vol) or vol<2.5,
        short_not_attacked=math.isnan(value("return_5d")) or value("return_5d")<8,not_rallied=math.isnan(value("return_20d")) or value("return_20d")<20,
        in_recent_range_10pct=value("high_20")>value("low_20") and value("low_20")*.9<=close<=value("high_20")*1.1)
    failed=["attack_already_started"] if flags["attack_already_started"] else []
    failed += [k for k in ("volume_below_2_5","short_not_attacked","not_rallied","in_recent_range_10pct") if not flags[k]]
    return not failed,failed,flags["attack_already_started"]


def derive_price_row(date,sid,r,history,calendar,closures,original,baseline):
    hs=history[-21:];reasons=[]
    if not annual.valid_price(r):reasons.append("signal_ohlc_invalid_or_conflicting")
    if len(hs)<21:reasons.append("insufficient_21_observations")
    if not all(annual.valid_price(x) for x in hs):reasons.append("history_ohlc_invalid_or_conflicting")
    if any(x["volume"] is None or x["volume"]<0 for x in hs[-20:]):reasons.append("volume_missing_or_negative")
    if any(x["source"]=="TPEX_OLD_DAILY_JSON" for x in hs[-20:]):reasons.append("raw_volume_lineage_unresolved")
    row={k:"" for k in annual.CSV_FIELDS["features"]}
    row.update(stock_id=sid,stock_name=r["stock_name"],market=r["market"],signal_date=date,tdcc_price_phase="",tdcc_status="",volume_confirmed_breakout=False,
               **{k:wire(r[k]) for k in ("open","high","low","close")})
    derived={}
    if len(hs)==21 and all(annual.valid_price(x) for x in hs):
        derived.update(return_5d=(r["close"]/hs[-6]["close"]-1)*100,return_20d=(r["close"]/hs[-21]["close"]-1)*100,
            daily_return_calc=(r["close"]/hs[-2]["close"]-1)*100,previous_close=hs[-2]["close"],high_20=max(x["high"] for x in hs[-20:]),
            low_20=min(x["low"] for x in hs[-20:]),previous_20d_high_ex_today=max(x["high"] for x in hs[-21:-1]))
        if all(x["volume"] is not None and x["volume"]>=0 for x in hs[-20:]):
            avg=statistics.mean(x["volume"] for x in hs[-20:])
            if avg>0:derived.update(volume_ma20=avg,volume_ma20_lots=avg/1000,volume_ratio=r["volume"]/avg)
            else:reasons.append("volume_mean_zero")
    row.update({k:format(round(v,4),".4f") for k,v in derived.items()})
    qualified,failed,attack=price_qualifier(row)
    old_reasons=list(reasons)
    if not baseline["supported"]:old_reasons.append("tdcc_four_batch_coverage_missing")
    if baseline["supported"]:
        row.update(tdcc_accumulation_signal=baseline["enum"],tdcc_accumulation_description=baseline["description"],
            tdcc_400_change_sum=baseline["delta400"],tdcc_1000_change_sum=baseline["delta1000"],tdcc_400_up_weeks=baseline["up400"],tdcc_1000_up_weeks=baseline["up1000"])
    missing_dates=[d for d in calendar if hs and hs[0]["date"]<=d<=date and d not in {x["date"] for x in hs}]
    global_dates=sorted(d for d in original["_batch_paths"] if d<=date)[-4:]
    row.update(feature_id=date+":"+sid,input_ref=original["price_source_ref"],receipt_id="",available_no_later_than="",entry_cutoff="",
        universe_source_path=r["source_path"],universe_source_sha256=r["source_sha256"],observed_history_dates=";".join(x["date"] for x in hs),history_observations=len(hs),
        history_missing_session_dates=";".join(missing_dates),history_gap_count=len(missing_dates),historical_closed_date_files_excluded=";".join(d for d in closures if d<=date),
        tdcc_window_dates=";".join(baseline["dates"]),tdcc_paths=";".join(original["_batch_paths"][d] for d in global_dates),
        phase_policy="phase_classifier_not_invoked",instrument_note="possible_TDR_91_prefix" if sid.startswith("91") else "four_digit_nonzero_equity_code",
        input_availability_proven=False,feature_supported=not old_reasons,unsupported_reasons=";".join(old_reasons),
        raw_selector_selected=qualified and baseline.get("selected",False),selected=not old_reasons and qualified and baseline.get("selected",False),
        positive_resolution="recognized_enum_positive_fallback" if baseline.get("selected") else "recognized_enum_nonpositive_fail_closed" if baseline["supported"] else "missing_positive_evidence_fail_closed",
        attack_already_started=attack,primary_row_retained=True,formal_use=False,promotion_evidence_allowed=False,
        price_supported=not reasons,price_unsupported_reasons=";".join(reasons),price_qualified=not reasons and qualified,price_rejection_reasons=";".join(failed),
        baseline_4_supported=baseline["supported"],baseline_4_selected=baseline.get("selected",False))
    return row


def cohort_decision(feature,profile,strategy):
    if not feature["price_qualified"]:return False,False,False
    common=0 if profile=="full_available" else 8 if profile=="common_8" else 12
    eligible=not common or bool(feature[f"w{common}_supported"])
    supported=bool(feature["baseline_4_supported"] if strategy=="baseline_4" else feature[f"w{strategy[-1] if strategy=='trend_8' else '12'}_supported"])
    selected=bool(feature["baseline_4_selected"] if strategy=="baseline_4" else feature[f"w{strategy[-1] if strategy=='trend_8' else '12'}_selected"])
    return eligible,supported,eligible and supported and selected


def operation_dates(calendar,signal,horizon,as_of,split):
    i=bisect.bisect_right(calendar,signal);j=i+horizon
    entry=calendar[i] if i<len(calendar) else "";exit_date=calendar[j] if j<len(calendar) else ""
    partition="validation" if not entry or entry>=split else "training" if exit_date and exit_date<split else "purged_cross_split"
    return dict(entry_date=entry,exit_date=exit_date,entry_index=i,exit_target_index=j,partition=partition),j<bisect.bisect_right(calendar,as_of)


def replay_positions(features,prices,calendar,contract,profile,strategy,emit_block=None):
    trades=[];counts=Counter()
    def emit(row):
        counts[row["partition"],row["horizon"],row["record_type"],row["reasons"]]+=1
        if emit_block:emit_block(row)
    for horizon in (20,60):
        held={}
        for feature in features:
            sd,sid=feature["signal_date"],feature["stock_id"]
            dates,mature=operation_dates(calendar,sd,horizon,contract["as_of"],contract["split_date"])
            common=dict(profile=profile,strategy=strategy,feature_id=feature["feature_id"],signal_date=sd,stock_id=sid,horizon=horizon,**dates)
            eligible,supported,selected=cohort_decision(feature,profile,strategy)
            if not eligible or not supported or not selected:
                reason="cohort_data_ineligible" if not eligible else "strategy_feature_unsupported" if not supported else "strategy_rule_false"
                emit(dict(common,record_type="qualification_decision",reasons=reason,primary_row_retained=True));continue
            ed,xd=dates["entry_date"],dates["exit_date"]
            er=prices.get(ed,{}).get(sid)
            strict="blocked_entry_after_as_of" if not ed or ed>contract["as_of"] else "blocked_entry_price" if not er or not annual.valid_price(er) else "blocked_input_availability_unproven"
            emit(dict(common,record_type="strict_ledger_decision",reasons=strict,strict_v3_status=strict,
                entry_open=er["open"] if er else "",strict_entry_established=False,strict_prior_position_locked=False,proxy_result_must_not_release_strict_lock=True))
            reason=""
            if sid in held and sd<=held[sid]:reason="blocked_exit_day" if sd==held[sid] else "blocked_active_position"
            if not reason and (not ed or ed>contract["as_of"]):reason="entry_after_as_of"
            if not reason and (not er or not annual.valid_price(er)):reason="entry_price_missing_or_invalid"
            if reason:
                emit(dict(common,record_type="operation_no_entry",reasons=reason,strict_v3_status=strict));continue
            xr=prices.get(xd,{}).get(sid) if mature else None
            held[sid]=xd if mature and xr and annual.valid_price(xr) else "99999999"
            if not mature or not xr or not annual.valid_price(xr):
                emit(dict(common,record_type="operation_censored",reasons="open_immature" if not mature else "open_unresolved_exit_price",entry_open=er["open"],strict_v3_status=strict));continue
            for slip in (0,10,20):
                trades.append(dict(common,trade_id=f"{profile}:{strategy}:{sd}:{sid}:D{horizon}:S{slip}",stock_name=feature["stock_name"],market=feature["market"],
                    slippage_bps=slip,**annual.cost_cashflows(er["open"],xr["close"],slip),simulation_status="realized_raw_price_proxy",strict_v3_status=strict,
                    strict_missing_evidence="corporate_action_complete_coverage;calendar_event_full_audit",ca_cashflow_assumption="not_applied_not_asserted_absent",total_return_verified=False,
                    input_ref=PRICE_REF,receipt_id="",outcome_ref=PRICE_REF,entry_source_path=er["source_path"],entry_source_sha256=er["source_sha256"],
                    exit_source_path=xr["source_path"],exit_source_sha256=xr["source_sha256"],history_gap_count=feature["history_gap_count"],
                    anomaly_candidate=False,primary_row_retained=True,formal_use=False,promotion_evidence_allowed=False))
    return trades,counts


def anomaly_key(row):
    return row["signal_date"],row["stock_id"],int(row["horizon"])


def detect_candidates(trades):
    detections=[]
    for h in (20,60):
        group=[r for r in trades if r["horizon"]==h and r["slippage_bps"]==10]
        if len(group)<4:continue
        q1,_,q3=statistics.quantiles([float(r["net_return_pct"]) for r in group],n=4,method="inclusive")
        lo=q1-3*(q3-q1);hi=q3+3*(q3-q1)
        for row in group:
            if lo<=float(row["net_return_pct"])<=hi:continue
            detections.append(dict(signal_date=row["signal_date"],stock_id=row["stock_id"],horizon=h,
                detector_profile=row["profile"],detector_strategy=row["strategy"],q1=q1,q3=q3,lower_fence=lo,upper_fence=hi))
    return detections


def annotate_candidates(trades,prior_keys,detections):
    keys=prior_keys|set(detections);rows=[]
    for t in trades:
        key=anomaly_key(t);t["anomaly_candidate"]=key in keys
        if key not in keys or t["slippage_bps"]!=10:continue
        provenance=detections.get(key,[])
        if key in prior_keys:provenance=[dict(detector_profile="immutable_prior",detector_strategy="",q1="",q3="",lower_fence="",upper_fence="")]+provenance
        for p in provenance:
            rows.append(dict(profile=t["profile"],strategy=t["strategy"],partition=t["partition"],slippage_bps=10,
                signal_date=t["signal_date"],stock_id=t["stock_id"],horizon=t["horizon"],net_return_pct=t["net_return_pct"],
                reason="immutable_previous_candidate_retained" if p["detector_profile"]=="immutable_prior" else "full_ledger_Q1_Q3_plus_3IQR_candidate_union",
                disposition="unresolved_anomaly_candidate",primary_row_retained=True,exclusion_allowed_only_as_sensitivity=True,
                entry_date=t["entry_date"],exit_date=t["exit_date"],represented_in_current_proxy_trade=True,
                **{k:p[k] for k in ("detector_profile","detector_strategy","q1","q3","lower_fence","upper_fence")}))
    return rows


def statistics_row(values):
    n=len(values);wins=sum(v>0 for v in values);zeros=sum(v==0 for v in values);losses=sum(v<0 for v in values)
    return dict(win_count=wins,neutral_count=zeros,failure_count=losses,win_rate_pct=wins/n*100 if n else "",
        neutral_rate_pct=zeros/n*100 if n else "",failure_rate_pct=losses/n*100 if n else "",mean_net_return_pct=statistics.mean(values) if n else "",
        median_net_return_pct=statistics.median(values) if n else "",high_return_ge10_rate_pct=sum(v>=10 for v in values)/n*100 if n else "",
        loss_le_minus10_rate_pct=sum(v<=-10 for v in values)/n*100 if n else "",min_net_return_pct=min(values) if n else "",max_net_return_pct=max(values) if n else "")


def summarize(trades,counts,features,calendar,contract,profile,strategy):
    summary=[]
    for h in (20,60):
        population_counts=Counter()
        for f in features:
            part=operation_dates(calendar,f["signal_date"],h,contract["as_of"],contract["split_date"])[0]["partition"]
            eligible,supported,selected=cohort_decision(f,profile,strategy)
            for partition in ("all",part):
                population_counts[partition,"price"]+=1
                population_counts[partition,"eligible"]+=eligible
                population_counts[partition,"supported"]+=eligible and supported
        for partition in PARTITIONS:
            c=Counter()
            for (p,horizon,kind,reason),n in counts.items():
                if horizon==h and (partition=="all" or partition==p):c[kind,reason]+=n
            count=lambda kind,reason=None:sum(n for (k,r),n in c.items() if k==kind and (reason is None or r==reason))
            for slip in (0,10,20):
                for population in ("primary","sensitivity_excluding_candidates"):
                    selected=[t for t in trades if t["horizon"]==h and t["slippage_bps"]==slip and (partition=="all" or t["partition"]==partition)
                              and (population=="primary" or not t["anomaly_candidate"])]
                    summary.append(dict(profile=profile,strategy=strategy,horizon=h,slippage_bps=slip,partition=partition,population=population,
                        samples=len(selected),stocks=len({t["stock_id"] for t in selected}),signal_dates=len({t["signal_date"] for t in selected}),entry_dates=len({t["entry_date"] for t in selected}),
                        price_qualified_rows=population_counts[partition,"price"],cohort_eligible_rows=population_counts[partition,"eligible"],strategy_supported_rows=population_counts[partition,"supported"],
                        selected_signals=count("strict_ledger_decision"),unsupported_rows=count("qualification_decision","strategy_feature_unsupported"),
                        cohort_ineligible_rows=count("qualification_decision","cohort_data_ineligible"),rejected_rows=count("qualification_decision","strategy_rule_false"),
                        overlap_blocked_signals=count("operation_no_entry","blocked_active_position")+count("operation_no_entry","blocked_exit_day"),
                        missing_entry_signals=count("operation_no_entry","entry_price_missing_or_invalid"),entry_after_as_of_signals=count("operation_no_entry","entry_after_as_of"),
                        immature_positions=count("operation_censored","open_immature"),missing_exit_positions=count("operation_censored","open_unresolved_exit_price"),
                        purged_positions=sum(t["partition"]=="purged_cross_split" for t in selected),anomaly_candidate_positions=sum(t["anomaly_candidate"] for t in selected),
                        **statistics_row([float(t["net_return_pct"]) for t in selected]),formal_use=False,promotion_evidence_allowed=False))
    return summary


def quantile(values,q):
    if not values:return None
    with localcontext() as context:
        context.prec=50;ordered=sorted(values);x=Decimal(len(values)-1)*Decimal(q);i=int(x)
        return ordered[i]+(ordered[min(i+1,len(ordered)-1)]-ordered[i])*(x-i)


def feature_contrasts(trades,by_id,prior_keys,profile,strategy):
    rows=[]
    for horizon in (20,60):
      for slip in (0,10,20):
       for partition in PARTITIONS:
        selected=[t for t in trades if t["horizon"]==horizon and t["slippage_bps"]==slip and (partition=="all" or t["partition"]==partition)]
        for population in ("primary","immutable_prior_candidate_exclusion_sensitivity"):
         subset=[t for t in selected if population=="primary" or anomaly_key(t) not in prior_keys]
         for group in ("all_realized","high","low","middle"):
          members=[t for t in subset if group=="all_realized" or ("high" if decimal(t["net_return_pct"])>=10 else "low" if decimal(t["net_return_pct"])<=-10 else "middle")==group]
          for field in CONTRAST_FIELDS:
            values=[decimal(by_id[t["feature_id"]].get(field)) for t in members];values=[v for v in values if v is not None]
            with localcontext() as context:
                context.prec=50
                rows.append(dict(profile=profile,strategy=strategy,horizon=horizon,slippage_bps=slip,partition=partition,population=population,feature_name=field,outcome_group=group,
                    samples=len(members),valid_samples=len(values),missing_samples=len(members)-len(values),mean=str(sum(values)/len(values)) if values else "",
                    median=wire(quantile(values,"0.5")),q25=wire(quantile(values,"0.25")),q75=wire(quantile(values,"0.75")),minimum=str(min(values)) if values else "",maximum=str(max(values)) if values else ""))
    return rows


@contextmanager
def gzip_writer(fields):
    sink=io.BytesIO()
    with io.TextIOWrapper(gzip.GzipFile(fileobj=sink,mode="wb",mtime=0),encoding="utf-8",newline="") as stream:
        writer=csv.DictWriter(stream,fieldnames=fields,lineterminator="\n");writer.writeheader()
        yield writer,sink


def read_control(source,original,contract):
    manifest=json.loads(source.blob(BASE_REF,DIRECTORY+"/"+annual.NAMES["source_manifest"]))
    annual.require(manifest["contract"]==original and manifest["contract_sha256"]==annual.CONTRACT_SHA256,"Annual control contract mismatch")
    data={}
    for kind in ("features","signals"):
        name=annual.NAMES[kind];payload=source.blob(BASE_REF,DIRECTORY+"/"+name)
        annual.require(manifest["hashes"][name]==dict(bytes=len(payload),sha256=annual.sha(payload)),"Annual control bytes mismatch")
        data[kind]=payload
    return manifest,data


def calendar_inputs(source,original,payloads):
    closures=set()
    for item in original["external_files"]:
        if item["kind"]=="calendar":closures.update(r["date"] for r in annual.records(payloads[item["path"]]) if r["scheduled_closed"]=="True")
    for path in ("config/twse_non_trading_days.csv","data/market_calendar/exceptional_non_trading_days.csv"):
        closures.update(r["date"] for r in annual.records(source.blob(PRICE_REF,path)))
    calendar=[d for d,w in annual.date_range(original["history_start"],original["calendar_end"]) if w<5 and d not in closures]
    return calendar,sorted(closures)


def read_prior_candidates(source,contract):
    keys=set();evidence=[]
    for item in contract["anomaly_retention_sources"]:
        payload=source.blob(item["ref"],item["path"]);rows=annual.records(payload)
        keys.update(anomaly_key(r) for r in rows)
        evidence.append(dict(**item,sha256=annual.sha(payload),rows=len(rows)))
    return keys,evidence


def report_bytes(contract,coverage,summary,contrasts,counts):
    lines=["# TDCC 潛伏吸籌：中期整體趨勢研究 v1","",
        "advisory-only；formal_use=False；promotion_evidence_allowed=False；不是strict PIT、核實total-return或正式操作勝率。",
        "先前年報、期間延伸及條件分層結果已看過；20260401以entry_date切分的validation不是genuine unseen OOS。",
        "全市場原始歷史價量母體重新建立，不以舊selected signals或混合TDCC缺證的feature_supported作母體。",
        f"原始母體{counts['universe_rows']}列；price-supported {counts['price_supported_rows']}列；price-qualified {counts['price_qualified_rows']}列；可能TDR {counts['possible_tdr_rows']}列。",
        "baseline_4重建原四批float介面及enum fallback；trend_8為主研究、trend_12為穩健性研究，兩級距OLS精確分子皆>0才接受，容許中途下降。",
        "OLS使用實際日差，單位pp/week；不先round、不轉float、不加epsilon。批次不等於完整日曆週；已完整結束開市週無批才unsupported，整週休市可接受、當週未完成不算缺批。",
        "full_available各自可支持期間不同；common_8只比較四／八批、common_12比較四／八／十二批。共同母體是資料資格交集，不是selected訊號交集，各帳本共同起點空倉。",
        "原21個現存觀測價量窗口與四位小數精度保留，history_gap_count揭露但不新增連續交易日gate。",
        "D0下一session open、Dh=entry_index+h的close；每profile/strategy/horizon獨立同股鎖，split不重置。跨split purged不進train或validation績效，仍占鎖。",
        "1000股；買賣各0.001425且各最低20元；賣出稅0.003；slippage0／10／20bps。缺entry、缺exit、未成熟、重疊不算失敗。",
        "", "## 覆蓋與共同資格","",
        "| 項目 | 列數 |","|---|---:|",
        f"| baseline_4可支持 | {sum(r['baseline_4_supported_rows'] for r in coverage)} |",
        f"| trend_8可支持／common_8資格 | {sum(r['trend_8_supported_rows'] for r in coverage)} |",
        f"| trend_12可支持／common_12資格 | {sum(r['trend_12_supported_rows'] for r in coverage)} |"]
    for window in (8,12):
        c=Counter()
        for row in coverage:c.update(json.loads(row[f"trend_{window}_unsupported_reason_counts"]))
        lines += [f"{window}批缺證原因（可重疊）：`{json.dumps(dict(c),ensure_ascii=False,sort_keys=True)}`。"]
    lines += ["", "## 固定高／低報酬特徵對照（10 bps primary）","",
        "high>=10%、low<=-10%、middle介於兩者；negative<0獨立為failure。以下各帳本all已實現主樣本，數值為中位數；完整各成本、partition及不可變既有候選排除敏感度見feature_contrasts CSV。只描述，不據此加gate或選參數。",
        "| profile | strategy | horizon | feature | high | low | middle |","|---|---|---:|---|---:|---:|---:|"]
    lookup={(r['profile'],r['strategy'],r['horizon'],r['slippage_bps'],r['partition'],r['population'],r['feature_name'],r['outcome_group']):r for r in contrasts}
    for profile,strategies in PROFILES.items():
      for strategy in strategies:
       for horizon in (20,60):
        for field in ("w8_slope400_pp_per_week","w8_slope1000_pp_per_week","w12_slope400_pp_per_week","w12_slope1000_pp_per_week","w8_net400_pp","w8_last400_pp","w8_max_positive_share400"):
            values=[lookup[profile,strategy,horizon,10,"all","primary",field,g]["median"] for g in ("high","low","middle")]
            lines.append(f"| {profile} | {strategy} | {horizon} | {field} | {' | '.join(values)} |")
    lines += ["", "## 原始價格proxy主要與敏感性（10 bps）","",
        "| profile | strategy | horizon | partition | population | n | stocks | signal dates | entry dates | 正/零/負 | 正/零/負率% | 平均% | 中位% | >=10% | <=-10% |",
        "|---|---|---:|---|---|---:|---:|---:|---:|---|---|---:|---:|---:|---:|"]
    for r in summary:
        if r["slippage_bps"]==10 and r["partition"] in {"all","training","validation"}:
            lines.append(f"| {r['profile']} | {r['strategy']} | {r['horizon']} | {r['partition']} | {r['population']} | {r['samples']} | {r['stocks']} | {r['signal_dates']} | {r['entry_dates']} | {r['win_count']}/{r['neutral_count']}/{r['failure_count']} | {r['win_rate_pct']}/{r['neutral_rate_pct']}/{r['failure_rate_pct']} | {r['mean_net_return_pct']} | {r['median_net_return_pct']} | {r['high_return_ge10_rate_pct']} | {r['loss_le_minus10_rate_pct']} |")
    lines += ["", "## 未入場、未成熟及purged（10 bps primary）","",
        "| profile | strategy | horizon | partition | unsupported | cohort ineligible | rejected | overlap | missing entry | entry after asof | immature | missing exit | purged |",
        "|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for r in summary:
        if r["slippage_bps"]==10 and r["population"]=="primary":
            lines.append(f"| {r['profile']} | {r['strategy']} | {r['horizon']} | {r['partition']} | {r['unsupported_rows']} | {r['cohort_ineligible_rows']} | {r['rejected_rows']} | {r['overlap_blocked_signals']} | {r['missing_entry_signals']} | {r['entry_after_as_of_signals']} | {r['immature_positions']} | {r['missing_exit_positions']} | {r['purged_positions']} |")
    lines += ["", "## 候選警訊與禁止外推","",
        f"既有候選鍵{counts['prior_candidate_keys']}；新增偵測ledger列{counts['new_candidate_detections']}；本次聯集候選鍵{counts['candidate_union_keys']}。候選全留primary，排除僅sensitivity，不是corrected/cleaned performance。",
        "IQR只觸發調查，不認定資料錯誤；保留每個偵測帳本與fences，跨本次帳本按相同signal_date/stock_id/horizon聯集標記，不跨horizon。",
        "特徵對照的敏感度只排不可變既有候選，不使用新全期IQR旗標作訓練或調參。缺證、未成熟與零分母均不得補0。",
        "weekly_features僅第一個complete batch為anchor的持有比例偏移，不含付費原文absolute p400/p1000。full驗證需讀原65份SHA-bound輸入；published-only不能聲稱重讀私有原文。",
        "兩級距重疊，不能證明同一批大戶持續買進。公司行動、調整基礎、完整calendar與原始發布可得性未核實；current-version proxy不能支持promotion。",
        "月營收、EPS、毛利率、營益率、營業利益、業外損益、淨利與季／年財報全排除；不改正式selector、adapter/readiness、PDF、Apps Script。",
        "不同full_available期間不能稱策略優劣；8與12批的直接比較限common_12。無重現改善時應結論為目前無證據支持改條件。",""]
    return "\n".join(lines).encode("utf-8")


def build(repository_root,contract,input_root):
    validate_contract(contract)
    source=annual.GitSource(Path(repository_root))
    original=json.loads(source.blob(BASE_REF,annual.CONTRACT_FILE));annual.validate_contract(original)
    manifest,control=read_control(source,original,contract)
    prior_keys,prior_evidence=read_prior_candidates(source,contract)
    annual.require(source.tree(original["classifier_ref"]).get("tdcc_trend_utils.py")==original["classifier_blob_oid"],"Classifier blob mismatch")
    classify=annual.pure(source,original["classifier_ref"],"tdcc_trend_utils.py",{"classify_accumulation"},{})["classify_accumulation"]
    payloads=annual.external_inputs(Path(input_root),original)
    external=[dict(r,bytes=len(payloads[r["path"]])) for r in original["external_files"]]
    weeks=load_tdcc_exact(original,payloads)
    prices,price_meta,supplemental=annual.read_current_prices(source,original,payloads)
    calendar,closures=calendar_inputs(source,original,payloads)
    annual.require(closures==manifest["evidence"]["calendar_closures"],"Immutable proxy calendar mismatch")
    del payloads
    source._blobs.clear();source._objects.clear()
    metadata=dict(original,_batch_paths={r["date"]:r["path"] for r in original["external_files"] if r["kind"]=="tdcc"})
    control_stream=io.TextIOWrapper(gzip.GzipFile(fileobj=io.BytesIO(control["features"])),encoding="utf-8",newline="")
    control_rows=csv.DictReader(control_stream)
    signal_stream=io.TextIOWrapper(gzip.GzipFile(fileobj=io.BytesIO(control["signals"])),encoding="utf-8",newline="")
    control_signals=csv.DictReader(signal_stream)
    historical_dates=sorted(d for d in prices if d in set(calendar));cursor=0;history=defaultdict(list)
    excluded_closed_dates=sorted(d for d in prices if d in closures)
    feature_count=baseline_count=weekly_count=0;features=[];coverage=[]
    keep=tuple(dict.fromkeys(("feature_id","signal_date","stock_id","stock_name","market","price_qualified","baseline_4_supported","baseline_4_selected",
                              "w8_supported","w8_selected","w12_supported","w12_selected",*CONTRAST_FIELDS)))
    with gzip_writer(SCHEMAS["weekly_features"]) as (writer,weekly_sink):
        for row in weekly_feature_rows(weeks):writer.writerow(row);weekly_count+=1
    window_cache={};four_cache={};cache_version=None
    with gzip_writer(SCHEMAS["features"]) as (writer,feature_sink):
      for date in (d for d in calendar if contract["requested_signal_start"]<=d<=contract["requested_signal_end"]):
        while cursor<len(historical_dates) and historical_dates[cursor]<=date:
            for sid,r in prices[historical_dates[cursor]].items():history[sid].append(r)
            cursor+=1
        current_dates=tuple(d for d in sorted(weeks) if d<=date)
        version=(current_dates[-1] if current_dates else "",monday(date))
        if version!=cache_version:window_cache.clear();four_cache.clear();cache_version=version
        prepared={n:window_context(weeks,date,n,calendar,original["history_start"],original["calendar_end"]) for n in (8,12)}
        counts=Counter();reason_counts={8:Counter(),12:Counter(),"price":Counter()}
        for sid,r in sorted(prices.get(date,{}).items()):
            if sid not in four_cache:four_cache[sid]=baseline_four(weeks,date,sid,classify)
            row=derive_price_row(date,sid,r,history[sid],calendar,excluded_closed_dates,metadata,four_cache[sid])
            # This assertion verifies reconstruction, never selects its input rows.
            old=next(control_rows,None)
            annual.require(old is not None,"New universe exceeds immutable annual control")
            mismatches=[k for k in annual.CSV_FIELDS["features"] if str(row[k])!=old[k]]
            annual.require(not mismatches,"Annual full-universe reconstruction mismatch "+date+":"+sid+":"+",".join(mismatches))
            if row["selected"]:
                signal=next(control_signals,None)
                annual.require(signal==old,"Independent baseline4 selected-set control mismatch");baseline_count+=1
            for n in (8,12):
                key=(sid,n)
                if key not in window_cache:window_cache[key]=window_metrics(weeks,date,sid,n,calendar,original["history_start"],original["calendar_end"],prepared[n])
                row.update({f"w{n}_{k}":v for k,v in window_cache[key].items()})
            writer.writerow(row);feature_count+=1;counts["raw"]+=1
            counts["price_supported"]+=row["price_supported"];counts["price_qualified"]+=row["price_qualified"];counts["tdr"]+=sid.startswith("91")
            reason_counts["price"].update(filter(None,row["price_unsupported_reasons"].split(";")))
            if row["price_qualified"]:
                features.append({k:row[k] for k in keep})
                counts["baseline_supported"]+=row["baseline_4_supported"];counts["baseline_selected"]+=row["baseline_4_selected"] and row["baseline_4_supported"]
                for n in (8,12):
                    counts[f"supported{n}"]+=row[f"w{n}_supported"];counts[f"selected{n}"]+=row[f"w{n}_selected"]
                    reason_counts[n].update(filter(None,row[f"w{n}_reasons"].split(";")))
        coverage.append(dict(signal_date=date,raw_universe_rows=counts["raw"],price_supported_rows=counts["price_supported"],price_qualified_rows=counts["price_qualified"],
            baseline_4_supported_rows=counts["baseline_supported"],baseline_4_signals=counts["baseline_selected"],trend_8_supported_rows=counts["supported8"],trend_8_signals=counts["selected8"],
            trend_12_supported_rows=counts["supported12"],trend_12_signals=counts["selected12"],common_8_eligible_rows=counts["supported8"],common_12_eligible_rows=counts["supported12"],
            price_unsupported_reason_counts=json.dumps(dict(reason_counts["price"]),sort_keys=True),trend_8_unsupported_reason_counts=json.dumps(dict(reason_counts[8]),sort_keys=True),
            trend_12_unsupported_reason_counts=json.dumps(dict(reason_counts[12]),sort_keys=True),possible_tdr_rows=counts["tdr"],formal_use=False,promotion_evidence_allowed=False))
        if len(coverage)%40==0:print(f"medium-term features through {date}: universe={feature_count} price_qualified={len(features)}",flush=True)
    annual.require(next(control_rows,None) is None and next(control_signals,None) is None,"Annual reconstruction control left unmatched rows")
    control_stream.close();signal_stream.close();del control
    annual.require(feature_count==manifest["counts"]["covered_universe_rows"] and baseline_count==manifest["counts"]["signals"],"Baseline control counts mismatch")
    print(f"medium-term source reconstruction verified: universe={feature_count} baseline4={baseline_count} price_qualified={len(features)}",flush=True)
    by_id={r["feature_id"]:r for r in features};detections=defaultdict(list)
    # Two bounded pure replay passes avoid retaining every ledger in memory while
    # preserving cross-ledger candidate-union semantics in final serialized bytes.
    for profile,strategies in PROFILES.items():
        for strategy in strategies:
            trades,_=replay_positions(features,prices,calendar,contract,profile,strategy)
            found=detect_candidates(trades)
            for r in found:detections[anomaly_key(r)].append(r)
            print(json.dumps(dict(progress="candidate_detection",profile=profile,strategy=strategy,trade_rows=len(trades),detections=len(found))),flush=True)
    del trades
    all_summary=[];all_contrasts=[];all_anomalies=[];trade_count=blocked_count=signal_count=0;represented=set();cohorts={}
    with gzip_writer(SCHEMAS["trades"]) as (trade_writer,trade_sink), gzip_writer(SCHEMAS["blocked"]) as (blocked_writer,blocked_sink), gzip_writer(SCHEMAS["signals"]) as (signal_writer,signal_sink):
      for profile,strategies in PROFILES.items():
       for strategy in strategies:
        eligible_keys=[];selected_count=0
        for f in features:
            eligible,supported,selected=cohort_decision(f,profile,strategy)
            if eligible:eligible_keys.append(f["feature_id"])
            if selected:
                signal_writer.writerow(dict(profile=profile,strategy=strategy,**{k:f[k] for k in ("feature_id","signal_date","stock_id","stock_name","market","history_gap_count")},formal_use=False,promotion_evidence_allowed=False))
                selected_count+=1;signal_count+=1
        cohorts[profile+":"+strategy]=dict(eligible_rows=len(eligible_keys),eligible_keys_sha256=annual.sha(annual.json_bytes(eligible_keys)),
            first_eligible_date=eligible_keys[0].split(":")[0] if eligible_keys else "",selected_signals=selected_count)
        trades,counts=replay_positions(features,prices,calendar,contract,profile,strategy,blocked_writer.writerow)
        all_anomalies.extend(annotate_candidates(trades,prior_keys,detections));represented.update(anomaly_key(t) for t in trades)
        summary=summarize(trades,counts,features,calendar,contract,profile,strategy);all_summary.extend(summary)
        all_contrasts.extend(feature_contrasts(trades,by_id,prior_keys,profile,strategy))
        trade_writer.writerows(trades);trade_count+=len(trades);blocked_count+=sum(counts.values())
        print(json.dumps(dict(progress="ledger_finished",profile=profile,strategy=strategy,summary=[r for r in summary if r["slippage_bps"]==10 and r["partition"]=="all"])),flush=True)
    counts=dict(universe_rows=feature_count,price_supported_rows=sum(r["price_supported_rows"] for r in coverage),price_qualified_rows=len(features),
        baseline_4_control_signals=baseline_count,possible_tdr_rows=sum(r["possible_tdr_rows"] for r in coverage),weekly_features=weekly_count,features=feature_count,
        signals=signal_count,trades=trade_count,blocked=blocked_count,coverage=len(coverage),summary=len(all_summary),feature_contrasts=len(all_contrasts),anomalies=len(all_anomalies),
        prior_candidate_keys=len(prior_keys),prior_candidate_keys_represented=len(prior_keys&represented),prior_candidate_keys_unrepresented=len(prior_keys-represented),
        new_candidate_detections=sum(map(len,detections.values())),candidate_union_keys=len(prior_keys|set(detections)),supplemental=supplemental)
    artifacts={NAMES["weekly_features"]:weekly_sink.getvalue(),NAMES["features"]:feature_sink.getvalue(),NAMES["signals"]:signal_sink.getvalue(),NAMES["trades"]:trade_sink.getvalue(),NAMES["blocked"]:blocked_sink.getvalue(),
        NAMES["coverage"]:annual.csv_bytes(coverage,SCHEMAS["coverage"]),NAMES["summary"]:annual.csv_bytes(all_summary,SCHEMAS["summary"]),
        NAMES["feature_contrasts"]:annual.csv_bytes(all_contrasts,SCHEMAS["feature_contrasts"]),NAMES["anomalies"]:annual.csv_bytes(all_anomalies,SCHEMAS["anomalies"]),
        NAMES["report"]:report_bytes(contract,coverage,all_summary,all_contrasts,counts)}
    artifacts[NAMES["source_manifest"]]=annual.json_bytes(dict(model_id=MODEL_ID,owner_id=OWNER_ID,artifact_version=VERSION,contract=contract,contract_file=CONTRACT_FILE,contract_sha256=CONTRACT_SHA256,
        base_contract=original,sources=sorted(source.sources.values(),key=lambda r:(r["ref"],r["path"])),external_sources=external,prior_candidate_sources=prior_evidence,
        calendar=dict(sessions=calendar,closures=closures,history_start=original["history_start"],calendar_end=original["calendar_end"]),
        baseline_control=dict(ref=BASE_REF,full_universe_rows=feature_count,selected_signals=baseline_count,used_as_universe=False),cohorts=cohorts,counts=counts,
        hashes={k:dict(bytes=len(v),sha256=annual.sha(v)) for k,v in artifacts.items()},**{k:False for k in FALSE_FLAGS}))
    annual.require(set(artifacts)==GENERATED,"Exact eleven outputs required")
    return artifacts


@contextmanager
def artifact_guard(root):
    root=Path(root)
    sparse=subprocess.run(["git","--no-replace-objects","config","--bool","core.sparseCheckout"],cwd=root,check=False,capture_output=True,text=True).stdout.strip()=="true"
    standard_guard=nullcontext() if sparse else model_owned_artifact_guard(
        OWNER_ID,PRODUCER,root=root,
        registry_path=root/"config/model_research_artifact_ownership.csv",
        sentinel_registry_path=root/"config/model_research_protected_sentinels.csv")
    with standard_guard:
        sentinels=load_protected_sentinels(root/"config/model_research_protected_sentinels.csv")
        before=annual.protected_snapshot(root,sentinels);dirty=annual.dirty_hashes(root)
        try:yield
        finally:
            after=annual.protected_snapshot(root,sentinels);current=annual.dirty_hashes(root)
            annual.require(before==after,"Protected source/artifact mapping or physical bytes changed")
            changed=[p for p in set(dirty)|set(current) if dirty.get(p,"clean")!=current.get(p,"clean")]
            annual.require(all(p==DIRECTORY+"/"+Path(p).name and Path(p).name in GENERATED for p in changed),"Changes exceeded exact eleven output allowlist")
            errors=validate_changed_paths(OWNER_ID,PRODUCER,changed,load_ownership_rules(root/"config/model_research_artifact_ownership.csv"))
            annual.require(not errors,"New owner artifact guard rejected changes: "+";".join(errors))
            print(f"model-owned medium-term guard passed changed_paths={len(changed)} protected_git_mapping_paths={len(after['git_tree_blob_mapping'])} protected_physical_files={len(after['physical_sha256'])}",flush=True)


def write_outputs(root,artifacts,output_root=None):
    root=Path(root).resolve();requested=Path(output_root) if output_root else root/DIRECTORY
    output=requested.resolve();sealed=annual.SEALED_ROOT.resolve()
    annual.require(output==(root/DIRECTORY).resolve() and output!=sealed and sealed not in output.parents,"Exact registered nonsealed output directory required")
    annual.require(not any(p.is_symlink() for p in [requested,*requested.parents]),"Output directory symlink forbidden")
    annual.require(set(artifacts)==GENERATED and all(isinstance(v,bytes) for v in artifacts.values()),"Exact eleven byte allowlist required")
    annual.require(not any((output/n).is_symlink() for n in GENERATED),"Artifact symlink forbidden")
    output.mkdir(parents=True,exist_ok=True)
    for name in sorted(GENERATED):(output/name).write_bytes(artifacts[name])


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-root",type=Path,required=True)
    parser.add_argument("--price-repository-root",type=Path)
    parser.add_argument("--contract",type=Path,default=ROOT/CONTRACT_FILE)
    parser.add_argument("--output-root",type=Path,default=ROOT/DIRECTORY)
    args=parser.parse_args(argv)
    annual.require(args.contract.resolve()==(ROOT/CONTRACT_FILE).resolve(),"Exact model-owned contract path required")
    contract=json.loads(args.contract.read_text(encoding="utf-8"))
    with artifact_guard(ROOT):
        artifacts=build(args.price_repository_root or ROOT,contract,args.input_root)
        write_outputs(ROOT,artifacts,args.output_root)
    return 0


if __name__=="__main__":
    raise SystemExit(main())
