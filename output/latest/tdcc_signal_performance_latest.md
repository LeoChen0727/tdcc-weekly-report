# TDCC 訊號績效追蹤報告

- 產生時間：`2026-05-19 16:40:11 Asia/Taipei`
- 最新 TDCC signal 批次日期：`20260515`
- signal log：`output/history/tdcc_signals/tdcc_signal_log.csv`
- performance csv：`output/history/tdcc_signals/tdcc_signal_performance.csv`

## 1. 本週 TDCC 入榜股票清單摘要

| signal_date | code | name | signal_type | threshold_group | rank | current_pct | previous_pct | weekly_change_pct | is_consecutive_2w | consecutive_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260515 | 3450 | 聯鈞 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 1 | +45.76% | +37.06% | +34.78% | True | 51.50 |
| 20260515 | 3006 | 晶豪科 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 2 | +56.69% | +49.64% | +28.20% | True | 39.43 |
| 20260515 | 3481 | 群創 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 3 | +47.34% | +44.49% | +11.41% | True | 38.47 |
| 20260515 | 8042 | 金山電 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 4 | +71.04% | +69.22% | +7.28% | True | 37.61 |
| 20260515 | 2492 | 華新科 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 5 | +66.41% | +61.35% | +20.23% | True | 36.23 |
| 20260515 | 3048 | 益登 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 6 | +51.82% | +43.64% | +32.73% | True | 35.75 |
| 20260515 | 6173 | 信昌電 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 7 | +66.45% | +63.13% | +13.30% | True | 35.40 |
| 20260515 | 2481 | 強茂 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 8 | +62.61% | +54.69% | +31.70% | True | 33.95 |
| 20260515 | 3624 | 光頡 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 9 | +54.26% | +47.38% | +27.52% | True | 32.51 |
| 20260515 | 2344 | 華邦電 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 10 | +70.67% | +66.84% | +15.34% | True | 27.74 |
| 20260515 | 5464 | 霖宏 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 11 | +64.75% | +62.43% | +9.28% | True | 26.25 |
| 20260515 | 5351 | 鈺創 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 12 | +32.51% | +29.50% | +12.03% | True | 26.10 |
| 20260515 | 3305 | 昇貿 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 13 | +44.68% | +40.87% | +15.26% | True | 23.98 |
| 20260515 | 3707 | 漢磊 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 14 | +51.38% | +46.71% | +18.69% | True | 23.53 |
| 20260515 | 3033 | 威健 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 15 | +38.73% | +36.12% | +10.44% | True | 23.47 |
| 20260515 | 4906 | 正文 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 16 | +25.99% | +23.83% | +8.65% | True | 17.87 |
| 20260515 | 2355 | 敬鵬 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 17 | +42.94% | +40.91% | +8.10% | True | 15.97 |
| 20260515 | 8390 | 金益鼎 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 18 | +46.13% | +42.94% | +12.73% | True | 15.37 |
| 20260515 | 6285 | 啟碁 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 19 | +64.20% | +63.16% | +4.18% | True | 14.98 |
| 20260515 | 3591 | 艾笛森 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 20 | +48.44% | +47.31% | +4.53% | True | 11.59 |
| 20260515 | 3450 | 聯鈞 | weekly_change_top20 | over_1000 | 1 | +43.04% | +33.10% | +9.94% | False | 0.00 |
| 20260515 | 4931 | 新盛力 | weekly_change_top20 | over_1000 | 2 | +18.51% | +10.21% | +8.30% | False | 0.00 |
| 20260515 | 3048 | 益登 | weekly_change_top20 | over_1000 | 3 | +49.29% | +40.99% | +8.30% | False | 0.00 |
| 20260515 | 2481 | 強茂 | weekly_change_top20 | over_1000 | 4 | +59.10% | +51.43% | +7.67% | False | 0.00 |
| 20260515 | 3131 | 弘塑 | weekly_change_top20 | over_1000 | 5 | +35.60% | +28.70% | +6.90% | False | 0.00 |
| 20260515 | 9960 | 邁達康 | weekly_change_top20 | over_1000 | 6 | +60.10% | +53.60% | +6.50% | False | 0.00 |
| 20260515 | 3006 | 晶豪科 | weekly_change_top20 | over_1000 | 7 | +52.42% | +46.25% | +6.17% | False | 0.00 |
| 20260515 | 3624 | 光頡 | weekly_change_top20 | over_1000 | 8 | +49.22% | +43.40% | +5.82% | False | 0.00 |
| 20260515 | 3498 | 陽程 | weekly_change_top20 | over_1000 | 9 | +46.04% | +40.43% | +5.61% | False | 0.00 |
| 20260515 | 2492 | 華新科 | weekly_change_top20 | over_1000 | 10 | +64.54% | +59.32% | +5.22% | False | 0.00 |
| 20260515 | 8028 | 昇陽半導體 | weekly_change_top20 | over_1000 | 11 | +39.90% | +34.90% | +5.00% | False | 0.00 |
| 20260515 | 4966 | 譜瑞-KY | weekly_change_top20 | over_1000 | 12 | +30.22% | +25.39% | +4.83% | False | 0.00 |
| 20260515 | 3707 | 漢磊 | weekly_change_top20 | over_1000 | 13 | +50.04% | +45.43% | +4.61% | False | 0.00 |
| 20260515 | 5439 | 高技 | weekly_change_top20 | over_1000 | 14 | +40.79% | +36.44% | +4.35% | False | 0.00 |
| 20260515 | 2344 | 華邦電 | weekly_change_top20 | over_1000 | 15 | +69.42% | +65.61% | +3.81% | False | 0.00 |
| 20260515 | 5464 | 霖宏 | weekly_change_top20 | over_1000 | 16 | +58.05% | +54.28% | +3.77% | False | 0.00 |
| 20260515 | 4744 | 皇將 | weekly_change_top20 | over_1000 | 17 | +33.19% | +29.48% | +3.71% | False | 0.00 |
| 20260515 | 3490 | 單井 | weekly_change_top20 | over_1000 | 18 | +17.76% | +14.09% | +3.67% | False | 0.00 |
| 20260515 | 1708 | 東鹼 | weekly_change_top20 | over_1000 | 19 | +43.13% | +39.82% | +3.31% | False | 0.00 |
| 20260515 | 2363 | 矽統 | weekly_change_top20 | over_1000 | 20 | +31.76% | +28.47% | +3.29% | False | 0.00 |
| 20260515 | 4966 | 譜瑞-KY | weekly_change_top20 | over_400 | 1 | +46.16% | +34.46% | +11.70% | False | 0.00 |
| 20260515 | 3624 | 光頡 | weekly_change_top20 | over_400 | 2 | +58.62% | +49.91% | +8.71% | False | 0.00 |
| 20260515 | 2481 | 強茂 | weekly_change_top20 | over_400 | 3 | +65.63% | +57.62% | +8.01% | False | 0.00 |
| 20260515 | 3450 | 聯鈞 | weekly_change_top20 | over_400 | 4 | +49.03% | +41.32% | +7.71% | False | 0.00 |
| 20260515 | 3048 | 益登 | weekly_change_top20 | over_400 | 5 | +54.64% | +47.07% | +7.57% | False | 0.00 |
| 20260515 | 3006 | 晶豪科 | weekly_change_top20 | over_400 | 6 | +60.81% | +53.60% | +7.21% | False | 0.00 |
| 20260515 | 3498 | 陽程 | weekly_change_top20 | over_400 | 7 | +51.96% | +45.03% | +6.93% | False | 0.00 |
| 20260515 | 4931 | 新盛力 | weekly_change_top20 | over_400 | 8 | +31.16% | +24.34% | +6.82% | False | 0.00 |
| 20260515 | 8114 | 振樺電 | weekly_change_top20 | over_400 | 9 | +50.81% | +44.92% | +5.89% | False | 0.00 |
| 20260515 | 8028 | 昇陽半導體 | weekly_change_top20 | over_400 | 10 | +51.67% | +45.92% | +5.75% | False | 0.00 |
| 20260515 | 2492 | 華新科 | weekly_change_top20 | over_400 | 11 | +68.63% | +63.20% | +5.43% | False | 0.00 |
| 20260515 | 6831 | 邁科 | weekly_change_top20 | over_400 | 12 | +62.01% | +57.41% | +4.60% | False | 0.00 |
| 20260515 | 3707 | 漢磊 | weekly_change_top20 | over_400 | 13 | +52.67% | +48.13% | +4.54% | False | 0.00 |
| 20260515 | 6173 | 信昌電 | weekly_change_top20 | over_400 | 14 | +69.34% | +65.16% | +4.18% | False | 0.00 |
| 20260515 | 3135 | 凌航 | weekly_change_top20 | over_400 | 15 | +56.99% | +52.82% | +4.17% | False | 0.00 |
| 20260515 | 2438 | 翔耀 | weekly_change_top20 | over_400 | 16 | +58.51% | +54.66% | +3.85% | False | 0.00 |
| 20260515 | 2344 | 華邦電 | weekly_change_top20 | over_400 | 17 | +72.17% | +68.33% | +3.84% | False | 0.00 |
| 20260515 | 8261 | 富鼎 | weekly_change_top20 | over_400 | 18 | +48.84% | +45.12% | +3.72% | False | 0.00 |
| 20260515 | 3305 | 昇貿 | weekly_change_top20 | over_400 | 19 | +48.07% | +44.41% | +3.66% | False | 0.00 |
| 20260515 | 6265 | 方土昶 | weekly_change_top20 | over_400 | 20 | +49.27% | +45.63% | +3.64% | False | 0.00 |
| 20260515 | 3048 | 益登 | weekly_change_top20 | over_600 | 1 | +52.09% | +44.16% | +7.93% | False | 0.00 |
| 20260515 | 2481 | 強茂 | weekly_change_top20 | over_600 | 2 | +64.02% | +56.09% | +7.93% | False | 0.00 |
| 20260515 | 3450 | 聯鈞 | weekly_change_top20 | over_600 | 3 | +46.62% | +38.80% | +7.82% | False | 0.00 |
| 20260515 | 3006 | 晶豪科 | weekly_change_top20 | over_600 | 4 | +58.79% | +51.00% | +7.79% | False | 0.00 |
| 20260515 | 3624 | 光頡 | weekly_change_top20 | over_600 | 5 | +56.02% | +49.00% | +7.02% | False | 0.00 |
| 20260515 | 4966 | 譜瑞-KY | weekly_change_top20 | over_600 | 6 | +37.44% | +30.70% | +6.74% | False | 0.00 |
| 20260515 | 8028 | 昇陽半導體 | weekly_change_top20 | over_600 | 7 | +45.91% | +40.06% | +5.85% | False | 0.00 |
| 20260515 | 3498 | 陽程 | weekly_change_top20 | over_600 | 8 | +48.71% | +43.34% | +5.37% | False | 0.00 |
| 20260515 | 8261 | 富鼎 | weekly_change_top20 | over_600 | 9 | +46.77% | +41.70% | +5.07% | False | 0.00 |
| 20260515 | 2492 | 華新科 | weekly_change_top20 | over_600 | 10 | +67.02% | +62.03% | +4.99% | False | 0.00 |
| 20260515 | 4931 | 新盛力 | weekly_change_top20 | over_600 | 11 | +27.25% | +22.59% | +4.66% | False | 0.00 |
| 20260515 | 3707 | 漢磊 | weekly_change_top20 | over_600 | 12 | +51.65% | +47.14% | +4.51% | False | 0.00 |
| 20260515 | 3305 | 昇貿 | weekly_change_top20 | over_600 | 13 | +46.78% | +42.28% | +4.50% | False | 0.00 |
| 20260515 | 6831 | 邁科 | weekly_change_top20 | over_600 | 14 | +53.75% | +49.32% | +4.43% | False | 0.00 |
| 20260515 | 9960 | 邁達康 | weekly_change_top20 | over_600 | 15 | +73.01% | +68.70% | +4.31% | False | 0.00 |
| 20260515 | 3526 | 凡甲 | weekly_change_top20 | over_600 | 16 | +49.73% | +45.47% | +4.26% | False | 0.00 |
| 20260515 | 2438 | 翔耀 | weekly_change_top20 | over_600 | 17 | +55.58% | +51.46% | +4.12% | False | 0.00 |
| 20260515 | 2344 | 華邦電 | weekly_change_top20 | over_600 | 18 | +70.95% | +67.10% | +3.85% | False | 0.00 |
| 20260515 | 3357 | 臺慶科 | weekly_change_top20 | over_600 | 19 | +56.82% | +53.09% | +3.73% | False | 0.00 |
| 20260515 | 8114 | 振樺電 | weekly_change_top20 | over_600 | 20 | +42.40% | +38.80% | +3.60% | False | 0.00 |
| 20260515 | 3450 | 聯鈞 | weekly_change_top20 | over_800 | 1 | +44.33% | +35.02% | +9.31% | False | 0.00 |
| 20260515 | 3048 | 益登 | weekly_change_top20 | over_800 | 2 | +51.28% | +42.35% | +8.93% | False | 0.00 |
| 20260515 | 9960 | 邁達康 | weekly_change_top20 | over_800 | 3 | +65.29% | +56.40% | +8.89% | False | 0.00 |
| 20260515 | 2481 | 強茂 | weekly_change_top20 | over_800 | 4 | +61.70% | +53.61% | +8.09% | False | 0.00 |
| 20260515 | 3006 | 晶豪科 | weekly_change_top20 | over_800 | 5 | +54.74% | +47.71% | +7.03% | False | 0.00 |
| 20260515 | 8028 | 昇陽半導體 | weekly_change_top20 | over_800 | 6 | +43.53% | +37.44% | +6.09% | False | 0.00 |
| 20260515 | 3624 | 光頡 | weekly_change_top20 | over_800 | 7 | +53.17% | +47.20% | +5.97% | False | 0.00 |
| 20260515 | 3305 | 昇貿 | weekly_change_top20 | over_800 | 8 | +44.39% | +39.03% | +5.36% | False | 0.00 |
| 20260515 | 3707 | 漢磊 | weekly_change_top20 | over_800 | 9 | +51.16% | +46.13% | +5.03% | False | 0.00 |
| 20260515 | 4966 | 譜瑞-KY | weekly_change_top20 | over_800 | 10 | +31.35% | +26.46% | +4.89% | False | 0.00 |
| 20260515 | 2492 | 華新科 | weekly_change_top20 | over_800 | 11 | +65.46% | +60.87% | +4.59% | False | 0.00 |
| 20260515 | 8390 | 金益鼎 | weekly_change_top20 | over_800 | 12 | +45.68% | +41.10% | +4.58% | False | 0.00 |
| 20260515 | 2438 | 翔耀 | weekly_change_top20 | over_800 | 13 | +53.58% | +49.28% | +4.30% | False | 0.00 |
| 20260515 | 3498 | 陽程 | weekly_change_top20 | over_800 | 14 | +47.64% | +43.34% | +4.30% | False | 0.00 |
| 20260515 | 3455 | 由田 | weekly_change_top20 | over_800 | 15 | +20.81% | +16.57% | +4.24% | False | 0.00 |
| 20260515 | 4127 | 天良 | weekly_change_top20 | over_800 | 16 | +60.57% | +56.39% | +4.18% | False | 0.00 |
| 20260515 | 8261 | 富鼎 | weekly_change_top20 | over_800 | 17 | +44.42% | +40.55% | +3.87% | False | 0.00 |
| 20260515 | 2344 | 華邦電 | weekly_change_top20 | over_800 | 18 | +70.15% | +66.31% | +3.84% | False | 0.00 |
| 20260515 | 3357 | 臺慶科 | weekly_change_top20 | over_800 | 19 | +50.57% | +46.80% | +3.77% | False | 0.00 |
| 20260515 | 1708 | 東鹼 | weekly_change_top20 | over_800 | 20 | +46.37% | +42.65% | +3.72% | False | 0.00 |

