# TDCC Overheated Short-Term Edge

- generated_at: `2026-06-20 15:36:32 Asia/Taipei`
- tuning_status: `not_ready`
- allowed_changes: `reporting_priority_only`
- forbidden_changes: `core_weight_change`

## Calculation Method

- close-to-close win rate: `dN_return_pct > 0`, from signal close to D+N close, only mature_dN=True rows.
- close-to-close relative return: stock D+N return minus TWSE/TPEx benchmark D+N return.
- next-open return: next trading day's open to D+N close.
- next-open relative return: stock next-open return minus benchmark next-open return when benchmark OHLC is available.
- pending rows are not counted as success or failure.
- These rules are a short-term reporting specialty, not a core TDCC/ABM weight change.

## Current Matching Stocks

| signal_date | stock_id | stock_name | theme | rule_name_zh | price_ret_1w | price_ret_2w | d5_mature_count | d5_win_rate_pct | d5_avg_relative_return_pct | d10_mature_count | d10_win_rate_pct | d10_avg_relative_return_pct | sample_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 2241 | 艾姆勒 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 26.34207240948816 | 57.14285714285714 | 44 | 68.18 | 3.02 | 38 | 63.16 | 4.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 3362 | 先進光 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 28.65853658536586 | 46.52777777777777 | 44 | 68.18 | 3.02 | 38 | 63.16 | 4.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 2327 | 國巨* | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 28.266033254156774 | 45.35666218034993 | 44 | 68.18 | 3.02 | 38 | 63.16 | 4.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 2484 | 希華 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 17.298187808896202 | 40.15748031496065 | 44 | 68.18 | 3.02 | 38 | 63.16 | 4.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 5426 | 振發 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.795069337442214 | 39.08256880733945 | 44 | 68.18 | 3.02 | 38 | 63.16 | 4.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 4958 | 臻鼎-KY | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 21.361058601134218 | 30.355329949238573 | 44 | 68.18 | 3.02 | 38 | 63.16 | 4.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 6175 | 立敦 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 10.679611650485432 | 29.692832764505116 | 44 | 68.18 | 3.02 | 38 | 63.16 | 4.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 8358 | 金居 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 29.629629629629626 | 23.893805309734507 | 44 | 68.18 | 3.02 | 38 | 63.16 | 4.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 3484 | 崧騰 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 19.13513513513514 | 22.444444444444443 | 44 | 68.18 | 3.02 | 38 | 63.16 | 4.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 2882 | 國泰金 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 14.925373134328357 | 22.35169491525424 | 44 | 68.18 | 3.02 | 38 | 63.16 | 4.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 2332 | 友訊 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 27.707006369426757 | 21.148036253776436 | 44 | 68.18 | 3.02 | 38 | 63.16 | 4.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 2890 | 永豐金 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 19.69924812030075 | 20.060331825037704 | 44 | 68.18 | 3.02 | 38 | 63.16 | 4.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 3321 | 同泰 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 23.664122137404586 | 18.536585365853654 | 44 | 68.18 | 3.02 | 38 | 63.16 | 4.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 5425 | 台半 | power discrete/diodes | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 28.944504896626768 | 16.748768472906406 | 44 | 68.18 | 3.02 | 38 | 63.16 | 4.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 8096 | 擎亞 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 28.512396694214882 | 14.338235294117641 | 44 | 68.18 | 3.02 | 38 | 63.16 | 4.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 2887 | 台新新光金 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 12.86956521739131 | 13.66024518388793 | 44 | 68.18 | 3.02 | 38 | 63.16 | 4.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 2883 | 凱基金 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 10.81081081081081 | 12.226277372262784 | 44 | 68.18 | 3.02 | 38 | 63.16 | 4.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 6269 | 台郡 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 20.972644376899694 | 11.328671328671325 | 44 | 68.18 | 3.02 | 38 | 63.16 | 4.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 4707 | 磐亞 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 15.8690176322418 | 9.004739336492884 | 44 | 68.18 | 3.02 | 38 | 63.16 | 4.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 4534 | 慶騰 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 12.166666666666659 | 6.319115323854652 | 44 | 68.18 | 3.02 | 38 | 63.16 | 4.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 3149 | 正達 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 18.012422360248447 | 4.395604395604402 | 44 | 68.18 | 3.02 | 38 | 63.16 | 4.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 2409 | 友達 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 21.598272138228936 | -3.7606837606837695 | 44 | 68.18 | 3.02 | 38 | 63.16 | 4.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 2484 | 希華 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 17.298187808896202 | 40.15748031496065 | 25 | 68.00 | 1.02 | 22 | 59.09 | -0.29 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 5426 | 振發 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 16.795069337442214 | 39.08256880733945 | 25 | 68.00 | 1.02 | 22 | 59.09 | -0.29 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 4958 | 臻鼎-KY | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 21.361058601134218 | 30.355329949238573 | 25 | 68.00 | 1.02 | 22 | 59.09 | -0.29 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 6156 | 松上 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 19.070904645476784 | 24.871794871794872 | 25 | 68.00 | 1.02 | 22 | 59.09 | -0.29 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 8358 | 金居 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 29.629629629629626 | 23.893805309734507 | 25 | 68.00 | 1.02 | 22 | 59.09 | -0.29 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 3484 | 崧騰 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 19.13513513513514 | 22.444444444444443 | 25 | 68.00 | 1.02 | 22 | 59.09 | -0.29 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 2882 | 國泰金 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 14.925373134328357 | 22.35169491525424 | 25 | 68.00 | 1.02 | 22 | 59.09 | -0.29 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 2332 | 友訊 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 27.707006369426757 | 21.148036253776436 | 25 | 68.00 | 1.02 | 22 | 59.09 | -0.29 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 6488 | 環球晶 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 41.221374045801525 | 27.586206896551737 | 2 | 0.00 | -9.21 | 2 | 0.00 | -12.54 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 2344 | 華邦電 | memory | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 39.616613418530356 | 21.72701949860725 | 2 | 0.00 | -9.21 | 2 | 0.00 | -12.54 | short-term TDCC overheated edge; reporting-only until more market regimes mature |

## D+5 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 2 | 0.00 | -3.38 | -3.38 | -9.21 | 2 | 0.00 | -13.08 | -17.92 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 25 | 68.00 | 3.59 | 1.88 | 1.02 | 25 | 52.00 | 2.21 | -0.16 | insufficient_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 44 | 68.18 | 4.98 | 2.30 | 3.02 | 44 | 59.09 | 4.23 | 2.31 | ok_initial_sample |

## D+10 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 2 | 0.00 | -5.91 | -5.91 | -12.54 | 2 | 0.00 | -14.51 | -20.14 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 22 | 59.09 | 2.82 | 1.82 | -0.29 | 22 | 63.64 | 3.45 | 1.01 | insufficient_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 38 | 63.16 | 7.53 | 7.06 | 4.47 | 38 | 71.05 | 8.10 | 5.47 | ok_initial_sample |
