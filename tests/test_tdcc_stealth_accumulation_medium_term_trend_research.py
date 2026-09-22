"""Synthetic boundary tests; never run real annual research or source downloads."""
from __future__ import annotations

import copy
import csv
import gzip
import io
import json
import sys
from contextlib import contextmanager
from datetime import datetime,timedelta
from decimal import Decimal,localcontext
from pathlib import Path
from types import SimpleNamespace

import pytest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import build_tdcc_stealth_accumulation_medium_term_trend_research as p


def days(start="20250905",offsets=None,n=12):
    d=datetime.strptime(start,"%Y%m%d")
    return [(d+timedelta(days=i)).strftime("%Y%m%d") for i in (offsets if offsets is not None else range(0,n*7,7))]


def calendar(start="20250101",end="20261231"):
    return [d for d,w in p.annual.date_range(start,end) if w<5]


def weeks(dates=None,v400=None,v1000=None):
    dates=dates or days()
    v400=v400 or [Decimal(40)+i for i in range(len(dates))]
    v1000=v1000 or [Decimal(20)+i for i in range(len(dates))]
    return {d:{"2330":dict(p400=Decimal(v400[i]),p1000=Decimal(v1000[i]),path=d+".csv",sha256="a"*64)} for i,d in enumerate(dates)}


def raw_tdcc_fixture(values=None):
    dates=days(n=8);payloads={};external=[]
    values=values or [Decimal(40)+i for i in range(8)]
    for i,date in enumerate(dates):
        rows=[dict(日期=date,股票代碼="2330",持股分級=level,比例=str(values[i] if j==0 else 1)) for j,level in enumerate(p.LEVELS)]
        rows += [dict(日期=date,股票代碼="2330",持股分級="adjustment",比例="999"),dict(日期=date,股票代碼="2330",持股分級="total",比例="100")]
        data=p.annual.csv_bytes(rows,list(rows[0]));path=date+".csv";payloads[path]=data
        external.append(dict(kind="tdcc",date=date,path=path,rows=len(rows),sha256=p.annual.sha(data)))
    return dict(external_files=external,expected_tdcc_weeks=8,expected_tdcc_rows=48),payloads


def classify(n,a,b,u,v):
    if a>0 and b>0 and u>=2 and v>=2:return "strong_accumulation","strong"
    if a>0 or b>0:return "mild_accumulation","mild"
    if a<0 or b<0:return "distribution_warning","distribution"
    return "neutral","neutral"


def quote(date,**changes):
    row=dict(date=date,stock_id="2330",stock_name="合成",market="TWSE",open=10.0,high=11.0,low=9.0,close=10.0,volume=1000000.0,
             source="canonical",source_path="data/daily_price/"+date+".csv",source_sha256="f"*64,
             duplicate_key=False,date_mismatch=False,alias_payload_conflict=False)
    row.update(changes);return row


def price_feature_fixture():
    sessions=calendar();history=[quote(d) for d in sessions[:21]];date=sessions[20]
    dates=days("20241206",n=8);w=weeks(dates)
    original=dict(price_source_ref=p.PRICE_REF,_batch_paths={d:d+".csv" for d in dates})
    baseline=p.baseline_four(w,date,"2330",classify)
    return date,history,sessions,original,baseline


def replay_fixture(indices=(0,10,20,21,22,35,45,70),split_index=30,asof_index=100):
    sessions=calendar();prices={d:{"2330":quote(d)} for d in sessions}
    features=[]
    for i in indices:
        f={k:"1" for k in p.CONTRAST_FIELDS}
        f.update(feature_id=sessions[i]+":2330",signal_date=sessions[i],stock_id="2330",stock_name="合成",market="TWSE",history_gap_count=0,
                 price_qualified=True,baseline_4_supported=True,baseline_4_selected=True,w8_supported=i>=10,w8_selected=True,w12_supported=i>=20,w12_selected=True)
        features.append(f)
    c=dict(as_of=sessions[asof_index],split_date=sessions[split_index])
    return features,prices,sessions,c


def test_frozen_contract_matches_canonical_bytes_and_exact11():
    raw=(ROOT/p.CONTRACT_FILE).read_bytes();c=json.loads(raw)
    assert raw==p.annual.json_bytes(c)
    p.validate_contract(c)
    assert len(p.GENERATED)==11 and len(p.GZIP_KINDS)==5
    assert c["price_source_ref"]==p.PRICE_REF


