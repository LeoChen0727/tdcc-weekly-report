"""Model-owned receipted TDCC research replay; never formal promotion evidence.

The fixed research v2 enum fallback is not the production phase classifier.
Raw unadjusted price cashflows are proxies, not verified total returns.
"""
from __future__ import annotations

import argparse
import ast
import bisect
import csv
import fnmatch
import hashlib
import io
import json
import math
import re
import statistics
import subprocess
from collections import Counter, defaultdict
from contextlib import contextmanager
from datetime import datetime, timedelta
from decimal import Decimal, localcontext
from pathlib import Path
from types import SimpleNamespace
from typing import Any

from model_research_artifact_guard import (
    load_ownership_rules, load_protected_sentinels, model_owned_artifact_guard,
    validate_changed_paths,
)

ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "tdcc_stealth_accumulation"
OWNER_ID = "tdcc_stealth_accumulation_receipted_marketwide_replay"
PRODUCER = "scripts/build_tdcc_stealth_accumulation_receipted_marketwide_replay.py"
ARTIFACT_VERSION = OWNER_ID + "_v1"
PREFIX = OWNER_ID + "_"
DIRECTORY = "output/research/tdcc_stealth_accumulation"
CONTRACT_FILE = "config/tdcc_stealth_accumulation_receipted_marketwide_replay_v1.json"
AVAILABILITY_FILE = "config/tdcc_stealth_accumulation_receipted_marketwide_availability_v1.json"
PINNED_REFS = {
    "selector_ref": "2244a0a36c4542cd62948b50f12ef98ade50e1df",
    "operation_ref": "b4c289c98f7276f07036c1b8b4d90d9d8de466bd",
    "classifier_ref": "af71f09d64aabbbadf9481940590dce21cd8e263",
    "outcome_ref": "40cee0405390a9ccaf3a1ad0778aa1e680ab8252",
}
KINDS = ("source_manifest", "coverage", "features", "signals", "trades",
         "summary", "blocked", "anomalies", "report")
NAMES = {kind: PREFIX + kind + "_v1." + (
    "json" if kind == "source_manifest" else "md" if kind == "report" else "csv"
) for kind in KINDS}
GENERATED = frozenset(NAMES.values())
CSV_FIELDS = {
    "coverage": "signal_date,input_ref,receipt_id,mother_population_basis,path,missing,total_rows,universe_rows,excluded_code_rows,duplicate_keys,alias_payload_conflict,coverage_status,pit_supported_rows,selected_signals,unsupported_reason_counts,historical_closed_date_files_excluded,receipt_available_no_later_than,entry_cutoff,receipt_gap_audit".split(","),
    "features": "stock_id,stock_name,market,signal_date,tdcc_price_phase,tdcc_status,volume_confirmed_breakout,open,high,low,close,return_5d,return_20d,daily_return_calc,previous_close,high_20,low_20,previous_20d_high_ex_today,volume_ma20,volume_ma20_lots,volume_ratio,tdcc_accumulation_signal,tdcc_accumulation_description,tdcc_400_change_sum,tdcc_1000_change_sum,tdcc_400_up_weeks,tdcc_1000_up_weeks,feature_id,input_ref,receipt_id,available_no_later_than,entry_cutoff,universe_source_path,universe_source_sha256,observed_history_dates,history_observations,history_missing_session_dates,history_gap_count,historical_closed_date_files_excluded,tdcc_window_dates,tdcc_paths,phase_policy,instrument_note,input_availability_proven,feature_supported,unsupported_reasons,raw_selector_selected,selected,positive_resolution,attack_already_started,primary_row_retained,formal_use,promotion_evidence_allowed".split(","),
    "trades": "trade_id,signal_date,stock_id,stock_name,market,horizon,slippage_bps,entry_date,exit_date,entry_open,exit_close,shares,entry_notional,buy_fee,entry_cash,exit_notional,sell_fee,sell_tax,net_exit_cash,net_pnl,gross_return_pct,net_return_pct,outcome,simulation_status,strict_v3_status,strict_missing_evidence,ca_cashflow_assumption,total_return_verified,input_ref,receipt_id,outcome_ref,entry_source_path,entry_source_sha256,exit_source_path,exit_source_sha256,history_gap_count,anomaly_candidate,primary_row_retained,formal_use,promotion_evidence_allowed".split(","),
    "summary": "horizon,slippage_bps,population,realized_raw_price_proxy_positions,total_input_signals,proxy_no_entry_signals,proxy_immature_positions,proxy_unresolved_exit_positions,strict_verified_total_return_positions,denominator,win_count,neutral_count,failure_count,mean_net_return_pct,median_net_return_pct,win_rate_pct,neutral_rate_pct,failure_rate_pct,high_return_ge10_rate_pct,loss_le_minus10_rate_pct,min_net_return_pct,max_net_return_pct,anomaly_candidate_positions,caveat,gap_present_positions,gap_present_mean_return_pct,gap_present_median_return_pct,gap_present_win_rate_pct,gap_absent_positions,gap_absent_mean_return_pct,gap_absent_median_return_pct,gap_absent_win_rate_pct".split(","),
    "blocked": "record_type,signal_date,stock_id,reasons,primary_row_retained,horizon,entry_date,exit_date,entry_open,strict_v3_status,strict_entry_established,strict_prior_position_locked,proxy_result_must_not_release_strict_lock".split(","),
    "anomalies": "signal_date,stock_id,horizon,net_return_pct,reason,disposition,primary_row_retained,exclusion_allowed_only_as_sensitivity,entry_date,exit_date,represented_in_current_proxy_trade".split(","),
}
CSV_FIELDS["signals"] = CSV_FIELDS["features"]
SEALED_ROOT = Path("F:/CodexStorage/retained-evidence/taiwan-stock-recommendation")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class GitSource:
    """Per-build immutable blob reader; injectable without materializing files."""

    def __init__(self, repository_root: Path):
        self.repository_root = Path(repository_root)
        self.sources = {}
        self._trees = {}
        self._objects = {}
        self._blobs = {}

    def _git(self, *args):
        return subprocess.check_output(
            ["git", "--no-replace-objects", "-C", str(self.repository_root), *args]
        )

    def tree(self, ref):
        require(bool(re.fullmatch(r"[0-9a-f]{40}", ref)), "Source refs must be full immutable SHAs")
        if ref not in self._trees:
            entries = self._git("ls-tree", "-r", "-z", ref).decode("utf-8").split("\0")
            self._trees[ref] = {
                entry.split("\t", 1)[1]: entry.split("\t", 1)[0].split()[2]
                for entry in entries if entry
            }
        return self._trees[ref]

    def blob(self, ref, path):
        key = (ref, path)
        if key not in self._blobs:
            oid = self.tree(ref).get(path)
            require(oid is not None, "Required blob is absent: " + ref + ":" + path)
            if oid not in self._objects:
                self._objects[oid] = self._git("cat-file", "blob", oid)
            payload = self._objects[oid]
            self._blobs[key] = payload
            self.sources[key] = dict(ref=ref, path=path, git_blob_oid=oid,
                                     bytes=len(payload), sha256=sha(payload))
        return self._blobs[key]


