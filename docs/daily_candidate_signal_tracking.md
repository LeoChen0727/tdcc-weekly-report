# Daily Candidate Signal Tracking

每日全市場候選股監測報告新增訊號追蹤與績效回測。

## Files

- `output/history/daily_signals/daily_candidate_signal_log.csv`
- `output/history/daily_signals/daily_candidate_signal_performance.csv`
- `output/latest/daily_signal_performance_summary_latest.md`
- `output/latest/daily_signal_performance_weekly_latest.md`
- `output/latest/daily_signal_performance_weekly_latest.pdf`
- `output/latest/daily_signal_performance_monthly_latest.md`
- `output/latest/daily_signal_performance_monthly_latest.pdf`

## Signal log

每一列代表某股票在某天出現某分類訊號。若同一股票同一天出現在多個分類，保留多列，不把不同分類分數混成總排名。

主要欄位包含：

- 分類與優先度
- TDCC 狀態
- 權證狀態
- 營收欄位
- 價格、均線、前高距離
- 營建/交屋認列型標記
- 大盤/櫃買 benchmark 與 market regime

## Performance

績效用 repo 內的日價歷史計算，不使用外部即時網頁補資料。

追蹤：

- D+1 / D+2 / D+5 / D+10 / D+20 收盤報酬
- MFE / MAE
- 是否跑贏 TWSE 或 TPEx benchmark
- market regime 下的分類效果

未滿 D+N 的欄位留空。

## Construction revenue recognition

營建業、建材營造、不動產開發、工程承攬等認列型產業會標示：

- `is_construction_recognition=True`
- `recognition_type=營建認列型 / 交屋認列型`

月營收 YoY 不與電子、半導體、零組件等出貨型產業同權重比較。