## 2.1 D+1 表現排行

| signal_date | code | name | signal_type | threshold_group | signal_close | d1_close | d1_return_pct | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260515 | 6285 | 啟碁 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 260.00 | 286.00 | +10.00% | partial_1d |
| 20260515 | 4127 | 天良 | weekly_change_top20 | over_800 | 39.10 | 43.00 | +9.97% | partial_1d |
| 20260515 | 3624 | 光頡 | weekly_change_top20 | over_1000 | 76.20 | 83.80 | +9.97% | partial_1d |
| 20260515 | 3624 | 光頡 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 76.20 | 83.80 | +9.97% | partial_1d |
| 20260515 | 3624 | 光頡 | weekly_change_top20 | over_600 | 76.20 | 83.80 | +9.97% | partial_1d |
| 20260515 | 3624 | 光頡 | weekly_change_top20 | over_800 | 76.20 | 83.80 | +9.97% | partial_1d |
| 20260515 | 3624 | 光頡 | weekly_change_top20 | over_400 | 76.20 | 83.80 | +9.97% | partial_1d |
| 20260515 | 2355 | 敬鵬 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 52.50 | 57.70 | +9.90% | partial_1d |
| 20260515 | 2481 | 強茂 | weekly_change_top20 | over_1000 | 117.50 | 129.00 | +9.79% | partial_1d |
| 20260515 | 2481 | 強茂 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 117.50 | 129.00 | +9.79% | partial_1d |
| 20260515 | 2481 | 強茂 | weekly_change_top20 | over_800 | 117.50 | 129.00 | +9.79% | partial_1d |
| 20260515 | 2481 | 強茂 | weekly_change_top20 | over_600 | 117.50 | 129.00 | +9.79% | partial_1d |
| 20260515 | 2481 | 強茂 | weekly_change_top20 | over_400 | 117.50 | 129.00 | +9.79% | partial_1d |
| 20260515 | 8042 | 金山電 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 98.10 | 107.50 | +9.58% | partial_1d |
| 20260515 | 2438 | 翔耀 | weekly_change_top20 | over_400 | 20.65 | 22.20 | +7.51% | partial_1d |
| 20260515 | 2438 | 翔耀 | weekly_change_top20 | over_600 | 20.65 | 22.20 | +7.51% | partial_1d |
| 20260515 | 2438 | 翔耀 | weekly_change_top20 | over_800 | 20.65 | 22.20 | +7.51% | partial_1d |
| 20260515 | 3481 | 群創 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 36.10 | 38.70 | +7.20% | partial_1d |
| 20260515 | 6173 | 信昌電 | consecutive_2w_all_thresholds | all_400_600_800_1000 | 155.00 | 166.00 | +7.10% | partial_1d |
| 20260515 | 6173 | 信昌電 | weekly_change_top20 | over_400 | 155.00 | 166.00 | +7.10% | partial_1d |