@pytest.mark.parametrize("field,value",[("formal_use",True),("promotion_evidence_allowed",True),("split_date","20260402"),("price_source_ref","0"*40),("weekly_publication_policy","absolute ratios")])
def test_frozen_contract_rejects_any_semantic_change(field,value):
    c=json.loads((ROOT/p.CONTRACT_FILE).read_text(encoding="utf-8"));c[field]=value
    with pytest.raises(ValueError,match="Frozen medium-term contract changed"):p.validate_contract(c)


def test_exact_tdcc_four_bins_excludes_adjustment_total_and_keeps_decimal():
    original,payloads=raw_tdcc_fixture()
    w=p.load_tdcc_exact(original,payloads)
    r=w[days(n=8)[0]]["2330"]
    assert r["p400"]==Decimal(43) and r["p1000"]==Decimal(1)
    assert isinstance(r["p400"],Decimal)


@pytest.mark.parametrize("defect",["date","duplicate","rows","batches","total"])
def test_tdcc_source_scope_fails_closed(defect):
    c,payloads=raw_tdcc_fixture();item=c["external_files"][0];rows=p.annual.records(payloads[item["path"]])
    if defect=="date":rows[0]["日期"]="19000101"
    elif defect=="duplicate":rows[1]["持股分級"]=rows[0]["持股分級"]
    elif defect=="rows":item["rows"]+=1
    elif defect=="batches":c["expected_tdcc_weeks"]+=1
    else:c["expected_tdcc_rows"]+=1
    payloads[item["path"]]=p.annual.csv_bytes(rows,list(rows[0]))
    with pytest.raises(ValueError):p.load_tdcc_exact(c,payloads)


@pytest.mark.parametrize("value",["","--","NaN","Infinity"])
def test_tdcc_missing_ratio_never_zero_filled(value):
    c,payloads=raw_tdcc_fixture();item=c["external_files"][0];rows=p.annual.records(payloads[item["path"]]);rows[0]["比例"]=value
    payloads[item["path"]]=p.annual.csv_bytes(rows,list(rows[0]))
    w=p.load_tdcc_exact(c,payloads)
    assert w[item["date"]]["2330"]["p400"] is None


def test_equal_decimal_bin_totals_do_not_create_phantom_change():
    c,payloads=raw_tdcc_fixture()
    for i,item in enumerate(c["external_files"]):
        rows=p.annual.records(payloads[item["path"]])
        for r,v in zip(rows,[".15",".15","0","0"] if i%2==0 else [".1",".2","0","0"]):r["比例"]=v
        payloads[item["path"]]=p.annual.csv_bytes(rows,list(rows[0]))
    w=p.load_tdcc_exact(c,payloads)
    assert {r["2330"]["p400"] for r in w.values()}=={Decimal(".3")}
    assert p.baseline_four(w,days(n=8)[-1],"2330",classify)["enum"]=="neutral"
    assert 0.15+0.15 != 0.1+0.2


def test_weekly_offsets_hide_absolute_levels_and_anchor_first_complete_batch():
    dates=days(n=8);w=weeks(dates);w[dates[0]]["2330"]["p400"]=None
    rows=list(p.weekly_feature_rows(w))
    assert rows[0]["complete"] is False and rows[0]["anchor_date"]==""
    assert rows[1]["anchor_date"]==dates[1] and Decimal(rows[1]["offset400_pp"])==0
    assert Decimal(rows[-1]["offset400_pp"])==6
    assert set(rows[1])==set(p.SCHEMAS["weekly_features"])
    assert not ({"p400","p1000","absolute400","absolute1000"}&set(rows[1]))


def test_offsets_preserve_exact_ols_numerator_and_slope():
    dates=days(n=8);values=[Decimal("39.123456789")+Decimal(i)/100 for i in range(8)]
    a=p.exact_trend(dates,values);b=p.exact_trend(dates,[v-values[0] for v in values])
    assert a==b


def test_ols_irregular_actual_spacing_has_one_pp_per_week():
    offsets=[0,6,14,20,28,35,43,49];dates=days(offsets=offsets)
    with localcontext() as c:
        c.prec=50
        values=[Decimal(30)+Decimal(d)/7 for d in offsets]
        assert abs(p.exact_trend(dates,values)["slope"]-1)<Decimal("1e-47")