def records(payload):
    return list(csv.DictReader(io.StringIO(payload.decode('utf-8-sig'),newline='')))


def num(v):
    try:
        x = float(str(v).replace(',','').strip())
        return x if math.isfinite(x) else None
    except (ValueError,TypeError):
        return None


def pure(source,ref,path,names,env):
    parsed = ast.parse(source.blob(ref,path).decode('utf-8-sig'))
    nodes = [n for n in parsed.body if isinstance(n,ast.FunctionDef) and n.name in names]
    require({n.name for n in nodes} == names, 'Pinned selector AST function allowlist mismatch')
    future = ast.ImportFrom(module='__future__',names=[ast.alias(name='annotations')],level=0)
    exec(compile(ast.fix_missing_locations(ast.Module(body=[future]+nodes,type_ignores=[])),path,'exec'),env)
    return env


def csv_bytes(rows,empty_fields):
    fields = empty_fields
    buf = io.StringIO(newline='')
    w = csv.DictWriter(buf,fieldnames=fields,lineterminator='\n')
    w.writeheader()
    w.writerows(rows)
    return buf.getvalue().encode('utf-8')


def json_bytes(value):
    return (json.dumps(value,ensure_ascii=False,sort_keys=True,indent=2,allow_nan=False)+'\n').encode('utf-8')


def date_range(start,end):
    d = datetime.strptime(start,'%Y%m%d')
    stop = datetime.strptime(end,'%Y%m%d')
    while d <= stop:
        yield d.strftime('%Y%m%d'), d.weekday()
        d += timedelta(days=1)


def daily(source,ref,date):
    path = 'data/daily_price/'+date+'.csv'
    alias = 'data/daily_price/daily_price_'+date+'.csv'
    paths = source.tree(ref)
    if path not in paths:
        return {},dict(path=path,missing=True,total_rows=0,universe_rows=0)
    payload = source.blob(ref,path)
    payload_sha = sha(payload)
    alias_conflict = alias in paths and source.blob(ref,alias) != payload
    out = {}
    duplicates = set()
    rows = records(payload)
    for r in rows:
        sid = (r.get('stock_id') or r.get('ticker') or '').strip()
        if not re.fullmatch(r'[1-9][0-9]{3}',sid):
            continue
        d = (r.get('date') or '').replace('-','').strip()
        if sid in out:
            duplicates.add(sid)
        out[sid] = dict(stock_id=sid,stock_name=r.get('stock_name',r.get('name','')),
                       market=r.get('market',''),date=d,source=r.get('source',''),
                       source_path=path,source_ref=ref,source_sha256=payload_sha,
                       **{k:num(r.get(k)) for k in ['open','high','low','close','volume','trading_value']})
    for sid,r in out.items():
        r['duplicate_key'] = sid in duplicates
        r['date_mismatch'] = r['date'] != date
        r['alias_payload_conflict'] = alias_conflict
    return out,dict(path=path,missing=False,total_rows=len(rows),universe_rows=len(out),
                    excluded_code_rows=len(rows)-sum(bool(re.fullmatch(r'[1-9][0-9]{3}',(r.get('stock_id') or r.get('ticker') or '').strip())) for r in rows),
                    duplicate_keys=len(duplicates),alias_payload_conflict=alias_conflict)


def valid_price(r):
    return all(r.get(k) is not None and r[k]>0 for k in ['open','high','low','close']) and r['low']<=min(r['open'],r['close'])<=max(r['open'],r['close'])<=r['high'] and not r['duplicate_key'] and not r['date_mismatch'] and not r['alias_payload_conflict']