## 2.2 D+2 表現排行

目前沒有可用資料。

## 2.5 D+5 表現排行

目前沒有可用資料。

## 2.10 D+10 表現排行

目前沒有可用資料。

## 2.20 D+20 表現排行

目前沒有可用資料。

## 3. 四級距同步入榜股票的表現

| signal_date | code | name | threshold_count | avg_d5_return_pct | avg_d10_return_pct | avg_d20_return_pct | max_return_20d | max_drawdown_20d |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260515 | 2344 | 華邦電 | 4 | - | - | - | +3.47% | -8.11% |
| 20260515 | 2481 | 強茂 | 4 | - | - | - | +9.79% | -5.11% |
| 20260515 | 2492 | 華新科 | 4 | - | - | - | +6.31% | 0.00% |
| 20260515 | 3006 | 晶豪科 | 4 | - | - | - | +0.60% | -8.96% |
| 20260515 | 3048 | 益登 | 4 | - | - | - | +7.31% | -1.96% |
| 20260515 | 3450 | 聯鈞 | 4 | - | - | - | +4.93% | -3.79% |
| 20260515 | 3498 | 陽程 | 4 | - | - | - | +3.02% | -7.05% |
| 20260515 | 3624 | 光頡 | 4 | - | - | - | +9.97% | +0.13% |
| 20260515 | 3707 | 漢磊 | 4 | - | - | - | -2.36% | -8.71% |
| 20260515 | 4966 | 譜瑞-KY | 4 | - | - | - | -2.00% | -6.25% |
| 20260515 | 8028 | 昇陽半導體 | 4 | - | - | - | -0.87% | -6.09% |