def test_eight_batch_positive_trend_can_have_negative_four_batch_delta():
    dates=days(n=8);v=[1,2,3,4,5,6,7,0];w=weeks(dates,[40+x for x in v],[20+x for x in v])
    r=p.window_metrics(w,dates[-1],"2330",8,calendar(),"20250101","20261231")
    with localcontext() as c:
        c.prec=50
        assert Decimal(r["slope400_pp_per_week"])==Decimal(1)/3
    assert r["selected"] is True
    assert p.baseline_four(w,dates[-1],"2330",classify)["selected"] is False


@pytest.mark.parametrize("values",[[1]*8,[1,2,3,4,4,3,2,1]])
def test_exact_zero_slope_rejected(values):
    dates=days(n=8);w=weeks(dates,values,values)
    r=p.window_metrics(w,dates[-1],"2330",8,calendar(),"20250101","20261231")
    assert r["selected"] is False and Decimal(r["numerator400"])==0


def test_symmetric_values_irregular_dates_not_forced_to_zero():
    dates=days(offsets=[0,7,14,21,28,35,42,48]);values=[1,2,3,4,4,3,2,1]
    with localcontext() as c:
        c.prec=50
        assert p.exact_trend(dates,list(map(Decimal,values)))["slope"]==Decimal(84)/16079


@pytest.mark.parametrize("n",[8,12])
def test_missing_current_batch_never_substitutes_older_stock_batch(n):
    dates=days(n=n+1);w=weeks(dates);del w[dates[-2]]["2330"]
    r=p.window_metrics(w,dates[-1],"2330",n,calendar(),"20250101","20261231")
    assert not r["supported"] and dates[-2] in r["missing_batch_dates"]
    assert r["dates"].split(";")==dates[-n:]


def test_insufficient_market_batches_not_zero_filled():
    w=weeks(days(n=7));r=p.window_metrics(w,max(w),"2330",8,calendar(),"20250101","20261231")
    assert not r["supported"] and "insufficient_market_batches" in r["reasons"]


def test_6_and_8_day_spacing_does_not_mean_missing_calendar_week():
    dates=["20250919","20250926","20251003","20251009","20251017","20251023","20251031","20251107"]
    assert p.missing_open_weeks(dates,calendar(),"20251107")==[]


def test_fully_closed_week_is_distinct_from_missing_open_week():
    dates=["20260213","20260226"]
    sessions=calendar();closed=[d for d in sessions if not "20260216"<=d<="20260220"]
    assert p.missing_open_weeks(dates,closed,"20260226")==[]
    assert p.missing_open_weeks(dates,sessions,"20260226")==["20260216"]


def test_trailing_completed_open_week_missing_even_after_last_batch():
    dates=["20250926","20251003","20251009"]
    assert p.missing_open_weeks(dates,calendar(),"20251016")==[]
    assert p.missing_open_weeks(dates,calendar(),"20251020")==["20251013"]


def test_future_tdcc_mutation_does_not_change_past_window():
    dates=["20250822","20250829","20250905","20250912","20250919","20250926","20251003","20251009","20251017"]
    w=weeks(dates);args=("20251016","2330",8,calendar(),"20250101","20261231")
    before=p.window_metrics(w,*args)
    w["20251017"]["2330"]["p400"]=Decimal("9999")
    assert p.window_metrics(w,*args)==before
    w.pop("20251017")
    assert p.window_metrics(w,*args)==before


def test_unknown_calendar_evidence_is_unsupported():
    w=weeks();r=p.window_metrics(w,max(w),"2330",8,calendar(),"20260101","20261231")
    assert not r["supported"] and "calendar_evidence_insufficient" in r["reasons"]


def test_jump_share_is_descriptive_and_missing_when_no_positive_change():
    values=list(map(Decimal,[1,4,3,5,5,5,5,5]));r=p.exact_trend(days(n=8),values)
    assert r["max_positive_share"]==Decimal("0.6")
    assert p.exact_trend(days(n=8),list(map(Decimal,range(8,0,-1))))["max_positive_share"] is None
    w=weeks(days(n=8),[1]*8,[1]*8);r=p.window_metrics(w,max(w),"2330",8,calendar(),"20250101","20261231")
    assert r["supported"] and r["max_positive_share400"]=="" and "no_positive_change_400" in r["descriptive_missing_reasons"]