def load_selector(source, contract):
    """Load only frozen research helper functions, never a producer entrypoint."""
    rule_ref = contract["selector_ref"]
    base = pure(source,rule_ref,'scripts/build_tdcc_stealth_accumulation_historical_replay.py',
                {'_text','_number','_truthy','_row_text','_row_num','_flag','_volume_ma20_lots',
                 '_previous_close','_breakout_level','_bottom_volume_attack_like','evaluate_selector'},
                dict(math=math,re=re,Any=Any,POSITIVE_TDCC={'strong_accumulation','mild_accumulation'}))
    v2 = pure(source,rule_ref,'scripts/build_tdcc_stealth_accumulation_field_contract_replay.py',
              {'_text','_recognized_polarity','_resolve_tdcc_positive','evaluate_selector'},
              dict(base=SimpleNamespace(**base),BASE_EVALUATE_SELECTOR=base['evaluate_selector'],
                   POSITIVE={'strong_accumulation','mild_accumulation'},NONPOSITIVE={'distribution_warning','neutral'},Any=Any))
    classify = pure(source,contract['classifier_ref'],'tdcc_trend_utils.py',{'classify_accumulation'}, {})['classify_accumulation']
    require(classify(4,0.36,0.4,2,2)[0]=='strong_accumulation', 'Pinned classifier probe mismatch')
    return v2["evaluate_selector"], classify


def cost_cashflows(entry_open, exit_close, slippage_bps):
    """Fixed 1,000-share raw-price proxy, decimal precision independent of caller."""
    require(slippage_bps in (0, 10, 20), "Only fixed slippage scenarios are authorized")
    with localcontext() as context:
        context.prec = 50
        op = Decimal(str(entry_open))
        cl = Decimal(str(exit_close))
        require(op.is_finite() and cl.is_finite() and op > 0 and cl > 0,
                "Positive finite entry and exit prices are required")
        qty = Decimal(1000)
        slip = Decimal(slippage_bps) / Decimal(10000)
        buy = qty * op * (1 + slip)
        sell = qty * cl * (1 - slip)
        bf = max(Decimal(20), buy * Decimal("0.001425"))
        sf = max(Decimal(20), sell * Decimal("0.001425"))
        tax = sell * Decimal("0.003")
        cash = buy + bf
        exitcash = sell - sf - tax
        net = exitcash - cash
        return dict(entry_open=str(op), exit_close=str(cl), shares="1000",
                    entry_notional=str(buy), buy_fee=str(bf), entry_cash=str(cash),
                    exit_notional=str(sell), sell_fee=str(sf), sell_tax=str(tax),
                    net_exit_cash=str(exitcash), net_pnl=str(net),
                    gross_return_pct=str((cl / op - 1) * 100),
                    net_return_pct=str(net / cash * 100),
                    outcome="win" if net > 0 else "failure" if net < 0 else "neutral")


def validate_contract(contract):
    require(contract.get("model_id") == MODEL_ID, "Model ownership mismatch")
    require(all(contract.get(key) == value for key, value in PINNED_REFS.items()),
            "Fixed research source refs cannot be changed")
    require(contract.get("formal_use") is False and contract.get("promotion_evidence_allowed") is False,
            "Research-only flags must remain false")
    require(contract.get("costs") == dict(shares=1000, fee_each_side="0.001425",
            minimum_fee_each_side="20", sell_tax="0.003", slippage_bps=[0, 10, 20]),
            "Fixed operation costs cannot be changed")
    for key in ("requested_signal_start", "requested_signal_end", "as_of", "history_start", "calendar_end"):
        value = contract[key]
        require(bool(re.fullmatch(r"[0-9]{8}", value)), "Invalid date: " + key)
        datetime.strptime(value, "%Y%m%d")
    require(contract["history_start"] <= contract["requested_signal_start"]
            <= contract["requested_signal_end"] <= contract["as_of"] < contract["calendar_end"],
            "Invalid research date window")
    if "artifact_prefix" in contract:
        require(contract["artifact_prefix"] == PREFIX, "Artifact prefix cannot change")
    if "artifact_kinds" in contract:
        require({PREFIX + name for name in contract["artifact_kinds"]} == GENERATED,
                "Artifact allowlist must remain exactly nine files")