## 4. 連續兩週四級距同步增加股票的表現

| signal_date | code | name | rank | consecutive_score | signal_close | d5_return_pct | d10_return_pct | d20_return_pct | max_return_20d | max_drawdown_20d | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260515 | 3450 | 聯鈞 | 1 | 51.50 | 395.50 | - | - | - | +4.93% | -3.79% | partial_1d |
| 20260515 | 3006 | 晶豪科 | 2 | 39.43 | 251.00 | - | - | - | +0.60% | -8.96% | partial_1d |
| 20260515 | 3481 | 群創 | 3 | 38.47 | 36.10 | - | - | - | +9.14% | -4.29% | partial_1d |
| 20260515 | 8042 | 金山電 | 4 | 37.61 | 98.10 | - | - | - | +9.58% | +1.63% | partial_1d |
| 20260515 | 2492 | 華新科 | 5 | 36.23 | 206.00 | - | - | - | +6.31% | 0.00% | partial_1d |
| 20260515 | 3048 | 益登 | 6 | 35.75 | 56.10 | - | - | - | +7.31% | -1.96% | partial_1d |
| 20260515 | 6173 | 信昌電 | 7 | 35.40 | 155.00 | - | - | - | +9.03% | +4.84% | partial_1d |
| 20260515 | 2481 | 強茂 | 8 | 33.95 | 117.50 | - | - | - | +9.79% | -5.11% | partial_1d |
| 20260515 | 3624 | 光頡 | 9 | 32.51 | 76.20 | - | - | - | +9.97% | +0.13% | partial_1d |
| 20260515 | 2344 | 華邦電 | 10 | 27.74 | 129.50 | - | - | - | +3.47% | -8.11% | partial_1d |
| 20260515 | 5464 | 霖宏 | 11 | 26.25 | 57.10 | - | - | - | +7.01% | -5.78% | partial_1d |
| 20260515 | 5351 | 鈺創 | 12 | 26.10 | 87.50 | - | - | - | -0.34% | -6.17% | partial_1d |
| 20260515 | 3305 | 昇貿 | 13 | 23.98 | 138.50 | - | - | - | +1.08% | -8.30% | partial_1d |
| 20260515 | 3707 | 漢磊 | 14 | 23.53 | 80.40 | - | - | - | -2.36% | -8.71% | partial_1d |
| 20260515 | 3033 | 威健 | 15 | 23.47 | 47.90 | - | - | - | +1.77% | -2.19% | partial_1d |
| 20260515 | 4906 | 正文 | 16 | 17.87 | 39.15 | - | - | - | +3.07% | -2.43% | partial_1d |
| 20260515 | 2355 | 敬鵬 | 17 | 15.97 | 52.50 | - | - | - | +9.90% | -1.71% | partial_1d |
| 20260515 | 8390 | 金益鼎 | 18 | 15.37 | 119.50 | - | - | - | +5.02% | -2.93% | partial_1d |
| 20260515 | 6285 | 啟碁 | 19 | 14.98 | 260.00 | - | - | - | +10.00% | -2.31% | partial_1d |
| 20260515 | 3591 | 艾笛森 | 20 | 11.59 | 23.85 | - | - | - | +4.40% | -2.10% | partial_1d |