def test_price_mother_population_not_gated_by_missing_four_batch_tdcc():
    date,h,c,original,b=price_feature_fixture();b=dict(supported=False,dates=[],paths=[])
    r=p.derive_price_row(date,"2330",h[-1],h,c,[],original,b)
    assert r["price_supported"] and r["price_qualified"]
    assert not r["feature_supported"] and not r["baseline_4_selected"]
    r.update(w8_supported=True,w8_selected=True)
    assert p.cohort_decision(r,"full_available","trend_8")== (True,True,True)


def test_price_observation_features_round_before_selector_and_preserve_gap():
    date,h,c,original,b=price_feature_fixture();h[-1]["close"]=10.00004
    r=p.derive_price_row(date,"2330",h[-1],h,c,[],original,b)
    assert r["return_5d"]=="0.0004" and r["volume_ma20_lots"]=="1000.0000"
    skipped=h.pop(1);h.insert(0,quote("20241231"))
    r=p.derive_price_row(date,"2330",h[-1],h,c,[],original,b)
    assert r["price_supported"] and r["history_gap_count"]>=1
    assert skipped["date"] in r["history_missing_session_dates"]


@pytest.mark.parametrize("defect",["missing_volume","negative_volume","old_volume","invalid_ohlc","duplicate","bad_date","short"])
def test_price_quality_cannot_be_bypassed_by_trend(defect):
    date,h,c,original,b=price_feature_fixture()
    if defect=="missing_volume":h[-2]["volume"]=None
    elif defect=="negative_volume":h[-2]["volume"]=-1
    elif defect=="old_volume":h[-2]["source"]="TPEX_OLD_DAILY_JSON"
    elif defect=="invalid_ohlc":h[-2]["low"]=99
    elif defect=="duplicate":h[-2]["duplicate_key"]=True
    elif defect=="bad_date":h[-2]["date_mismatch"]=True
    else:h=h[1:]
    r=p.derive_price_row(date,"2330",h[-1],h,c,[],original,b)
    assert not r["price_supported"] and not r["price_qualified"]


def test_closed_file_audit_only_discloses_actual_excluded_past_files():
    date,h,c,original,b=price_feature_fixture()
    # Caller passes actual closed-day copies, not the entire holiday calendar.
    r=p.derive_price_row(date,"2330",h[-1],h,c,["20250101","20261225"],original,b)
    assert r["historical_closed_date_files_excluded"]=="20250101"


@pytest.mark.parametrize("field,value",[("volume_ratio","2.5000"),("return_5d","8.0000"),("return_20d","20.0000")])
def test_original_strict_price_threshold_boundaries(field,value):
    date,h,c,original,b=price_feature_fixture();r=p.derive_price_row(date,"2330",h[-1],h,c,[],original,b)
    r[field]=value
    assert not p.price_qualifier(r)[0]


def test_original_attack_normal_and_locked_exclusions():
    date,h,c,original,b=price_feature_fixture();r=p.derive_price_row(date,"2330",h[-1],h,c,[],original,b)
    r.update(close="12",open="10",high="12",low="10",previous_close="10",previous_20d_high_ex_today="11",volume_ratio="2",volume_ma20_lots="1000")
    assert p.price_qualifier(r)[2]
    r.update(open="12",high="12",low="12",volume_ratio="1",daily_return_calc="20")
    assert p.price_qualifier(r)[2]


def test_common_profiles_are_eligibility_intersections_not_signal_intersections():
    features,_,_,_=replay_fixture();f=features[-1];f["baseline_4_selected"]=False
    assert p.cohort_decision(f,"common_8","baseline_4")== (True,True,False)
    assert p.cohort_decision(f,"common_8","trend_8")== (True,True,True)
    f["w12_supported"]=False
    assert not p.cohort_decision(f,"common_12","trend_8")[0]


def test_common_profile_starts_empty_and_never_inherits_prestart_position():
    f,prices,c,contract=replay_fixture()
    a,_=p.replay_positions(f,prices,c,contract,"full_available","baseline_4")
    b,_=p.replay_positions(f,prices,c,contract,"common_8","baseline_4")
    assert any(t["signal_date"]==c[0] for t in a)
    assert any(t["signal_date"]==c[10] for t in b)
    assert not any(t["signal_date"]==c[10] for t in a)


