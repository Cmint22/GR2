# Chuyển động thị trường

## Bản đồ nhiệt giá

```python
fr_trade_heatmap (symbol='HOSE', report_type='FrBuyVal')
```

Kết quả:

```shell
>>> fr_trade_heatmap (symbol='VN30', report_type='FrBuyVal').T
                                                         0   ...                                 29
avgPrice                                           21583.35  ...                           24757.58
best1Bid                                            21550.0  ...                                NaN
best1BidVol                                        205900.0  ...                                NaN
best1Offer                                            21600  ...                              24600
best1OfferVol                                         39500  ...                             690100
best2Bid                                            21500.0  ...                                NaN
best2BidVol                                        620300.0  ...                                NaN
best2Offer                                            21650  ...                              24650
best2OfferVol                                         65700  ...                              86200
best3Bid                                            21450.0  ...                                NaN
best3BidVol                                        483100.0  ...                                NaN
best3Offer                                            21700  ...                              24700
best3OfferVol                                         29700  ...                              20500
caStatus                                                     ...
ceiling                                               23400  ...                              28300
corporateEvents                                          []  ...                                 []
coveredWarrantType                                           ...
exchange                                               hose  ...                               hose
exercisePrice                                             0  ...                                  0
exerciseRatio                                                ...
floor                                                 20400  ...                              24600
highest                                               21750  ...                              25900
issuerName                                                   ...
lastTradingDate                                              ...
lastVol                                               38999  ...                              54716
lowest                                                21450  ...                              24600
matchedPrice                                          21550  ...                              24600
maturityDate                                                 ...
nmTotalTradedValue                              84172900000  ...                       135463580000
openPrice                                             21750  ...                              25900
priorClosePrice                                       21900  ...                              26450
refPrice                                              21900  ...                              26450
securityName                          NGAN HANG TMCP A CHAU  ...                 CTCP VINCOM RETAIL
stockSymbol                                             ACB  ...                                VRE
stockType                                                 s  ...                                  s
totalShare                                            38999  ...                              54716
tradingStatus                                                ...
tradingUnit                                             100  ...                                100
underlyingSymbol                                             ...
companyNameEn              Asia Commercial Joint Stock Bank  ...  Vincom Retail Joint Stock Company
companyNameVi           Ngân hàng Thương mại Cổ phần Á Châu  ...      Công ty Cổ phần Vincom Retail
oddSession                                               LO  ...                                 LO
session                                                  LO  ...                                 LO
buyForeignQtty                                       120300  ...                             748207
remainForeignQtty                                         0  ...                          382909157
sellForeignQtty                                      120365  ...                             695725
matchedVolume                                            30  ...                                 50
priceChange                                            -350  ...                              -1850
priceChangePercent                                     -1.6  ...                              -6.99
lastMatchedPrice                                      21550  ...                              24600
lastMatchedVolume                                        30  ...                                 50
lastPriceChange                                        -350  ...                              -1850
lastPriceChangePercent                                 -1.6  ...                              -6.99
nmTotalTradedQty                                    3899900  ...                            5471600

[54 rows x 30 columns]
```

## Top cổ phiếu

```python
market_top_mover (report_name='Value', exchange='All', filter= 'NetBuyVol', report_range='ThreeMonths', rate='OnePointFive', lang='vi')
```

```python
market_top_mover (report_name='Value', exchange='All', filter= 'NetBuyVol', report_range='ThreeMonths', rate='OnePointFive', lang='vi')
```

```python
market_top_mover (report_name='Losers', exchange='All', filter= 'NetBuyVol', report_range='ThreeMonths', rate='OnePointFive', lang='vi')
```


```python
market_top_mover (report_name='Gainers', exchange='All', filter= 'NetBuyVol', report_range='ThreeMonths', rate='OnePointFive', lang='vi')
```


```python
market_top_mover (report_name='Volume', exchange='All', filter= 'NetBuyVol', report_range='ThreeMonths', rate='OnePointFive', lang='vi')
```


```python
market_top_mover (report_name='ForeignTrading', exchange='All', filter= 'NetBuyVol', report_range='ThreeMonths', rate='OnePointFive', lang='vi')
```

```python
market_top_mover (report_name='NewLow', exchange='All', filter= 'NetBuyVol', report_range='ThreeMonths', rate='OnePointFive', lang='vi')
```

```python
market_top_mover (report_name='NewHigh', exchange='All', filter= 'NetBuyVol', report_range='ThreeMonths', rate='OnePointFive', lang='vi')
```

```python
market_top_mover (report_name='Breakout', exchange='All', filter= 'NetBuyVol', report_range='TwoWeeks', rate='OnePointFive', lang='vi')
```