## 5. 過熱警示

### 訊號日前 5 日漲幅過大

| signal_date | code | name | signal_type | threshold_group | pre_signal_5d_return_pct | d5_return_pct | d10_return_pct | max_drawdown_10d |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260515 | 6831 | 邁科 | weekly_change_top20 | over_400 | +34.26% | - | - | -9.79% |
| 20260515 | 6831 | 邁科 | weekly_change_top20 | over_600 | +34.26% | - | - | -9.79% |
| 20260515 | 3048 | 益登 | weekly_change_top20 | over_400 | +32.31% | - | - | -1.96% |
| 20260515 | 3048 | 益登 | weekly_change_top20 | over_1000 | +32.31% | - | - | -1.96% |
| 20260515 | 3048 | 益登 | consecutive_2w_all_thresholds | all_400_600_800_1000 | +32.31% | - | - | -1.96% |
| 20260515 | 3048 | 益登 | weekly_change_top20 | over_600 | +32.31% | - | - | -1.96% |
| 20260515 | 3048 | 益登 | weekly_change_top20 | over_800 | +32.31% | - | - | -1.96% |
| 20260515 | 2492 | 華新科 | weekly_change_top20 | over_400 | +32.05% | - | - | 0.00% |
| 20260515 | 2492 | 華新科 | consecutive_2w_all_thresholds | all_400_600_800_1000 | +32.05% | - | - | 0.00% |
| 20260515 | 2492 | 華新科 | weekly_change_top20 | over_600 | +32.05% | - | - | 0.00% |
| 20260515 | 2492 | 華新科 | weekly_change_top20 | over_800 | +32.05% | - | - | 0.00% |
| 20260515 | 2492 | 華新科 | weekly_change_top20 | over_1000 | +32.05% | - | - | 0.00% |
| 20260515 | 8028 | 昇陽半導體 | weekly_change_top20 | over_800 | +27.21% | - | - | -6.09% |
| 20260515 | 8028 | 昇陽半導體 | weekly_change_top20 | over_1000 | +27.21% | - | - | -6.09% |
| 20260515 | 8028 | 昇陽半導體 | weekly_change_top20 | over_400 | +27.21% | - | - | -6.09% |
| 20260515 | 8028 | 昇陽半導體 | weekly_change_top20 | over_600 | +27.21% | - | - | -6.09% |
| 20260515 | 3006 | 晶豪科 | consecutive_2w_all_thresholds | all_400_600_800_1000 | +24.26% | - | - | -8.96% |
| 20260515 | 3006 | 晶豪科 | weekly_change_top20 | over_800 | +24.26% | - | - | -8.96% |
| 20260515 | 3006 | 晶豪科 | weekly_change_top20 | over_600 | +24.26% | - | - | -8.96% |
| 20260515 | 3006 | 晶豪科 | weekly_change_top20 | over_400 | +24.26% | - | - | -8.96% |
| 20260515 | 3006 | 晶豪科 | weekly_change_top20 | over_1000 | +24.26% | - | - | -8.96% |
| 20260515 | 3481 | 群創 | consecutive_2w_all_thresholds | all_400_600_800_1000 | +22.79% | - | - | -4.29% |
| 20260515 | 3135 | 凌航 | weekly_change_top20 | over_400 | +22.03% | - | - | -7.64% |
| 20260515 | 2344 | 華邦電 | consecutive_2w_all_thresholds | all_400_600_800_1000 | +21.03% | - | - | -8.11% |
| 20260515 | 2344 | 華邦電 | weekly_change_top20 | over_800 | +21.03% | - | - | -8.11% |
| 20260515 | 2344 | 華邦電 | weekly_change_top20 | over_600 | +21.03% | - | - | -8.11% |
| 20260515 | 2344 | 華邦電 | weekly_change_top20 | over_1000 | +21.03% | - | - | -8.11% |
| 20260515 | 2344 | 華邦電 | weekly_change_top20 | over_400 | +21.03% | - | - | -8.11% |
| 20260515 | 3305 | 昇貿 | weekly_change_top20 | over_800 | +20.43% | - | - | -8.30% |
| 20260515 | 3305 | 昇貿 | consecutive_2w_all_thresholds | all_400_600_800_1000 | +20.43% | - | - | -8.30% |