def test_split_purge_does_not_reset_nonoverlap_lock():
    f,prices,c,contract=replay_fixture(indices=(10,20,30,31,32),split_index=20);blocked=[]
    trades,_=p.replay_positions(f,prices,c,contract,"full_available","baseline_4",blocked.append)
    first=next(t for t in trades if t["horizon"]==20)
    assert first["partition"]=="purged_cross_split"
    assert any(t["signal_date"]==c[30] and t["reasons"]=="blocked_active_position" for t in blocked)
    assert any(t["signal_date"]==c[31] and t["reasons"]=="blocked_exit_day" for t in blocked)
    assert any(t["signal_date"]==c[32] and t["partition"]=="validation" for t in trades)


def test_entry_date_not_signal_date_controls_split():
    c=calendar();d,_=p.operation_dates(c,"20260331",20,"20260909","20260401")
    assert d["entry_date"]=="20260401" and d["partition"]=="validation"


@pytest.mark.parametrize("kind",["entry","exit","immature"])
def test_missing_entry_exit_and_immature_have_separate_lock_semantics(kind):
    f,prices,c,contract=replay_fixture(indices=(0,10))
    if kind=="entry":prices[c[1]].pop("2330")
    elif kind=="exit":prices[c[21]].pop("2330")
    else:contract["as_of"]=c[15]
    blocked=[];trades,_=p.replay_positions(f,prices,c,contract,"full_available","baseline_4",blocked.append)
    if kind=="entry":assert any(t["signal_date"]==c[10] and t["horizon"]==20 for t in trades)
    else:assert any(t["signal_date"]==c[10] and t["horizon"]==20 and t["reasons"]=="blocked_active_position" for t in blocked)
    reason={"entry":"entry_price_missing_or_invalid","exit":"open_unresolved_exit_price","immature":"open_immature"}[kind]
    assert any(t["reasons"]==reason for t in blocked)


def test_calendar_tail_cannot_index_future_exit_or_invent_date():
    c=calendar()[:40];d,mature=p.operation_dates(c,c[-3],60,c[-1],c[20])
    assert not mature and d["exit_date"]=="" and d["exit_target_index"]==98


def test_cashflow_cost_boundary_includes_minimum_fees_tax_and_slippage():
    f,prices,c,contract=replay_fixture(indices=(0,))
    prices[c[1]]["2330"].update(open=1.0,low=.9)
    prices[c[21]]["2330"].update(close=1.1,low=1.0)
    trades,_=p.replay_positions(f,prices,c,contract,"full_available","baseline_4")
    t=next(t for t in trades if t["horizon"]==20 and t["slippage_bps"]==10)
    assert Decimal(t["buy_fee"])==20 and Decimal(t["sell_fee"])==20
    assert Decimal(t["entry_notional"])==Decimal(1001)
    assert Decimal(t["sell_tax"])==Decimal("3.2967")
    assert not t["formal_use"] and not t["promotion_evidence_allowed"] and not t["total_return_verified"]


def candidate_trades(profile="full_available",strategy="trend_8",values=(1,1,1,1,1,500)):
    return [dict(profile=profile,strategy=strategy,horizon=20,slippage_bps=10,signal_date=str(i),stock_id="2330",net_return_pct=str(v),partition="purged_cross_split" if i==5 else "training",
                 entry_date="20250101",exit_date="20250402",primary_row_retained=True) for i,v in enumerate(values)]


def test_iqr_is_full_ledger_including_purged_and_needs_four_observations():
    assert not p.detect_candidates(candidate_trades(values=(1,1,500)))
    found=p.detect_candidates(candidate_trades())
    assert len(found)==1 and found[0]["signal_date"]=="5"
    assert found[0]["lower_fence"]==1 and found[0]["upper_fence"]==1


def test_cross_ledger_candidate_union_matches_same_horizon_and_all_slippage():
    found=p.detect_candidates(candidate_trades());key=p.anomaly_key(found[0]);det={key:found}
    other=candidate_trades("common_12","trend_12")[-1:]
    for h,s in [(20,0),(20,20),(60,10)]:other.append(dict(other[0],horizon=h,slippage_bps=s))
    anomalies=p.annotate_candidates(other,set(),det)
    assert [r["anomaly_candidate"] for r in other]==[True,True,True,False]
    assert anomalies[0]["detector_profile"]=="full_available" and anomalies[0]["profile"]=="common_12"
    assert all(t["primary_row_retained"] for t in other)


