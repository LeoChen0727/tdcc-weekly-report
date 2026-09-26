# TDCC Weekly Data Readiness

- status: `pass`
- generated_at: `2026-09-26 15:26:53 Asia/Taipei`
- as_of_date: `20260926`
- target_week: `20260921 ~ 20260925`
- selected_official_date: `20260924`
- latest_official_date: `20260924`
- previous_official_date: `20260918`
- official_date_source: `https://www.tdcc.com.tw/portal/zh/smWeb/qryStock`

正式週報只能使用 target week 內由 TDCC 官方查詢頁列出的資料日期。
若該期尚未出現，workflow 必須停止且由外部 orchestrator 稍後重試，不得沿用舊 snapshot。