def build(repository_root: Path, contract: dict, availability: dict) -> dict[str, bytes]:
    """Build deterministic research bytes without any filesystem mutation."""
    validate_contract(contract)
    source = GitSource(Path(repository_root))
    evidence = availability
    source_ref = contract["outcome_ref"]
    evaluate_selector, classify = load_selector(source, contract)
    for path in ['scripts/build_stock_price_history.py', 'config/twse_non_trading_days.csv',
                 'data/market_calendar/exceptional_non_trading_days.csv']:
        source.blob(source_ref,path)
    source.blob(contract['operation_ref'],'scripts/build_tdcc_stealth_accumulation_operation_replay.py')
    source.blob(contract['operation_ref'],'docs/specs/tdcc_stealth_accumulation_operation_replay_v3.md')
    closures = {r['date'] for p in evidence['calendar_sources'] for r in records(source.blob(*p.split(':',1)))}
    calendar = [d for d,w in date_range(contract['history_start'],contract['calendar_end']) if w<5 and d not in closures]
    sessions = set(calendar)
    receipts = {d:r for r in evidence['receipts'] for d in r['signal_dates']}
    require(len(receipts)==sum(len(r['signal_dates']) for r in evidence['receipts']), 'Duplicate receipt dates require an explicit precedence decision')
    req_dates = [d for d in calendar if contract['requested_signal_start']<=d<=contract['requested_signal_end']]
    features=[]; signals=[]; coverage=[]; blocked=[]; anomalies=[]
    for date in req_dates:
        receipt = receipts.get(date)
        ref = receipt['ref'] if receipt else source_ref
        universe,meta = daily(source,ref,date)
        common = dict(signal_date=date,input_ref=ref,receipt_id=receipt['id'] if receipt else '',
                      mother_population_basis='same_day_raw_historical_price_codes_not_candidates',**meta)
        if not receipt:
            audits=[r for r in evidence.get('negative_receipt_audits',[]) if r['signal_date']==date]
            coverage.append(dict(**common,coverage_status='receipt_not_established_from_tested_run' if audits else 'exact_version_not_yet_pinned',
                                 receipt_gap_audit=' | '.join(r['finding'] for r in audits),pit_supported_rows=0,selected_signals=0))
            continue
        entry_date = calendar[bisect.bisect_right(calendar,date)]
        cutoff = datetime.fromisoformat(datetime.strptime(entry_date,'%Y%m%d').strftime('%Y-%m-%d')+'T08:30:00+08:00')
        available = datetime.fromisoformat(receipt['available_no_later_than'])
        require(available.tzinfo is not None and available < cutoff, 'Receipt must predate next-session 08:30 cutoff')
        paths = source.tree(ref)
        weekday_price_dates = sorted(p[-12:-4] for p in paths if re.fullmatch(r'data/daily_price/[0-9]{8}\.csv',p) and contract['history_start']<=p[-12:-4]<=date and datetime.strptime(p[-12:-4],'%Y%m%d').weekday()<5)
        historical_closures = {d for d in closures if d<=date}
        excluded_closed_dates = sorted(set(weekday_price_dates)&historical_closures)
        price_dates = [d for d in weekday_price_dates if d not in historical_closures]
        history=defaultdict(list)
        for hd in price_dates:
            dr,_ = daily(source,ref,hd)
            for sid,r in dr.items():
                if sid in universe:
                    history[sid].append(r)
        tdcc_paths = sorted(p for p in paths if re.fullmatch(r'output/history/tdcc/tdcc_holder_ratio_[0-9]{8}\.csv',p) and p[-12:-4]<=date)[-4:]
        tdcc = defaultdict(list)
        for p in tdcc_paths:
            seen=set()
            for r in records(source.blob(ref,p)):
                sid=r.get('code',r.get('stock_id','')).strip()
                require(sid not in seen, f'Duplicate TDCC identity: {ref}:{p}:{sid}')
                seen.add(sid)
                tdcc[sid].append(dict(date=p[-12:-4],row_date_valid=(r.get('date','').replace('-','')==p[-12:-4]),p400=num(r.get('over_400_pct')),p1000=num(r.get('over_1000_pct'))))
        selected_count=0; supported_count=0; reason_counts=Counter()
        for sid,r in sorted(universe.items()):
            reasons=[]
            if not valid_price(r): reasons.append('signal_ohlc_invalid_or_conflicting')
            hs=history[sid][-21:]
            if len(hs)<21: reasons.append('insufficient_21_observations')
            if not all(valid_price(x) for x in hs): reasons.append('history_ohlc_invalid_or_conflicting')
            if any(x['volume'] is None or x['volume']<0 for x in hs[-20:]): reasons.append('volume_missing_or_negative')
            if any(x['source']=='TPEX_OLD_DAILY_JSON' for x in hs[-20:]): reasons.append('raw_volume_lineage_unresolved')
            ts=tdcc.get(sid,[])
            if len(ts)!=4 or any(x['p400'] is None or x['p1000'] is None for x in ts): reasons.append('tdcc_four_batch_coverage_missing')
            if any(not x['row_date_valid'] for x in ts):reasons.append('tdcc_effective_date_mismatch')
            row=dict(stock_id=sid,stock_name=r['stock_name'],market=r['market'],signal_date=date,
                     tdcc_price_phase='',tdcc_status='',volume_confirmed_breakout=False)
            row.update({k:'' if r[k] is None else str(r[k]) for k in ['open','high','low','close']})
            derived={}
            if len(hs)==21 and all(valid_price(x) for x in hs):
                derived.update(return_5d=(r['close']/hs[-6]['close']-1)*100,
                               return_20d=(r['close']/hs[-21]['close']-1)*100,
                               daily_return_calc=(r['close']/hs[-2]['close']-1)*100,
                               previous_close=hs[-2]['close'],high_20=max(x['high'] for x in hs[-20:]),
                               low_20=min(x['low'] for x in hs[-20:]),previous_20d_high_ex_today=max(x['high'] for x in hs[-21:-1]))
                if all(x['volume'] is not None and x['volume']>=0 for x in hs[-20:]):
                    avg=statistics.mean(x['volume'] for x in hs[-20:])
                    if avg>0:
                        derived.update(volume_ma20=avg,volume_ma20_lots=avg/1000,volume_ratio=r['volume']/avg)
                    else: reasons.append('volume_mean_zero')
            row.update({k:format(round(v,4),'.4f') for k,v in derived.items()})
            if len(ts)==4 and all(x['p400'] is not None and x['p1000'] is not None for x in ts):
                s400=ts[-1]['p400']-ts[0]['p400'];s1000=ts[-1]['p1000']-ts[0]['p1000']
                u400=sum(b['p400']>a['p400'] for a,b in zip(ts,ts[1:]));u1000=sum(b['p1000']>a['p1000'] for a,b in zip(ts,ts[1:]))
                enum_value,enum_description=classify(4,s400,s1000,u400,u1000)
                require(isinstance(enum_value,str) and enum_value in {'strong_accumulation','mild_accumulation','distribution_warning','neutral'}, 'Unknown pinned classifier enum')
                row.update(tdcc_accumulation_signal=enum_value,tdcc_accumulation_description=enum_description,
                           tdcc_400_change_sum=round(s400,4),tdcc_1000_change_sum=round(s1000,4),
                           tdcc_400_up_weeks=u400,tdcc_1000_up_weeks=u1000)
            ev=evaluate_selector(row)
            supported=not reasons
            selected=supported and bool(ev['selector_selected'])
            missing_dates=[d for d in calendar if hs and hs[0]['date']<=d<=date and d not in {x['date'] for x in hs}]
            feature=dict(**row,feature_id=date+':'+sid,input_ref=ref,receipt_id=receipt['id'],
                         available_no_later_than=receipt['available_no_later_than'],entry_cutoff=cutoff.isoformat(),
                         universe_source_path=r['source_path'],universe_source_sha256=r['source_sha256'],
                         observed_history_dates=';'.join(x['date'] for x in hs),history_observations=len(hs),
                         history_missing_session_dates=';'.join(missing_dates),history_gap_count=len(missing_dates),
                         historical_closed_date_files_excluded=';'.join(excluded_closed_dates),
                         tdcc_window_dates=';'.join(x['date'] for x in ts),tdcc_paths=';'.join(tdcc_paths),
                         phase_policy='phase_classifier_not_invoked',instrument_note='possible_TDR_91_prefix' if sid.startswith('91') else 'four_digit_nonzero_equity_code',
                         input_availability_proven=True,feature_supported=supported,unsupported_reasons=';'.join(reasons),
                         raw_selector_selected=bool(ev['selector_selected']),selected=selected,
                         positive_resolution=ev['tdcc_positive_resolution'],attack_already_started=ev['attack_already_started'],
                         primary_row_retained=True,formal_use=False,promotion_evidence_allowed=False)
            features.append(feature)
            supported_count+=supported;selected_count+=selected;reason_counts.update(reasons)
            if selected: signals.append(feature)
            if reasons: blocked.append(dict(record_type='feature_unavailable',signal_date=date,stock_id=sid,reasons=';'.join(reasons),primary_row_retained=True))
        coverage.append(dict(**common,coverage_status='receipted_tree_partial_quality_coverage',
                             pit_supported_rows=supported_count,selected_signals=selected_count,
                             unsupported_reason_counts=json.dumps(dict(reason_counts),sort_keys=True),
                             historical_closed_date_files_excluded=';'.join(excluded_closed_dates),
                             receipt_available_no_later_than=receipt['available_no_later_than'],entry_cutoff=cutoff.isoformat()))
    outcomes={}
    outcome_meta={}
    for date in [d for d in calendar if contract['requested_signal_start'] <= d <= contract['as_of']]:
        outcomes[date],outcome_meta[date]=daily(source,source_ref,date)
    trades=[]
    strict_decisions=[]
    for horizon in [5,10,20]:
        proxy_held={};strict_held={}
        for signal in sorted(signals,key=lambda x:(x['signal_date'],x['stock_id'])):
            sid=signal['stock_id'];sd=signal['signal_date'];idx=bisect.bisect_right(calendar,sd)
            ed=calendar[idx];xd=calendar[idx+horizon]
            er=outcomes.get(ed,{}).get(sid);xr=outcomes.get(xd,{}).get(sid)
            strict_entered=False
            if sid in strict_held:
                strict_status='blocked_active_position'
                strict_reason='prior_strict_position_unresolved'
            elif ed>contract['as_of']:
                strict_status='blocked_entry_after_as_of'
                strict_reason='entry_after_as_of'
            elif not er or not valid_price(er):
                strict_status='blocked_entry_price'
                strict_reason='entry_price_missing_or_invalid'
            elif not evidence.get('calendar_complete_coverage_verified',False):
                strict_status='blocked_calendar_unverified'
                strict_reason='complete_official_calendar_event_coverage_not_yet_verified'
            else:
                strict_entered=True
                strict_held[sid]=sd
                strict_status='open_immature' if xd>contract['as_of'] else 'open_unresolved_exit'
                strict_reason='future_exit_not_mature' if xd>contract['as_of'] else 'corporate_action_complete_coverage_unverified'
            strict_decisions.append(dict(record_type='strict_ledger_decision',signal_date=sd,stock_id=sid,
                horizon=horizon,entry_date=ed,exit_date=xd,strict_v3_status=strict_status,
                strict_entry_established=strict_entered,strict_prior_position_locked=sid in strict_held,
                reasons=strict_reason,entry_open=er['open'] if er else '',
                proxy_result_must_not_release_strict_lock=True))
            reason=''
            if sid in proxy_held and sd<=proxy_held[sid]:
                reason='blocked_exit_day' if sd==proxy_held[sid] else 'blocked_active_position'
            if not reason and ed>contract['as_of']:reason='entry_after_as_of'
            if not reason and (not er or not valid_price(er)): reason='entry_price_missing_or_invalid'
            if reason:
                blocked.append(dict(record_type='operation_no_entry',signal_date=sd,stock_id=sid,horizon=horizon,
                                    entry_date=ed,exit_date=xd,reasons=reason,strict_v3_status=strict_status))
                continue
            proxy_held[sid]=xd if xr and valid_price(xr) else '99999999'
            if xd>contract['as_of'] or not xr or not valid_price(xr):
                blocked.append(dict(record_type='operation_censored',signal_date=sd,stock_id=sid,horizon=horizon,
                                    entry_date=ed,exit_date=xd,reasons='open_immature' if xd>contract['as_of'] else 'open_unresolved_exit_price',
                                    entry_open=er['open'],strict_v3_status=strict_status))
                continue
            for sb in [0,10,20]:
                trades.append(dict(trade_id=f'{sd}:{sid}:D{horizon}:S{sb}',signal_date=sd,stock_id=sid,
                    stock_name=signal['stock_name'],market=signal['market'],horizon=horizon,slippage_bps=sb,
                    entry_date=ed,exit_date=xd,**cost_cashflows(er['open'],xr['close'],sb),
                    simulation_status='realized_raw_price_proxy',strict_v3_status=strict_status,
                    strict_missing_evidence='corporate_action_complete_coverage;calendar_event_full_audit',
                    ca_cashflow_assumption='not_applied_not_asserted_absent',total_return_verified=False,
                    input_ref=signal['input_ref'],receipt_id=signal['receipt_id'],outcome_ref=source_ref,
                    entry_source_path=er['source_path'],entry_source_sha256=er['source_sha256'],
                    exit_source_path=xr['source_path'],exit_source_sha256=xr['source_sha256'],
                    history_gap_count=signal['history_gap_count'],anomaly_candidate=False,
                    primary_row_retained=True,formal_use=False,promotion_evidence_allowed=False))
    # Distribution diagnostics identify candidates only. No magnitude-based deletion.
    anomaly_keys={(r['signal_date'],r['stock_id'],int(r['horizon'])) for r in evidence.get('retained_anomaly_candidates',[])}
    for r in evidence.get('retained_anomaly_candidates',[]):
        anomalies.append(dict(signal_date=r['signal_date'],stock_id=r['stock_id'],horizon=int(r['horizon']),
            net_return_pct=r['net_return_pct'],reason='previously_observed_candidate_retained_not_reclassified_by_larger_sample',
            disposition='unresolved_anomaly_candidate',primary_row_retained=True,
            exclusion_allowed_only_as_sensitivity=True,entry_date=r['entry_date'],exit_date=r['exit_date']))
    for h in [5,10,20]:
        group=[t for t in trades if t['horizon']==h and t['slippage_bps']==10]
        vals=sorted(float(t['net_return_pct']) for t in group)
        if len(vals)>=4:
            q1,_,q3=statistics.quantiles(vals,n=4,method='inclusive');iqr=q3-q1
            for t in group:
                x=float(t['net_return_pct'])
                if x<q1-3*iqr or x>q3+3*iqr:
                    key=(t['signal_date'],t['stock_id'],h)
                    if key in anomaly_keys:continue
                    anomaly_keys.add(key)
                    anomalies.append(dict(signal_date=key[0],stock_id=key[1],horizon=h,
                        net_return_pct=t['net_return_pct'],reason='outside_Q1_Q3_plus_3IQR_descriptive_candidate',
                        disposition='unresolved_anomaly_candidate',primary_row_retained=True,
                        exclusion_allowed_only_as_sensitivity=True,entry_date=t['entry_date'],exit_date=t['exit_date']))
    for t in trades:t['anomaly_candidate']=(t['signal_date'],t['stock_id'],t['horizon']) in anomaly_keys
    current_proxy_keys={(t['signal_date'],t['stock_id'],t['horizon']) for t in trades}
    for r in anomalies:
        r['represented_in_current_proxy_trade']=(r['signal_date'],r['stock_id'],int(r['horizon'])) in current_proxy_keys
    summary=[]
    for h in [5,10,20]:
        for sb in [0,10,20]:
            for population in ['primary_including_anomaly_candidates','sensitivity_excluding_anomaly_candidates']:
                g=[t for t in trades if t['horizon']==h and t['slippage_bps']==sb and (population.startswith('primary') or not t['anomaly_candidate'])]
                vals=[float(t['net_return_pct']) for t in g];n=len(vals)
                row=dict(horizon=h,slippage_bps=sb,population=population,realized_raw_price_proxy_positions=n,
                         total_input_signals=len(signals),
                         proxy_no_entry_signals=sum(r.get('horizon')==h and r['record_type']=='operation_no_entry' for r in blocked),
                         proxy_immature_positions=sum(r.get('horizon')==h and r.get('reasons')=='open_immature' for r in blocked),
                         proxy_unresolved_exit_positions=sum(r.get('horizon')==h and r.get('reasons')=='open_unresolved_exit_price' for r in blocked),
                         strict_verified_total_return_positions=0,denominator='realized_raw_price_proxy_positions',
                         win_count=sum(x>0 for x in vals),neutral_count=sum(x==0 for x in vals),failure_count=sum(x<0 for x in vals),
                         mean_net_return_pct=statistics.mean(vals) if n else '',median_net_return_pct=statistics.median(vals) if n else '',
                         win_rate_pct=sum(x>0 for x in vals)/n*100 if n else '',neutral_rate_pct=sum(x==0 for x in vals)/n*100 if n else '',
                         failure_rate_pct=sum(x<0 for x in vals)/n*100 if n else '',high_return_ge10_rate_pct=sum(x>=10 for x in vals)/n*100 if n else '',
                         loss_le_minus10_rate_pct=sum(x<=-10 for x in vals)/n*100 if n else '',
                         min_net_return_pct=min(vals) if n else '',max_net_return_pct=max(vals) if n else '',
                         anomaly_candidate_positions=sum(t['anomaly_candidate'] for t in g),
                         caveat='raw_unadjusted_price_proxy_not_verified_total_return;not_performance_promotion_evidence')
                for group_name,condition in [('gap_present',lambda t:t['history_gap_count']>0),('gap_absent',lambda t:t['history_gap_count']==0)]:
                    subgroup=[float(t['net_return_pct']) for t in g if condition(t)]
                    row[group_name+'_positions']=len(subgroup)
                    row[group_name+'_mean_return_pct']=statistics.mean(subgroup) if subgroup else ''
                    row[group_name+'_median_return_pct']=statistics.median(subgroup) if subgroup else ''
                    row[group_name+'_win_rate_pct']=sum(x>0 for x in subgroup)/len(subgroup)*100 if subgroup else ''
                summary.append(row)
    blocked.extend(strict_decisions)
    counts = dict(
        requested_session_dates=len(req_dates), receipted_signal_dates=sorted(receipts),
        covered_universe_rows=len(features), supported_feature_rows=sum(r["feature_supported"] for r in features),
        signals=len(signals), realized_proxy_trade_rows=len(trades), anomaly_candidates=len(anomalies),
        signals_with_history_gaps=sum(r["history_gap_count"] > 0 for r in signals),
        anomaly_candidates_current_proxy_keys=len(anomaly_keys & current_proxy_keys),
        anomaly_candidates_removed_from_primary=0, strict_verified_total_return_positions=0,
        strict_ledger_rows=len(strict_decisions),
        strict_status_counts=dict(Counter(r["strict_v3_status"] for r in strict_decisions)),
    )
    row_groups = dict(coverage=coverage, features=features, signals=signals, trades=trades,
                      summary=summary, blocked=blocked, anomalies=anomalies)
    artifacts = {NAMES[kind]: csv_bytes(rows, CSV_FIELDS[kind]) for kind, rows in row_groups.items()}
    artifacts[NAMES["report"]] = report_bytes(contract, counts, coverage, summary)
    manifest = dict(
        model_id=MODEL_ID, artifact_version=ARTIFACT_VERSION,
        sources=sorted(source.sources.values(), key=lambda r: (r["ref"], r["path"])),
        receipt_evidence_file=AVAILABILITY_FILE, contract_file=CONTRACT_FILE,
        contract_sha256=sha(json_bytes(contract)), availability_sha256=sha(json_bytes(availability)),
        contract=contract, availability=availability, counts=counts,
        hashes={name: dict(bytes=len(value), sha256=sha(value)) for name, value in artifacts.items()},
        source_selector_import_policy="exact allowlisted pure AST nodes; no producer execution",
        full_period_pit_complete=False, formal_use=False, promotion_evidence_allowed=False,
        retention="model-owned research evidence until explicit supersession or cleanup authorization",
    )
    artifacts[NAMES["source_manifest"]] = json_bytes(manifest)
    require(set(artifacts) == GENERATED, "Producer must emit exactly nine model-owned artifacts")
    return artifacts


