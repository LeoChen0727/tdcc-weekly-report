# SURGE MODEL CHATGPT PACKET

## Metadata
- generated_at: 2026-07-05 04:59:20 Asia/Taipei
- main_price_date: 20260703
- surge_definition: surge_5d=future 5d high >= 20%; surge_10d=future 10d high >= 25%; surge_20d=future 20d high >= 35%
- feature_panel_rows: 338191
- mature_5d_count: 327551
- mature_10d_count: 316911
- mature_20d_count: 295631
- baseline_surge_rate_5d: 0.0456
- baseline_surge_rate_10d: 0.0681
- baseline_surge_rate_20d: 0.0825

## Data Availability
- feature_panel: True
- labels: True
- pre_surge_event_study: True
- non_surge_control_sample: True
- tdcc_snapshot: True
- warrant_flow_by_stock: True
- market_index_history: True

## Top Surge Precondition Candidates
| trade_date | stock_id | stock_name | theme | surge_precondition_score | surge_watch_label | tdcc_price_phase | setup_type | abm_score | tdcc_consecutive_up_weeks | price_ret_20d | distance_ma20_pct | volume_ratio_20d | theme_mainstream_status | revenue_yoy | warrant_flow_score | market_regime | risk_flags | reason_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260703 | 1737 | 臺鹽 | other | 106.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 100.00 | 10 | 1.1041009463722329 | 0.825796303578441 | 1.1081673828224434 | mainstream_leader |  |  | mild_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和 |
| 20260703 | 2204 | 中華 | other | 106.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 95.00 | 8 | 1.7825311942959 | 2.467474203678788 | 1.204466507344681 | non_mainstream_watch | 5.915786328844569 |  | mild_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和 |
| 20260703 | 2211 | 長榮鋼 | other | 106.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 95.00 | 3 | 2.008456659619462 | 2.3275542123959436 | 1.426161594704047 | mainstream_leader |  |  | mild_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和 |
| 20260703 | 2812 | 台中銀 | other | 104.0 | C_too_hot | tdcc_leading_price | quiet_accumulation | 90.00 | 2 | 5.154639175257736 | 3.304215723509296 | 1.1370874928492185 | mainstream_leader | 28.33 |  | mild_bull | too_hot_or_overextended | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和；風險:too_hot_or_overextended |
| 20260703 | 1442 | 名軒 | other | 98.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 95.00 | 5 | 2.7027027027026973 | 3.9103089964451776 | 1.4966138994576637 | mainstream_leader |  |  | mild_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和 |
| 20260703 | 2845 | 遠東銀 | other | 98.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 100.00 | 5 | 4.7808764940239 | 1.7801857585139302 | 0.5429217168977732 | mainstream_leader | 21.675436456772484 |  | mild_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260703 | 3252 | 海灣 | other | 98.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 95.00 | 7 | -0.8287292817679703 | 1.2551121139472654 | 1.2941176470588236 | mainstream_leader |  |  | mild_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和 |
| 20260703 | 3596 | 智易 | other | 98.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 85.00 | 2 | 5.053191489361697 | 4.899747709467528 | 0.7691002854206168 | non_mainstream_watch | 4.228010288725148 | 0.0 | mild_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260703 | 6504 | 南六 | other | 98.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 87.00 | 2 | -2.9451137884872858 | 0.6036217303822866 | 1.0570728628901491 | mainstream_leader |  |  | mild_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和 |
| 20260703 | 8404 | 百和興業-KY | other | 98.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 95.00 | 5 | -4.49438202247191 | 0.9501187648456089 | 1.4749607137626517 | mainstream_leader |  |  | mild_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和 |
| 20260703 | 9951 | 皇田 | other | 91.0 | A_surge_watch | tdcc_leading_price |  |  | 8 | 2.840909090909083 | 1.943114615601238 | 1.1428571428571428 |  |  |  | mild_bull |  | TDCC領先股價；靠近MA20；量能溫和 |
| 20260703 | 1339 | 昭輝 | other | 90.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 92.00 | 2 | 2.16894977168951 | 1.8318352486062173 | 0.6968536724549533 | mainstream_leader |  |  | mild_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260703 | 1615 | 大山 | other | 90.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 95.00 | 2 | -2.9001074113855996 | 0.7579135086937194 | 0.9364084633460394 | mainstream_leader |  |  | mild_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260703 | 1733 | 五鼎 | other | 90.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 92.00 | 9 | -3.0844155844155785 | 1.573798383666536 | 0.6800696769867846 | mainstream_leader |  |  | mild_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260703 | 2008 | 高興昌 | other | 90.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 100.00 | 9 | 2.6666666666666616 | 1.2574997945261845 | 0.5168077560832414 | mainstream_leader |  |  | mild_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260703 | 2528 | 皇普 | other | 90.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 85.00 | 7 | 7.294117647058829 | 3.6481418342993566 | 0.7767831877611343 | mainstream_leader |  |  | mild_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260703 | 2852 | 第一保 | other | 90.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 88.00 | 2 | -3.590664272890487 | -0.4818383988139274 | 0.6407118939678876 | mainstream_leader |  |  | mild_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260703 | 5203 | 訊連 | other | 90.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 100.00 | 4 | -3.194444444444444 | 1.544289044289049 | 0.7277678472959442 | mainstream_leader |  |  | mild_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260703 | 5523 | 豐謙 | other | 90.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 99.00 | 9 | -0.16420361247947435 | -0.04931777083676536 | 0.8041958041958042 | mainstream_leader |  |  | mild_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260703 | 5533 | 皇鼎 | other | 90.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 100.00 | 9 | 1.0676156583629748 | 1.4466869083764822 | 0.7528214179930002 | mainstream_leader |  |  | mild_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260703 | 5871 | 中租-KY | other | 90.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 88.00 | 2 | -2.1008403361344574 | -0.23549561121816165 | 0.4812583408457765 | mainstream_leader |  |  | mild_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260703 | 6115 | 鎰勝 | other | 90.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 90.00 | 3 | -2.004008016032066 | 0.6690684508491973 | 0.763541169197594 | mainstream_leader |  |  | mild_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260703 | 6283 | 淳安 | other | 90.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 100.00 | 9 | -4.545454545454552 | 0.9193480986209757 | 0.27716666319233835 | mainstream_leader |  |  | mild_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260703 | 6527 | 明達醫 | other | 90.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 100.00 | 9 | 3.1073446327683607 | 1.2412454060051203 | 0.9482758620689655 | mainstream_leader |  |  | mild_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260703 | 2017 | 官田鋼 | other | 88.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 100.00 | 8 | -3.2454361054766734 | 2.602710260271013 | 1.288337633026588 | mainstream_leader |  |  | mild_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和 |
| 20260703 | 2107 | 厚生 | other | 88.0 | C_too_hot | tdcc_leading_price | quiet_accumulation | 100.00 | 9 | -0.9596928982725572 | 0.5553931598947681 | 1.2729705342418869 | mainstream_leader |  |  | mild_bull | too_hot_or_overextended | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和；風險:too_hot_or_overextended |
| 20260703 | 2114 | 鑫永銓 | other | 88.0 | C_too_hot | tdcc_leading_price | quiet_accumulation | 100.00 | 7 | -0.9846827133479286 | 0.9762900976290068 | 1.5139631151552078 | mainstream_leader |  |  | mild_bull | too_hot_or_overextended | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和；風險:too_hot_or_overextended |
| 20260703 | 2801 | 彰銀 | other | 88.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 91.00 | 5 | 8.878504672897215 | 1.9247594050743722 | 0.3174539123759141 | mainstream_leader | 24.592717387788625 |  | mild_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260703 | 2886 | 兆豐金 | other | 88.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 91.00 | 8 | 8.076009501187652 | 1.8751749230338621 | 0.4721885712316243 | mainstream_leader | 25.5509359125496 | 0.0 | mild_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260703 | 3023 | 信邦 | other | 88.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 86.00 | 3 | 7.679999999999998 | 4.673769344428025 | 1.6807782752386429 | mainstream_leader | 17.525901573046514 | 2.0 | mild_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和 |