### 訊號日後隔日明顯轉弱

| signal_date | code | name | signal_type | threshold_group | d1_return_pct | d5_return_pct | max_drawdown_10d | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260515 | 4966 | 譜瑞-KY | weekly_change_top20 | over_400 | -5.37% | - | -6.25% | partial_1d |
| 20260515 | 4966 | 譜瑞-KY | weekly_change_top20 | over_1000 | -5.37% | - | -6.25% | partial_1d |
| 20260515 | 4966 | 譜瑞-KY | weekly_change_top20 | over_600 | -5.37% | - | -6.25% | partial_1d |
| 20260515 | 4966 | 譜瑞-KY | weekly_change_top20 | over_800 | -5.37% | - | -6.25% | partial_1d |
| 20260515 | 3707 | 漢磊 | weekly_change_top20 | over_400 | -4.48% | - | -8.71% | partial_1d |
| 20260515 | 3707 | 漢磊 | weekly_change_top20 | over_600 | -4.48% | - | -8.71% | partial_1d |
| 20260515 | 3707 | 漢磊 | weekly_change_top20 | over_1000 | -4.48% | - | -8.71% | partial_1d |
| 20260515 | 3707 | 漢磊 | consecutive_2w_all_thresholds | all_400_600_800_1000 | -4.48% | - | -8.71% | partial_1d |
| 20260515 | 3707 | 漢磊 | weekly_change_top20 | over_800 | -4.48% | - | -8.71% | partial_1d |
| 20260515 | 3135 | 凌航 | weekly_change_top20 | over_400 | -3.70% | - | -7.64% | partial_1d |
| 20260515 | 9960 | 邁達康 | weekly_change_top20 | over_1000 | -3.31% | - | -4.90% | partial_1d |
| 20260515 | 9960 | 邁達康 | weekly_change_top20 | over_800 | -3.31% | - | -4.90% | partial_1d |
| 20260515 | 9960 | 邁達康 | weekly_change_top20 | over_600 | -3.31% | - | -4.90% | partial_1d |
| 20260515 | 3131 | 弘塑 | weekly_change_top20 | over_1000 | -3.31% | - | -7.14% | partial_1d |
| 20260515 | 8028 | 昇陽半導體 | weekly_change_top20 | over_600 | -3.13% | - | -6.09% | partial_1d |
| 20260515 | 8028 | 昇陽半導體 | weekly_change_top20 | over_1000 | -3.13% | - | -6.09% | partial_1d |
| 20260515 | 8028 | 昇陽半導體 | weekly_change_top20 | over_800 | -3.13% | - | -6.09% | partial_1d |
| 20260515 | 8028 | 昇陽半導體 | weekly_change_top20 | over_400 | -3.13% | - | -6.09% | partial_1d |
| 20260515 | 3498 | 陽程 | weekly_change_top20 | over_1000 | -3.02% | - | -7.05% | partial_1d |
| 20260515 | 3498 | 陽程 | weekly_change_top20 | over_400 | -3.02% | - | -7.05% | partial_1d |
| 20260515 | 3498 | 陽程 | weekly_change_top20 | over_600 | -3.02% | - | -7.05% | partial_1d |
| 20260515 | 3498 | 陽程 | weekly_change_top20 | over_800 | -3.02% | - | -7.05% | partial_1d |