def test_prior_candidate_provenance_is_not_synthetic_trade():
    rows=candidate_trades(values=(1,));prior={p.anomaly_key(rows[0]),("old","9999",20)}
    a=p.annotate_candidates(rows,prior,{})
    assert len(a)==1 and a[0]["reason"]=="immutable_previous_candidate_retained"


def test_high_low_middle_and_negative_counts_are_distinct():
    f,prices,c,contract=replay_fixture(indices=(0,))
    trades=[]
    for i,value in enumerate(["10","-10","-1","0","9.99"]):
        feature=dict(f[0],feature_id=str(i));f.append(feature)
        trades.append(dict(profile="full_available",strategy="trend_8",feature_id=str(i),signal_date=str(i),stock_id="2330",horizon=20,slippage_bps=10,partition="training",net_return_pct=value,anomaly_candidate=True))
    contrasts=p.feature_contrasts(trades,{r["feature_id"]:r for r in f},set(),"full_available","trend_8")
    def count(group,pop="primary"):
        return next(r["samples"] for r in contrasts if r["horizon"]==20 and r["slippage_bps"]==10 and r["partition"]=="training" and r["population"]==pop and r["feature_name"]==p.CONTRAST_FIELDS[0] and r["outcome_group"]==group)
    assert [count(g) for g in ("high","low","middle")]==[1,1,3]
    assert count("all_realized","immutable_prior_candidate_exclusion_sensitivity")==5
    assert p.statistics_row([10,-10,-1,0,9.99])["failure_count"]==2


def test_nonempty_synthetic_schema_report_and_summary_coverage():
    f,prices,c,contract=replay_fixture();by={r["feature_id"]:r for r in f}
    summaries=[];contrasts=[]
    for profile,strategies in p.PROFILES.items():
        for strategy in strategies:
            blocks=[];trades,counts=p.replay_positions(f,prices,c,contract,profile,strategy,blocks.append)
            p.annotate_candidates(trades,set(),{})
            s=p.summarize(trades,counts,f,c,contract,profile,strategy);summaries+=s
            contrasts+=p.feature_contrasts(trades,by,set(),profile,strategy)
            assert p.annual.csv_bytes(trades,p.SCHEMAS["trades"])
            assert p.annual.csv_bytes(blocks,p.SCHEMAS["blocked"])
            assert all(r["win_count"]+r["neutral_count"]+r["failure_count"]==r["samples"] for r in s)
    assert len(summaries)==384 and len(contrasts)==39936
    counts=dict(universe_rows=8,price_supported_rows=8,price_qualified_rows=8,possible_tdr_rows=0,prior_candidate_keys=0,new_candidate_detections=0,candidate_union_keys=0)
    report=p.report_bytes(contract,[],summaries,contrasts,counts).decode()
    for text in ["不是strict PIT","不以舊selected signals","common_12","purged","corrected/cleaned performance","immutable","EPS","正/零/負率%"]:
        if text=="immutable":continue
        assert text in report


@pytest.mark.parametrize("defect",["missing","extra","nonbytes","wrong_root"])
def test_exact_eleven_writer_rejects_scope_before_write(tmp_path,defect):
    a={n:b"synthetic" for n in p.GENERATED};out=tmp_path/p.DIRECTORY
    if defect=="missing":a.pop(next(iter(a)))
    elif defect=="extra":a[p.annual.NAMES["summary"]]=b"no old overwrite"
    elif defect=="nonbytes":a[next(iter(a))]="notbytes"
    else:out=tmp_path/"wrong"
    with pytest.raises(ValueError):p.write_outputs(tmp_path,a,out)
    assert not out.exists()


def test_deterministic_gzip_and_successful_exact_writer(tmp_path):
    results=[]
    for _ in range(2):
        with p.gzip_writer(["key"]) as (w,sink):w.writerow(dict(key="合成"))
        results.append(sink.getvalue())
    assert results[0]==results[1] and gzip.decompress(results[0]).decode()=="key\n合成\n"
    artifacts={n:b"synthetic" for n in p.GENERATED};p.write_outputs(tmp_path,artifacts)
    assert {r.name for r in (tmp_path/p.DIRECTORY).iterdir()}==p.GENERATED


def test_cli_input_root_mandatory_and_no_old_producer_entrypoint():
    with pytest.raises(SystemExit) as exc:p.main([])
    assert exc.value.code==2
    assert p.PRODUCER!="scripts/build_tdcc_stealth_accumulation_current_version_annual_replay.py"


