"""有限直接狀態回歸；不讀付費CSV、不重跑原selector。"""
import copy
from decimal import Decimal, localcontext
import importlib.util
from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
SPEC = importlib.util.spec_from_file_location('conservative_producer', ROOT / 'scripts/build_tdcc_stealth_accumulation_conservative_execution_research.py')
P = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(P)


def policy():
    return copy.deepcopy(P.load_policy(ROOT))


def row(identity='a', strategy='baseline_4', stock='1101', entry='20260504', exit='20260601', candidate='False'):
    r = dict(trade_id=identity, strategy=strategy, stock_id=stock, signal_date='20260430', entry_date=entry, exit_date=exit, entry_open='134', exit_close='416', net_return_pct='208.01757427822747428875860040554828094524325902075', anomaly_candidate=candidate, primary_row_retained='True', formal_use='False', promotion_evidence_allowed='False')
    return r


def event(state='unknown', full=False, qty=None):
    return dict(event_id='synthetic-event', stock_id='1101', start_date='20260504', end_date='20260504', state=state, reason='synthetic-not-market-evidence', full_validity_covered=full, supported_quantity=qty)


def test_normal_proxy_preserves_every_original_field_and_cost_formula():
    source = row()
    actual = P.replay([source], policy())[0]
    assert all(actual[k] == v for k, v in source.items())
    assert actual['execution_position_state'] == 'assumed_closed'
    assert actual['execution_entry_quantity'] == actual['execution_exit_quantity'] == 1000
    assert actual['execution_proxy_return_pct'] == source['net_return_pct']
    assert actual['actual_fill_verified'] is False and actual['execution_evidence_state'] == 'unknown'
    assert not actual['execution_lock_retained']


def test_entry_unknown_keeps_lock_and_later_row_primary_without_zero_return():
    c = policy(); c['exceptions'] = [event()]
    first, later = P.replay([row('a'), row('b', entry='20260701', exit='20260729')], c)
    assert first['execution_position_state'] == 'entry_unknown'
    assert later['execution_position_state'] == 'lock_blocked'
    assert later['execution_blocking_trade_id'] == 'a'
    assert all(r['execution_proxy_return_pct'] == '' and r['primary_row_retained'] == 'True' and r['execution_lock_retained'] for r in (first, later))


def test_exit_exception_does_not_retroactively_cancel_assumed_entry():
    r = P.replay([row(stock='2492')], policy())[0]
    assert r['execution_entry_state'] == 'assumed_regular_price_proxy'
    assert r['execution_exit_state'] == 'unknown'
    assert r['execution_position_state'] == 'exit_unknown'
    assert r['execution_proxy_return_pct'] == '' and r['execution_lock_retained']


def test_chronology_strategy_independence_and_fixed_cohort():
    c = policy(); c['exceptions'] = [event()]
    input_rows = [row('a'), row('b', entry='20260701', exit='20260729'), row('c', strategy='trend_8', entry='20260701', exit='20260729')]
    result = P.replay(input_rows[::-1], c)
    assert result == P.replay(input_rows, c)
    assert {r['execution_cohort_id'] for r in result} == {'common12-validation'}
    assert result[1]['execution_position_state'] == 'lock_blocked'
    assert result[2]['execution_position_state'] == 'assumed_closed'


def test_same_date_new_open_precedes_old_close_unlock():
    result = P.replay([row('a'), row('b', entry='20260601', exit='20260629')], policy())
    assert result[0]['execution_position_state'] == 'assumed_closed'
    assert result[1]['execution_position_state'] == 'lock_blocked'


def test_no_entry_requires_full_validity_and_is_not_loss():
    c = policy(); c['exceptions'] = [event('evidenced_no_fill', full=False)]
    assert P.replay([row()], c)[0]['execution_position_state'] == 'entry_unknown'
    c['exceptions'][0]['full_validity_covered'] = True
    result = P.replay([row('a'), row('b', entry='20260701', exit='20260729')], c)
    assert result[0]['execution_position_state'] == 'no_entry'
    assert result[0]['execution_proxy_return_pct'] == ''
    assert result[0]['execution_entry_quantity'] == 0 and not result[0]['execution_lock_retained']
    assert result[1]['execution_position_state'] == 'assumed_closed'


@pytest.mark.parametrize('qty', [0, 1000, -1, 1.5, True])
def test_partial_rejects_invalid_quantity(qty):
    c = policy(); c['exceptions'] = [event('partial_fill_out_of_scope', qty=qty)]
    with pytest.raises(ValueError, match='部分成交'):
        P.replay([row()], c)


def test_partial_entry_and_no_fill_exit_keep_exposure():
    c = policy(); c['exceptions'] = [event('partial_fill_out_of_scope', qty=400)]
    r = P.replay([row()], c)[0]
    assert r['execution_position_state'] == 'entry_partial' and r['execution_entry_quantity'] == 400
    assert r['execution_proxy_return_pct'] == '' and r['execution_lock_retained']
    c['exceptions'] = [event('evidenced_no_fill', full=True)]
    c['exceptions'][0].update(start_date='20260601', end_date='20260601')
    r = P.replay([row()], c)[0]
    assert r['execution_position_state'] == 'exit_no_fill' and r['execution_lock_retained']


def test_existing_candidates_retained_and_unknown_subset_denominator():
    result = P.replay([row('a', stock='6806', entry='20260518', candidate='True'), row('b', stock='1101')], policy())
    summary = {r['population']: r for r in P.summarize(result) if r['strategy'] == 'baseline_4'}
    assert summary['original_primary_proxy']['samples'] == 2
    assert summary['original_primary_proxy']['original_candidate_samples'] == 1
    subset = summary['assumed_completed_subset']
    assert subset['samples'] == 1 and subset['primary_samples'] == 2
    assert subset['execution_not_computable_pct'] == '50.0'
    assert subset['execution_evidence_unknown_samples'] == 2
    assert summary['original_candidate_exclusion_sensitivity']['samples'] == 1


def test_minimum_fees_and_source_hash_fail_closed(tmp_path):
    c = policy()
    with localcontext() as ctx:
        ctx.prec = 50
        buy = Decimal(1000) * Decimal('1') * Decimal('1.001')
        sell = Decimal(1000) * Decimal('2') * Decimal('0.999')
        expected = (sell - 20 - sell * Decimal('.003') - buy - 20) / (buy + 20) * 100
    assert P.costed_return(dict(entry_open='1', exit_close='2'), c) == expected
    wrong = tmp_path / 'bad.gz'; wrong.write_bytes(b'not-the-frozen-source')
    with pytest.raises(ValueError, match='ledger SHA'):
        P.load_ledger(ROOT, c, wrong)