## 6. 統計摘要

### 各 threshold_group 統計

| threshold_group | signal_count | avg_d5_return_pct | avg_d10_return_pct | avg_d20_return_pct | win_rate_d5 | win_rate_d10 | win_rate_d20 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| all_400_600_800_1000 | 20 | - | - | - | 0.00% | 0.00% | 0.00% |
| over_1000 | 20 | - | - | - | 0.00% | 0.00% | 0.00% |
| over_400 | 20 | - | - | - | 0.00% | 0.00% | 0.00% |
| over_600 | 20 | - | - | - | 0.00% | 0.00% | 0.00% |
| over_800 | 20 | - | - | - | 0.00% | 0.00% | 0.00% |



### 各 signal_type 統計

| signal_type | signal_count | avg_d5_return_pct | avg_d10_return_pct | avg_d20_return_pct | win_rate_d5 | win_rate_d10 | win_rate_d20 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| consecutive_2w_all_thresholds | 20 | - | - | - | 0.00% | 0.00% | 0.00% |
| weekly_change_top20 | 80 | - | - | - | 0.00% | 0.00% | 0.00% |



### 四級距同步入榜 vs 單一/部分級距

| sync_type | signal_count | avg_d5_return_pct | avg_d10_return_pct | avg_d20_return_pct |
| --- | --- | --- | --- | --- |
| four_threshold_sync | 11 | - | - | - |
| single_or_partial | 22 | - | - | - |



### 連續兩週同步增加 vs 其他 signal

| group | signal_count | avg_d5_return_pct | avg_d10_return_pct | avg_d20_return_pct |
| --- | --- | --- | --- | --- |
| consecutive_2w_all_thresholds | 20 | - | - | - |
| other_signals | 80 | - | - | - |

## 7. 使用說明

- 這份報告只用來驗證 TDCC 週增訊號是否有後續報酬，不是直接買賣建議。
- `signal_close` 使用 signal 日期當天或之前最近一個可用交易日收盤價。
- D+1 / D+2 / D+5 / D+10 / D+20 使用後續第 N 個交易日收盤價。
- `max_return_*d` 使用 signal 後 N 個交易日內最高價計算。
- `max_drawdown_*d` 使用 signal 後 N 個交易日內最低價計算。
- 若每日股價資料不足，status 會顯示 partial 或 pending。
