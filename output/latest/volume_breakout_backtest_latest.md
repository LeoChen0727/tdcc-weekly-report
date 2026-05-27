# Volume Breakout Backtest

- generated_at: `2026-05-27 20:26:41 Asia/Taipei`
- main_price_date: `20260526`
- event_log_rows: `35243`
- rule: Features are detected on event date only. Future data is used only for D+N performance labels.
- rule: Pending horizons are excluded from mature D+N statistics.

## Summary

| group_name | group_value | sample_count | mature_d5_count | avg_return_d5 | win_rate_d5 | avg_mfe_d5 | avg_mae_d5 | mature_d10_count | avg_return_d10 | win_rate_d10 | mature_d20_count | avg_return_d20 | win_rate_d20 | sample_status | best_horizon |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_breakout_type | abnormal_volume_up | 980 | 964 | 0.2892 | 41.39 | 8.2493 | -5.4668 | 944 | 1.639 | 43.54 | 893 | 3.9638 | 45.58 | ok | D+20 |
| volume_breakout_type | loose_ma_reclaim_volume_watch | 3063 | 2840 | 0.7042 | 43.2 | 5.4541 | -3.4716 | 2778 | 1.5072 | 44.1 | 2589 | 3.6445 | 49.21 | ok | D+20 |
| volume_breakout_type | loose_platform_volume_watch | 7463 | 6932 | 0.4971 | 42.34 | 4.7156 | -3.3958 | 6748 | 1.0325 | 43.52 | 6199 | 2.5354 | 46.14 | ok | D+20 |
| volume_breakout_type | loose_right_side_volume_watch | 1086 | 984 | 0.9715 | 45.63 | 6.7652 | -4.4113 | 961 | 2.1886 | 47.14 | 874 | 5.2139 | 48.17 | ok | D+20 |
| volume_breakout_type | neckline_volume_breakout | 3450 | 3118 | 0.8926 | 44.23 | 6.9867 | -4.866 | 2930 | 2.706 | 47.27 | 2418 | 5.3213 | 49.88 | ok | D+20 |
| volume_breakout_type | platform_volume_breakout | 3518 | 3470 | 1.1457 | 44.9 | 8.5093 | -4.6337 | 3427 | 1.702 | 44.94 | 3251 | 3.6138 | 45.65 | ok | D+20 |
| volume_breakout_type | right_side_volume_attack | 3135 | 3025 | 2.1753 | 47.87 | 10.2669 | -5.18 | 2908 | 3.4602 | 49.62 | 2619 | 8.0412 | 53.57 | ok | D+20 |
| volume_breakout_type | strict_60d_volume_breakout | 2339 | 2216 | 2.0624 | 48.06 | 11.3972 | -6.3177 | 2066 | 5.2615 | 52.27 | 1677 | 9.3684 | 53.73 | ok | D+20 |
| volume_breakout_type | volume_expansion_watch | 10209 | 9996 | 0.6773 | 43.17 | 6.1434 | -4.1434 | 9788 | 1.4422 | 44.44 | 9171 | 3.0713 | 46.52 | ok | D+20 |
| volume_watch_scope | broad_watch | 11612 | 10756 | 0.5952 | 42.87 | 5.0981 | -3.5087 | 10487 | 1.2642 | 44.01 | 9662 | 3.0749 | 47.14 | ok | D+20 |
| volume_watch_scope | confirmed_attack | 6968 | 6588 | 1.0259 | 44.58 | 7.7887 | -4.7436 | 6357 | 2.1648 | 46.01 | 5669 | 4.3421 | 47.45 | ok | D+20 |
| volume_watch_scope | strict_breakout | 2339 | 2216 | 2.0624 | 48.06 | 11.3972 | -6.3177 | 2066 | 5.2615 | 52.27 | 1677 | 9.3684 | 53.73 | ok | D+20 |
| volume_watch_scope | volume_attack | 14324 | 13985 | 0.9746 | 44.06 | 7.1805 | -4.4588 | 13640 | 1.8861 | 45.48 | 12683 | 4.1604 | 47.91 | ok | D+20 |
| false_breakout_risk | False | 20752 | 19760 | 0.9534 | 43.53 | 7.2397 | -4.4404 | 19228 | 2.0661 | 45.59 | 17594 | 4.2781 | 47.57 | ok | D+20 |
| false_breakout_risk | True | 14491 | 13785 | 0.9083 | 44.79 | 6.4393 | -4.1787 | 13322 | 1.7932 | 45.47 | 12097 | 3.9293 | 48.38 | ok | D+20 |
| overheated_breakout | False | 30453 | 29036 | 0.7945 | 43.44 | 6.1744 | -3.8798 | 28252 | 1.5851 | 44.56 | 26053 | 3.4597 | 47.23 | ok | D+20 |
| overheated_breakout | True | 4790 | 4509 | 1.8388 | 47.97 | 11.6529 | -7.2505 | 4298 | 4.3818 | 51.98 | 3638 | 8.9793 | 52.67 | ok | D+20 |