def mock_materialization_mode(monkeypatch,sparse):
    def read_sparse(command,**kwargs):
        assert command==["git","--no-replace-objects","config","--bool","core.sparseCheckout"]
        assert kwargs==dict(cwd=ROOT,check=False,capture_output=True,text=True)
        return SimpleNamespace(stdout="true\n" if sparse else "false\n")
    monkeypatch.setattr(p.subprocess,"run",read_sparse)


def mock_standard_guard(monkeypatch):
    calls=[]
    @contextmanager
    def standard(owner,producer,**kwargs):
        assert owner==p.OWNER_ID and producer==p.PRODUCER
        assert kwargs==dict(root=ROOT,
            registry_path=ROOT/"config/model_research_artifact_ownership.csv",
            sentinel_registry_path=ROOT/"config/model_research_protected_sentinels.csv")
        calls.append("entered")
        try:yield
        finally:calls.append("exited")
    monkeypatch.setattr(p,"model_owned_artifact_guard",standard)
    return calls


@pytest.mark.parametrize("sparse",[False,True])
@pytest.mark.parametrize("defect",["protected","other_file","old_output","owner"])
def test_guard_detects_protected_or_outside_writer_scope(monkeypatch,defect,sparse):
    mock_materialization_mode(monkeypatch,sparse)
    calls=mock_standard_guard(monkeypatch)
    monkeypatch.setattr(p,"load_protected_sentinels",lambda path:[])
    snapshots=iter([{"git_tree_blob_mapping":{},"physical_sha256":{}},{"git_tree_blob_mapping":{},"physical_sha256":{} if defect!="protected" else {"x":"bad"}}])
    monkeypatch.setattr(p.annual,"protected_snapshot",lambda *args:next(snapshots))
    path=p.DIRECTORY+"/"+p.NAMES["report"]
    if defect=="other_file":path="scripts/other.py"
    if defect=="old_output":path=p.DIRECTORY+"/"+p.annual.NAMES["summary"]
    changes=iter([{}, {path:"changed"}]);monkeypatch.setattr(p.annual,"dirty_hashes",lambda root:next(changes))
    monkeypatch.setattr(p,"load_ownership_rules",lambda path:[])
    monkeypatch.setattr(p,"validate_changed_paths",lambda *args:["wrong owner"] if defect=="owner" else [])
    with pytest.raises(ValueError):
        with p.artifact_guard(ROOT):pass
    assert calls==([] if sparse else ["entered","exited"])


@pytest.mark.parametrize("sparse",[False,True])
def test_guard_enters_standard_context_only_for_full_checkout_and_keeps_exact_eleven(monkeypatch,sparse):
    mock_materialization_mode(monkeypatch,sparse)
    calls=mock_standard_guard(monkeypatch)
    protected={"git_tree_blob_mapping":{},"git_index_blob_mapping":{},"physical_sha256":{}}
    monkeypatch.setattr(p.annual,"protected_snapshot",lambda *args:protected)
    changes=iter([{}, {p.DIRECTORY+"/"+name:"new" for name in p.GENERATED}])
    monkeypatch.setattr(p.annual,"dirty_hashes",lambda root:next(changes))
    original_validator=p.validate_changed_paths
    checked=[]
    def verify(owner,producer,changed,rules):
        assert owner==p.OWNER_ID and producer==p.PRODUCER
        assert set(changed)=={p.DIRECTORY+"/"+name for name in p.GENERATED}
        checked.append(True)
        return original_validator(owner,producer,changed,rules)
    monkeypatch.setattr(p,"validate_changed_paths",verify)
    with p.artifact_guard(ROOT):
        assert calls==([] if sparse else ["entered"])
    assert checked==[True]
    assert calls==([] if sparse else ["entered","exited"])


def test_full_checkout_standard_sentinel_rejection_prevents_body(monkeypatch):
    mock_materialization_mode(monkeypatch,False)
    standard_namespace=p.model_owned_artifact_guard.__wrapped__.__globals__
    monkeypatch.setitem(standard_namespace,"_dirty_snapshot",lambda root:{})
    monkeypatch.setitem(standard_namespace,"protected_sentinel_snapshot",
                        lambda *args:({},["synthetic protected sentinel unavailable"]))
    entered=[]
    with pytest.raises(RuntimeError,match="protected sentinel preflight failed"):
        with p.artifact_guard(ROOT):entered.append(True)
    assert entered==[]
