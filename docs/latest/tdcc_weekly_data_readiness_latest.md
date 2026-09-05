# TDCC Weekly Data Readiness

- status: `pass`
- generated_at: `2026-09-05 15:26:30 Asia/Taipei`
- as_of_date: `20260905`
- target_week: `20260831 ~ 20260904`
- selected_official_date: `20260904`
- latest_official_date: `20260904`
- previous_official_date: `20260828`
- official_date_source: `https://www.tdcc.com.tw/portal/zh/smWeb/qryStock`

正式週報只能使用 target week 內由 TDCC 官方查詢頁列出的資料日期。
若該期尚未出現，workflow 必須停止且由外部 orchestrator 稍後重試，不得沿用舊 snapshot。