def report_bytes(contract, counts, coverage, summary):
    lines = [
        "# TDCC 潛伏吸籌：有收據全市場研究重建 v1", "",
        "這是 research-only 的現行固定研究語義歷史重建，不是完整原始 PIT、正式 production selector、正式可採用勝率或已核實 total-return。", "",
        "formal_use=False；promotion_evidence_allowed=False；full_period_pit_complete=False。", "",
        f"訊號範圍：{contract['requested_signal_start']}–{contract['requested_signal_end']}；結果資料 as_of：{contract['as_of']}。",
        f"有收據日期 {len(counts['receipted_signal_dates'])}；實際特徵列 {counts['covered_universe_rows']}；支持特徵列 {counts['supported_feature_rows']}；訊號 {counts['signals']}。",
        f"價格 proxy 交易列 {counts['realized_proxy_trade_rows']}（每部位三種成本情境）；strict 已核實總報酬部位 0。",
        f"異常候選 {counts['anomaly_candidates']}；未解異常保留 primary，排除版本僅 sensitivity，不是 corrected performance。", "",
        "## 邊界", "",
        "- 母體是當日四位且非零開頭的原始行情代碼，包含已註記的可能 91 開頭 TDR；不是今日存活名單，也不是已逐檔驗證普通股分類。",
        "- 只用各日收據指定同一 Git tree 的歷史資料。缺 receipt 日期不產生特徵，不借用 latest；事後結果來源不能補 decision features。",
        "- 每股至少 21 個既有觀測、末 20 個觀測量均值與四批 TDCC；缺交易日揭露、不前填，不把暖身日期或較長少數股票覆蓋冒稱全市場可評估日期。",
        "- 固定研究 v2 enum fallback：phase/status 明確留白；不是正式 production phase classifier。",
        "- 收據支持版本可得時間，但 unknown source lineage 不等於 PIT proof；空白 source 不自行增加模型 gate。",
        "- 買入為下一 session open，D+5/10/20 future close；各持有期獨立持倉鎖，當日出場不接受同股再入場訊號。",
        "- 未調整原始價格 proxy 不套用未證實公司行動現金流／股數變動；不是已核實 total-return、券商成交或模型升級證據。",
        "- 完整官方 calendar event coverage 與 corporate-action coverage 未核實，strict ledger 保持阻擋／未解狀態；proxy 出場不能解除 strict 持倉鎖。",
        "- 不以數值幅度判定資料錯誤。unresolved_anomaly_candidate 保留 primary；正式採用結論仍受阻。",
        "- 不使用月營收；EPS、毛利率、營益率、營業利益、業外損益、淨利、季度及年度財報均不在範圍。", "",
        "## 主要數值（10 bps，含未解異常候選）", "",
        "| 持有期 | 已實現 proxy 部位 | 勝／平／負 | 平均淨報酬 % | 中位淨報酬 % |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in summary:
        if row["slippage_bps"] == 10 and row["population"] == "primary_including_anomaly_candidates":
            mean = "" if row["mean_net_return_pct"] == "" else f"{row['mean_net_return_pct']:.6f}"
            median = "" if row["median_net_return_pct"] == "" else f"{row['median_net_return_pct']:.6f}"
            lines.append(f"| D+{row['horizon']} | {row['realized_raw_price_proxy_positions']} | {row['win_count']}/{row['neutral_count']}/{row['failure_count']} | {mean} | {median} |")
    lines.extend(["", "計算分母僅已實現 raw-price proxy 部位；未入場、未成熟及缺失出場價格分開列於 blocked，零 strict 部位不代表零報酬。",
                  "", "source_manifest 綁定各 Git blob、契約、收據與其餘八份最終序列化檔案的 SHA-256；本報告不是 producer 自我驗證證書。", ""])
    return "\n".join(lines).encode("utf-8")


def dirty_hashes(root):
    data = subprocess.check_output(["git", "--no-replace-objects", "status", "--porcelain", "-z", "--untracked-files=all"], cwd=root)
    result = {}
    for entry in data.decode("utf-8").split("\0"):
        if entry:
            path = entry[3:]
            file = root / path
            result[path] = sha(file.read_bytes()) if file.is_file() else "missing"
    return result


def protected_snapshot(root: Path, sentinels):
    """Sparse equivalent: immutable Git-object identities plus physical bytes.

    Absent sparse files are NOT claimed physically inspected. Their complete
    tree/index membership is bound, while ignored/skip-worktree physical files
    are inspected independently of git status. No protected materialization.
    """
    patterns = [sentinel.artifact_glob for sentinel in sentinels]
    matches = lambda path: any(fnmatch.fnmatchcase(path, pattern) for pattern in patterns)
    tree_data = subprocess.check_output(["git", "--no-replace-objects", "ls-tree", "-r", "-z", "HEAD"], cwd=root)
    index_data = subprocess.check_output(["git", "--no-replace-objects", "ls-files", "--stage", "-z"], cwd=root)
    tree, index, physical = {}, {}, {}
    for entry in tree_data.decode("utf-8").split("\0"):
        if entry:
            meta, path = entry.split("\t", 1)
            if matches(path):
                tree[path] = meta
    for entry in index_data.decode("utf-8").split("\0"):
        if entry:
            meta, path = entry.split("\t", 1)
            if matches(path):
                index[path] = meta
    candidates = set(tree) | set(index)
    for pattern in patterns:
        wildcard = min((pattern.find(char) for char in "*?[" if char in pattern), default=-1)
        if wildcard == -1:
            candidates.add(pattern)
            continue
        prefix = pattern[:wildcard].rsplit("/", 1)[0]
        directory = root / prefix
        if directory.exists():
            candidates.update(path.relative_to(root).as_posix() for path in directory.rglob("*") if path.is_file() and matches(path.relative_to(root).as_posix()))
    for relative in sorted(candidates):
        path = root / relative
        if path.is_symlink():
            raise RuntimeError(f"protected sentinel cannot be a symlink: {relative}")
        if path.is_file():
            physical[relative] = sha(path.read_bytes())
    for sentinel in sentinels:
        if sentinel.required and not any(fnmatch.fnmatchcase(path, sentinel.artifact_glob) for path in set(tree) | set(index) | set(physical)):
            raise RuntimeError(f"required protected sentinel family missing from Git and disk: {sentinel.sentinel_id}")
    return {"git_tree_blob_mapping": tree, "git_index_blob_mapping": index, "physical_sha256": physical}


@contextmanager
def artifact_guard(root):
    sparse = subprocess.run(["git", "--no-replace-objects", "config", "--bool", "core.sparseCheckout"], cwd=root, check=False, capture_output=True, text=True).stdout.strip() == "true"
    if not sparse:
        with model_owned_artifact_guard(OWNER_ID, PRODUCER, root=root, registry_path=root / "config/model_research_artifact_ownership.csv", sentinel_registry_path=root / "config/model_research_protected_sentinels.csv"):
            yield
        return
    sentinels = load_protected_sentinels(root / "config/model_research_protected_sentinels.csv")
    protected_before = protected_snapshot(root, sentinels)
    before = dirty_hashes(root)
    try:
        yield
    finally:
        after = dirty_hashes(root)
        protected_after = protected_snapshot(root, sentinels)
        if protected_before != protected_after:
            raise RuntimeError("protected sentinel Git mapping or physical SHA256 drift during model build/write")
        changed = [path for path in set(before) | set(after) if before.get(path, "clean") != after.get(path, "clean")]
        errors = validate_changed_paths(OWNER_ID, PRODUCER, changed, load_ownership_rules(root / "config/model_research_artifact_ownership.csv"))
        if errors:
            raise RuntimeError("model-owned sparse artifact guard failed: " + "; ".join(errors))
        print(f"model-owned sparse artifact guard passed owner={OWNER_ID} changed_paths={len(changed)}")
        print(f"protected_git_mapping_paths={len(protected_after['git_tree_blob_mapping'])}; protected_physical_files={len(protected_after['physical_sha256'])}")


def write_outputs(repository_root: Path, output_root: Path, artifacts: dict[str, bytes]):
    """Write only the nine owned filenames; sealed evidence is never a destination."""
    repository_root = Path(repository_root).resolve()
    output_root = Path(output_root).resolve()
    sealed = SEALED_ROOT.resolve()
    require(output_root != sealed and sealed not in output_root.parents,
            "Sealed retained evidence cannot be an output root")
    require(output_root == (repository_root / DIRECTORY).resolve(),
            "Output must use the exact registered model-owned directory")
    require(set(artifacts) == GENERATED and all(isinstance(value, bytes) for value in artifacts.values()),
            "Output allowlist must be exactly nine byte payloads")
    destinations = [output_root / name for name in sorted(GENERATED)]
    require(not any(path.is_symlink() for path in destinations), "Artifact symlink destinations are forbidden")
    output_root.mkdir(parents=True, exist_ok=True)
    for path in destinations:
        path.write_bytes(artifacts[path.name])


def main(argv=None):
    parser = argparse.ArgumentParser(description="Build only the receipted marketwide TDCC research replay.")
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    parser.add_argument("--output-root", type=Path)
    args = parser.parse_args(argv)
    root = args.repository_root.resolve()
    output_root = args.output_root or root / DIRECTORY
    contract = json.loads((root / CONTRACT_FILE).read_text(encoding="utf-8-sig"))
    availability = json.loads((root / AVAILABILITY_FILE).read_text(encoding="utf-8-sig"))
    with artifact_guard(root):
        artifacts = build(root, contract, availability)
        write_outputs(root, output_root, artifacts)
    print(f"{ARTIFACT_VERSION}: artifacts={len(artifacts)} research_only=True")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
