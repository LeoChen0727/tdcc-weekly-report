# TDCC Overheated Short-Term Edge

- generated_at: `2026-06-21 20:41:20 Asia/Taipei`
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
| 20260618 | 2241 | 艾姆勒 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 26.34207240948816 | 57.14285714285714 | 152 | 53.29 | 3.63 | 132 | 68.94 | 7.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 3362 | 先進光 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 28.65853658536586 | 46.52777777777777 | 152 | 53.29 | 3.63 | 132 | 68.94 | 7.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 2327 | 國巨* | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 28.266033254156774 | 45.35666218034993 | 152 | 53.29 | 3.63 | 132 | 68.94 | 7.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 2484 | 希華 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 17.298187808896202 | 40.15748031496065 | 152 | 53.29 | 3.63 | 132 | 68.94 | 7.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 5426 | 振發 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.795069337442214 | 39.08256880733945 | 152 | 53.29 | 3.63 | 132 | 68.94 | 7.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 4958 | 臻鼎-KY | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 21.361058601134218 | 30.355329949238573 | 152 | 53.29 | 3.63 | 132 | 68.94 | 7.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 6175 | 立敦 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 10.679611650485432 | 29.692832764505116 | 152 | 53.29 | 3.63 | 132 | 68.94 | 7.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 8358 | 金居 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 29.629629629629626 | 23.893805309734507 | 152 | 53.29 | 3.63 | 132 | 68.94 | 7.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 3484 | 崧騰 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 19.13513513513514 | 22.444444444444443 | 152 | 53.29 | 3.63 | 132 | 68.94 | 7.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 2882 | 國泰金 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 14.925373134328357 | 22.35169491525424 | 152 | 53.29 | 3.63 | 132 | 68.94 | 7.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 2332 | 友訊 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 27.707006369426757 | 21.148036253776436 | 152 | 53.29 | 3.63 | 132 | 68.94 | 7.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 2890 | 永豐金 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 19.69924812030075 | 20.060331825037704 | 152 | 53.29 | 3.63 | 132 | 68.94 | 7.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 3321 | 同泰 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 23.664122137404586 | 18.536585365853654 | 152 | 53.29 | 3.63 | 132 | 68.94 | 7.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 5425 | 台半 | power discrete/diodes | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 28.944504896626768 | 16.748768472906406 | 152 | 53.29 | 3.63 | 132 | 68.94 | 7.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 8096 | 擎亞 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 28.512396694214882 | 14.338235294117641 | 152 | 53.29 | 3.63 | 132 | 68.94 | 7.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 2887 | 台新新光金 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 12.86956521739131 | 13.66024518388793 | 152 | 53.29 | 3.63 | 132 | 68.94 | 7.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 2883 | 凱基金 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 10.81081081081081 | 12.226277372262784 | 152 | 53.29 | 3.63 | 132 | 68.94 | 7.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 6269 | 台郡 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 20.972644376899694 | 11.328671328671325 | 152 | 53.29 | 3.63 | 132 | 68.94 | 7.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 4707 | 磐亞 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 15.8690176322418 | 9.004739336492884 | 152 | 53.29 | 3.63 | 132 | 68.94 | 7.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 4534 | 慶騰 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 12.166666666666659 | 6.319115323854652 | 152 | 53.29 | 3.63 | 132 | 68.94 | 7.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 3149 | 正達 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 18.012422360248447 | 4.395604395604402 | 152 | 53.29 | 3.63 | 132 | 68.94 | 7.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 2409 | 友達 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 21.598272138228936 | -3.7606837606837695 | 152 | 53.29 | 3.63 | 132 | 68.94 | 7.02 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 3026 | 禾伸堂 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 29.7841726618705 | 45.016077170418 | 148 | 52.03 | 2.33 | 134 | 63.43 | 3.81 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 6432 | 今展科 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 19.20438957475994 | 41.993464052287585 | 148 | 52.03 | 2.33 | 134 | 63.43 | 3.81 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 6949 | 沛爾生醫-創 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 29.403409090909083 | 41.24031007751938 | 148 | 52.03 | 2.33 | 134 | 63.43 | 3.81 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 2484 | 希華 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 17.298187808896202 | 40.15748031496065 | 148 | 52.03 | 2.33 | 134 | 63.43 | 3.81 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 6241 | 鑫永洋 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 13.438735177865603 | 39.320388349514545 | 148 | 52.03 | 2.33 | 134 | 63.43 | 3.81 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 5426 | 振發 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 16.795069337442214 | 39.08256880733945 | 148 | 52.03 | 2.33 | 134 | 63.43 | 3.81 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 8121 | 越峰 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 22.758620689655174 | 31.85185185185184 | 148 | 52.03 | 2.33 | 134 | 63.43 | 3.81 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 2379 | 瑞昱 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 25.0381679389313 | 31.25 | 148 | 52.03 | 2.33 | 134 | 63.43 | 3.81 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 8042 | 金山電 | passive components | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 25.806451612903224 | 30.87248322147651 | 148 | 52.03 | 2.33 | 134 | 63.43 | 3.81 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 4958 | 臻鼎-KY | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 21.361058601134218 | 30.355329949238573 | 148 | 52.03 | 2.33 | 134 | 63.43 | 3.81 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 6645 | 金萬林-創 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 18.99224806201549 | 30.08474576271185 | 148 | 52.03 | 2.33 | 134 | 63.43 | 3.81 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 6654 | 天正國際 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 29.552238805970156 | 28.023598820059004 | 148 | 52.03 | 2.33 | 134 | 63.43 | 3.81 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 6585 | 鼎基 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 10.843373493975905 | 26.60550458715596 | 148 | 52.03 | 2.33 | 134 | 63.43 | 3.81 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 6156 | 松上 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 19.070904645476784 | 24.871794871794872 | 148 | 52.03 | 2.33 | 134 | 63.43 | 3.81 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 8358 | 金居 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 29.629629629629626 | 23.893805309734507 | 148 | 52.03 | 2.33 | 134 | 63.43 | 3.81 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 6465 | 威潤 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 28.519855595667877 | 22.758620689655174 | 148 | 52.03 | 2.33 | 134 | 63.43 | 3.81 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 3484 | 崧騰 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 19.13513513513514 | 22.444444444444443 | 148 | 52.03 | 2.33 | 134 | 63.43 | 3.81 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 2882 | 國泰金 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 14.925373134328357 | 22.35169491525424 | 148 | 52.03 | 2.33 | 134 | 63.43 | 3.81 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 2332 | 友訊 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 27.707006369426757 | 21.148036253776436 | 148 | 52.03 | 2.33 | 134 | 63.43 | 3.81 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 6432 | 今展科 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 19.20438957475994 | 41.993464052287585 | 42 | 45.24 | 0.92 | 40 | 60.00 | 5.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 4923 | 力士 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 33.56481481481482 | 31.735159817351622 | 42 | 45.24 | 0.92 | 40 | 60.00 | 5.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 8042 | 金山電 | passive components | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 25.806451612903224 | 30.87248322147651 | 42 | 45.24 | 0.92 | 40 | 60.00 | 5.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 6488 | 環球晶 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 41.221374045801525 | 27.586206896551737 | 42 | 45.24 | 0.92 | 40 | 60.00 | 5.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260618 | 2344 | 華邦電 | memory | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 39.616613418530356 | 21.72701949860725 | 42 | 45.24 | 0.92 | 40 | 60.00 | 5.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |

## D+5 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 42 | 45.24 | 1.73 | -1.09 | 0.92 | 42 | 40.48 | 0.56 | -0.12 | ok_initial_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 148 | 52.03 | 3.59 | 0.90 | 2.33 | 148 | 52.03 | 2.36 | 1.19 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 152 | 53.29 | 4.63 | 0.96 | 3.63 | 152 | 52.63 | 3.41 | 2.45 | ok_initial_sample |

## D+10 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 40 | 60.00 | 8.11 | 5.64 | 5.47 | 40 | 60.00 | 6.60 | 4.20 | ok_initial_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 134 | 63.43 | 5.91 | 4.57 | 3.81 | 134 | 53.73 | 3.65 | 1.82 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 132 | 68.94 | 9.14 | 6.40 | 7.02 | 132 | 60.61 | 6.43 | 4.59 | ok_initial_sample |