## Feature Importance Summary
| condition_name | sample_count | surge_count | surge_rate | baseline_surge_rate | lift_vs_baseline | avg_future_max_ret_5d | avg_future_max_ret_10d | avg_mae_before_surge | false_positive_rate | precision | recall | control_sample_count | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| relative_ret_20d_vs_twse > 0 | 74621 | 11343 | 0.15200814784042024 | 0.07905058518006633 | 1.9229224868375945 | 7.461900474475246 | 11.501309079749369 | -6.3407490036487735 | 0.8479918521595797 | 0.15200814784042024 | 0.45277822129969664 | 4607 | ok |
| volume_ratio_20d between 1.0 and 1.8 | 72458 | 5731 | 0.07909409589003284 | 0.07905058518006633 | 1.000550416038887 | 5.23923057739113 | 7.994341259614438 | -4.865250979127612 | 0.9209059041099672 | 0.07909409589003284 | 0.22876417052530737 | 4607 | ok |
| tdcc_consecutive_up_weeks >= 2 + price_ret_20d <= 8 | 17770 | 1026 | 0.05773776027011818 | 0.07905058518006633 | 0.7303900425101159 | 4.728768783273471 | 7.397360510823696 | -4.277296760330348 | 0.9422622397298819 | 0.05773776027011818 | 0.040954813986907236 | 4607 | ok |
| distance_ma20_pct between -3 and +6 | 191691 | 9833 | 0.05129609632168438 | 0.07905058518006633 | 0.6489021707409116 | 4.118230086275718 | 6.399835723054734 | -4.303150584204976 | 0.9487039036783156 | 0.05129609632168438 | 0.3925035925275427 | 4607 | ok |
| low volatility compression + volume expansion | 40856 | 1111 | 0.027193068337575878 | 0.07905058518006633 | 0.3439957879582272 | 3.3297114026751244 | 5.127961889535792 | -3.51352475044824 | 0.9728069316624242 | 0.027193068337575878 | 0.04434775666613444 | 4607 | ok |
| consolidation_days >= 10 + narrow_range_20d | 121570 | 2867 | 0.0235831208357325 | 0.07905058518006633 | 0.29832949094574573 | 3.0764693352361085 | 4.776615094306783 | -3.339284019037873 | 0.9764168791642674 | 0.0235831208357325 | 0.11444196072169886 | 4607 | ok |
| tdcc_leading_price + quiet_accumulation | 0 | 0 |  | 0.07905058518006633 |  |  |  |  |  |  | 0.0 | 4607 | insufficient_sample |
| theme_mainstream_status = emerging_theme | 0 | 0 |  | 0.07905058518006633 |  |  |  |  |  |  | 0.0 | 4607 | insufficient_sample |
| revenue_yoy > 20 + revenue_low_price_response | 0 | 0 |  | 0.07905058518006633 |  |  |  |  |  |  | 0.0 | 4607 | insufficient_sample |
| warrant_call_inflow + TDCC high_thresholds_up | 0 | 0 |  | 0.07905058518006633 |  |  |  |  |  |  | 0.0 | 4607 | insufficient_sample |

