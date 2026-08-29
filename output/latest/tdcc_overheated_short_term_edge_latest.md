# TDCC Overheated Short-Term Edge

- generated_at: `2026-08-29 15:37:47 Asia/Taipei`
- source_tdcc_dataset_id: `tdcc-20260828-9c8a9567ad6e0120`
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
| 20260828 | 2426 | 鼎元 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.90997566909975 | 44.2942942942943 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 8103 | 瀚荃 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 15.42553191489362 | 37.51584283903675 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 1815 | 富喬 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 12.05357142857142 | 37.158469945355186 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 3543 | 州巧 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 23.863636363636353 | 35.91022443890275 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 3234 | 光環 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 20.198675496688743 | 32.967032967032964 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 2489 | 瑞軒 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 12.762973352033669 | 27.61904761904763 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 8358 | 金居 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 24.541284403669717 | 26.72112018669779 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 6547 | 高端疫苗 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.696588868940744 | 26.21359223300972 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 8039 | 台虹 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 21.808510638297875 | 26.055045871559624 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 4956 | 光鋐 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 10.463378176382655 | 23.166666666666668 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 6213 | 聯茂 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 13.450292397660824 | 21.249999999999993 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 3504 | 揚明光 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 12.296110414052697 | 20.782726045883958 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 3363 | 上詮 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.83333333333332 | 19.62457337883958 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 6782 | 視陽 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 19.554455445544548 | 19.259259259259267 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 2301 | 光寶科 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 21.647509578544067 | 18.913857677902612 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 3374 | 精材 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 25.938009787928216 | 18.76923076923076 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 6168 | 宏齊 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 13.806706114398427 | 17.038539553752543 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 3105 | 穩懋 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 17.694369973190337 | 16.13756613756614 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 6147 | 頎邦 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.61341853035143 | 15.873015873015884 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 6269 | 台郡 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 20.192307692307686 | 14.155251141552515 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 2033 | 佳大 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.59090909090908 | 13.49557522123892 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 2313 | 華通 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 12.880562060889922 | 11.832946635730867 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 2481 | 強茂 | power discrete/diodes | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 15.789473684210531 | 11.594202898550732 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 3491 | 昇達科 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 17.96875 | 9.818181818181815 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 1303 | 南亞 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 14.84375 | 6.265060240963849 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 1597 | 直得 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 14.28571428571428 | 5.923344947735187 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 3189 | 景碩 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 10.850801479654738 | 4.292343387470998 | 87 | 55.17 | 0.93 | 79 | 50.63 | -0.16 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 2426 | 鼎元 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 16.90997566909975 | 44.2942942942943 | 52 | 59.62 | 0.56 | 49 | 48.98 | -2.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 8103 | 瀚荃 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 15.42553191489362 | 37.51584283903675 | 52 | 59.62 | 0.56 | 49 | 48.98 | -2.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 1815 | 富喬 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 12.05357142857142 | 37.158469945355186 | 52 | 59.62 | 0.56 | 49 | 48.98 | -2.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 3543 | 州巧 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 23.863636363636353 | 35.91022443890275 | 52 | 59.62 | 0.56 | 49 | 48.98 | -2.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 8358 | 金居 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 24.541284403669717 | 26.72112018669779 | 52 | 59.62 | 0.56 | 49 | 48.98 | -2.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 6547 | 高端疫苗 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 16.696588868940744 | 26.21359223300972 | 52 | 59.62 | 0.56 | 49 | 48.98 | -2.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 8039 | 台虹 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 21.808510638297875 | 26.055045871559624 | 52 | 59.62 | 0.56 | 49 | 48.98 | -2.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 6727 | 亞泰金屬 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 21.218961625282162 | 24.305555555555557 | 52 | 59.62 | 0.56 | 49 | 48.98 | -2.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 6213 | 聯茂 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 13.450292397660824 | 21.249999999999993 | 52 | 59.62 | 0.56 | 49 | 48.98 | -2.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260828 | 8358 | 金居 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 24.541284403669717 | 26.72112018669779 | 7 | 42.86 | 1.19 | 6 | 33.33 | -4.50 | short-term TDCC overheated edge; reporting-only until more market regimes mature |

## D+5 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 7 | 42.86 | 3.78 | -1.36 | 1.19 | 7 | 28.57 | -1.42 | -3.49 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 52 | 59.62 | 2.04 | 1.36 | 0.56 | 52 | 50.00 | 0.31 | -0.98 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 87 | 55.17 | 2.42 | 0.37 | 0.93 | 87 | 50.57 | 1.00 | -0.34 | ok_initial_sample |

## D+10 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 6 | 33.33 | -1.12 | -5.91 | -4.50 | 6 | 33.33 | -5.84 | -8.64 | insufficient_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 49 | 48.98 | -1.65 | -0.87 | -2.47 | 49 | 48.98 | -1.44 | -2.01 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 79 | 50.63 | 1.11 | 1.16 | -0.16 | 79 | 53.16 | 1.54 | 0.44 | ok_initial_sample |
