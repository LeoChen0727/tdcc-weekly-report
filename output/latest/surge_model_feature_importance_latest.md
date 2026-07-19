# Surge Model Feature Importance Latest

generated_at: 2026-07-19 11:20:06 Asia/Taipei
source_tdcc_dataset_id: tdcc-20260717-98c564c5bc4ab725

使用可解釋條件統計，比較 mature surge samples 與非暴漲對照母體。樣本不足時不得下正式結論。

| condition_name | sample_count | surge_count | surge_rate | baseline_surge_rate | lift_vs_baseline | avg_future_max_ret_5d | avg_future_max_ret_10d | avg_mae_before_surge | false_positive_rate | precision | recall | control_sample_count | sample_status | source_tdcc_dataset_id |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| relative_ret_20d_vs_twse > 0 | 78323 | 11826 | 0.15099013061297448 | 0.07900638472567738 | 1.9111130212733567 | 7.4886899619793805 | 11.506748524197128 | -6.434600748272272 | 0.8490098693870255 | 0.15099013061297448 | 0.4585853885528153 | 4727 | ok | tdcc-20260717-98c564c5bc4ab725 |
| volume_ratio_20d between 1.0 and 1.8 | 74544 | 5898 | 0.07912105602060528 | 0.07900638472567738 | 1.0014514180762233 | 5.294091195502217 | 8.064734279254369 | -4.9581112645626435 | 0.9208789439793947 | 0.07912105602060528 | 0.22871102838529547 | 4727 | ok | tdcc-20260717-98c564c5bc4ab725 |
| tdcc_consecutive_up_weeks >= 2 + price_ret_20d <= 8 | 23475 | 1372 | 0.058445154419595316 | 0.07900638472567738 | 0.7397522949888937 | 5.030145424999351 | 7.664031938435893 | -4.621476223446519 | 0.9415548455804047 | 0.058445154419595316 | 0.053203040173724216 | 4727 | ok | tdcc-20260717-98c564c5bc4ab725 |
| distance_ma20_pct between -3 and +6 | 196537 | 10066 | 0.05121681922487878 | 0.07900638472567738 | 0.6482617753326095 | 4.156674438085363 | 6.43754925060416 | -4.3635581438021545 | 0.9487831807751212 | 0.05121681922487878 | 0.39033659066232357 | 4727 | ok | tdcc-20260717-98c564c5bc4ab725 |
| low volatility compression + volume expansion | 41200 | 1129 | 0.027402912621359223 | 0.07900638472567738 | 0.3468442799465696 | 3.356338360375948 | 5.177297789745653 | -3.5031865260018766 | 0.9725970873786408 | 0.027402912621359223 | 0.04378005273770746 | 4727 | ok | tdcc-20260717-98c564c5bc4ab725 |
| consolidation_days >= 10 + narrow_range_20d | 123140 | 2909 | 0.023623517947052135 | 0.07900638472567738 | 0.2990077071502096 | 3.091514563769524 | 4.818020346485159 | -3.279523372784059 | 0.9763764820529479 | 0.023623517947052135 | 0.11280440514968203 | 4727 | ok | tdcc-20260717-98c564c5bc4ab725 |
| tdcc_leading_price + quiet_accumulation | 0 | 0 |  | 0.07900638472567738 |  |  |  |  |  |  | 0.0 | 4727 | insufficient_sample | tdcc-20260717-98c564c5bc4ab725 |
| theme_mainstream_status = emerging_theme | 0 | 0 |  | 0.07900638472567738 |  |  |  |  |  |  | 0.0 | 4727 | insufficient_sample | tdcc-20260717-98c564c5bc4ab725 |
| revenue_yoy > 20 + revenue_low_price_response | 0 | 0 |  | 0.07900638472567738 |  |  |  |  |  |  | 0.0 | 4727 | insufficient_sample | tdcc-20260717-98c564c5bc4ab725 |
| warrant_call_inflow + TDCC high_thresholds_up | 0 | 0 |  | 0.07900638472567738 |  |  |  |  |  |  | 0.0 | 4727 | insufficient_sample | tdcc-20260717-98c564c5bc4ab725 |