## Backtest Summary
| segment | sample_count | surge_5d_rate | surge_10d_rate | surge_20d_rate | baseline_surge_5d_rate | baseline_surge_10d_rate | baseline_surge_20d_rate | lift_5d | lift_10d | lift_20d | avg_future_max_ret_5d | avg_future_max_ret_10d | avg_future_max_ret_20d | avg_max_drawdown_10d | avg_max_drawdown_20d | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| top_10 | 2350 | 0.01446808510638298 | 0.026382978723404255 | 0.01829787234042553 | 0.04598136385294294 | 0.06810113880553215 | 0.07699006976722171 | 0.31465106499786827 | 0.3874087744515229 | 0.237665356009533 | 3.184579926654533 | 4.939129843234175 | 7.384167477039772 | -3.3202360159160524 | -4.9193104897686855 | ok |
| top_20 | 4149 | 0.014943359845745963 | 0.023138105567606652 | 0.019763798505664017 | 0.04598136385294294 | 0.06810113880553215 | 0.07699006976722171 | 0.3249873121105681 | 0.3397609199117687 | 0.25670581369025325 | 3.167518369650461 | 4.862189853280218 | 7.434464526049068 | -3.276442287854475 | -4.846211384331019 | ok |
| top_50 | 9425 | 0.013156498673740052 | 0.020159151193633953 | 0.021750663129973476 | 0.04598136385294294 | 0.06810113880553215 | 0.07699006976722171 | 0.286126760307002 | 0.29601782800137755 | 0.2825125785148172 | 3.1421367750865588 | 4.787039324852716 | 7.450294587127861 | -3.3447556904598637 | -4.828962913093602 | ok |
| top_100 | 18025 | 0.013370319001386962 | 0.021914008321775313 | 0.024965325936199722 | 0.04598136385294294 | 0.06810113880553215 | 0.07699006976722171 | 0.2907769122322635 | 0.3217862242267694 | 0.3242668309261441 | 3.130946850458671 | 4.826963367763004 | 7.4970992827869125 | -3.3786517639254003 | -4.835638225874106 | ok |
| score_ge_80 | 2585 | 0.011218568665377175 | 0.023984526112185687 | 0.01276595744680851 | 0.04598136385294294 | 0.06810113880553215 | 0.07699006976722171 | 0.2439807723245502 | 0.3521897949559299 | 0.16581303907641837 | 3.375071030417543 | 5.321237399027727 | 8.325266094559666 | -2.8910806474338093 | -4.059394981679232 | ok |
| score_70_80 | 2179 | 0.017898118402937126 | 0.027535566773749427 | 0.023405231757687012 | 0.04598136385294294 | 0.06810113880553215 | 0.07699006976722171 | 0.3892472276415871 | 0.404333426088208 | 0.30400325429568215 | 3.7687454211627625 | 5.928044605060643 | 9.975946902451819 | -3.509057805629599 | -4.767508969331839 | ok |
| score_60_70 | 2082 | 0.03218059558117195 | 0.0494716618635927 | 0.034101825168107586 | 0.04598136385294294 | 0.06810113880553215 | 0.07699006976722171 | 0.6998617023212176 | 0.7264439733506175 | 0.4429379694188345 | 4.74378470201924 | 7.362323593272939 | 13.1160980960486 | -4.928226197253245 | -6.967975905965229 | ok |
| score_50_60 | 4523 | 0.03183727614415211 | 0.05085120495246518 | 0.04687154543444617 | 0.04598136385294294 | 0.06810113880553215 | 0.07699006976722171 | 0.6923952113724533 | 0.7467012423635758 | 0.6087998825843588 | 4.424028582005026 | 7.046331016282176 | 11.916912360610334 | -4.171610356823454 | -5.226687253038852 | ok |
| score_lt_50 | 305542 | 0.04677916620300973 | 0.06914597665787355 | 0.07865367118104875 | 0.04598136385294294 | 0.06810113880553215 | 0.07699006976722171 | 1.0173505586441132 | 1.0153424431759506 | 1.021607999822015 | 5.219907137899845 | 8.046178740385633 | 12.496809053499234 | -5.107939856798542 | -6.8561870620301715 | ok |
| label_A_surge_watch | 3216 | 0.012126865671641791 | 0.024564676616915422 | 0.013992537313432836 | 0.04598136385294294 | 0.06810113880553215 | 0.07699006976722171 | 0.2637343622608888 | 0.3607087494830546 | 0.1817447023458877 | 3.4983105243516714 | 5.441467802637675 | 8.592950471777339 | -3.0008350985033942 | -4.165290787518475 | ok |
| label_B_confirm_needed | 3470 | 0.026512968299711816 | 0.04092219020172911 | 0.03025936599423631 | 0.04598136385294294 | 0.06810113880553215 | 0.07699006976722171 | 0.5766024771362868 | 0.6009031701890546 | 0.39302946582234616 | 4.292376157149273 | 6.789658014386473 | 11.718486174046237 | -4.370213885114368 | -5.94932616024935 | ok |
| label_C_too_hot | 34353 | 0.1346316187814747 | 0.17852880388903444 | 0.19005618141064826 | 0.04598136385294294 | 0.06810113880553215 | 0.07699006976722171 | 2.9279605366220096 | 2.621524500476221 | 2.4685804544050964 | 9.269762658720994 | 13.984346212278643 | 21.67915744506612 | -7.961099446983263 | -10.1511850675745 | ok |
| label_D_weak_or_insufficient | 275872 | 0.03558171905811391 | 0.05519951281753857 | 0.06423268762324556 | 0.04598136385294294 | 0.06810113880553215 | 0.07699006976722171 | 0.7738291359062541 | 0.8105519788026582 | 0.8342983428570997 | 4.70194399617897 | 7.289079523402329 | 11.372603222692456 | -4.736383625682445 | -6.435426208735075 | ok |
| market_unknown | 316911 | 0.04598136385294294 | 0.06810113880553215 | 0.07699006976722171 | 0.04598136385294294 | 0.06810113880553215 | 0.07699006976722171 | 1.0 | 1.0 | 1.0 | 5.180394377729236 | 7.99062533479008 | 12.453245191347103 | -5.064319637830865 | -6.810748875861678 | ok |
| theme_unknown | 316911 | 0.04598136385294294 | 0.06810113880553215 | 0.07699006976722171 | 0.04598136385294294 | 0.06810113880553215 | 0.07699006976722171 | 1.0 | 1.0 | 1.0 | 5.180394377729236 | 7.99062533479008 | 12.453245191347103 | -5.064319637830865 | -6.810748875861678 | ok |

## Risk Summary
- C_too_hot / failed_breakout / high_volume_upper_shadow 不可解讀為暴漲前低位候選。
- 未來資料只用於 label，不可用來產生當日 feature。
- pending 不可視為成功或失敗。
- 樣本不足時標示 insufficient_sample，不做正式調參。

## Model Tuning Status
tuning_status = not_ready
reason = insufficient mature samples for stable feature/weight tuning
allowed_changes = reporting_priority_only
forbidden_changes = core_weight_change

## Raw URLs
- surge_precondition_candidates_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/surge_precondition_candidates_latest.md
- surge_precondition_candidates_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/surge_precondition_candidates_latest.csv
- surge_model_backtest_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/surge_model_backtest_latest.md
- surge_model_backtest_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/surge_model_backtest_latest.csv
- surge_model_feature_importance_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/surge_model_feature_importance_latest.md
- surge_model_feature_importance_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/surge_model_feature_importance_latest.csv
