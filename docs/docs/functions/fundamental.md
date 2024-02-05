# Phân tích cơ bản

## Thông tin tổng quan

```python
company_overview('TCB')
```

```shell
>>> company_overview('TCB').T
                                              0
ticker                                      TCB
exchange                                   HOSE
industry                              Ngân hàng
companyType                                  NH
noShareholders                             1901
foreignPercent                            0.225
outstandingShare                         3517.2
issueShare                               3517.2
establishedYear                            1993
noEmployees                                9757
stockRating                                 4.2
deltaInWeek                              -0.002
deltaInMonth                              0.001
deltaInYear                               0.189
shortName                           Techcombank
industryEn                                Banks
industryID                                  289
industryIDv2                               8355
website           http://www.techcombank.com.vn
```

## Hồ sơ công ty

```python
company_profile ('TCB')
```

```shell
>>> company_profile ('TCB').T
                                                                    0
id                                                               None
companyName           Ngân hàng Thương mại Cổ phần Kỹ thương Việt Nam
ticker                                                            TCB
companyProfile      Ngân hàng Thương mại Cổ phần Kỹ thương Việt Na...
historyDev            Ngày 27/09/1993: Ngân hàng Thương mại Cổ phầ...
companyPromise                                                   None
businessRisk          Thông tư 36/2014/TT-NHNN cũng gây ra một số ...
keyDevelopments       Huy động vốn; Tín dụng; Liên kết và đầu tư t...
businessStrategies   Mở rộng tập khách hàng cả về quy mô và tốc độ...
```

## Danh sách cổ đông

```python
company_large_shareholders ('TCB')
```

```shell
  >>> company_large_shareholders ('TCB')
    ticker                     shareHolder  shareOwnPercent
  0    TCB  Công ty Cổ phần Tập đoàn Masan           0.1491
  1    TCB           Nguyễn Thị Thanh Thủy           0.0495
  2    TCB            Nguyễn Thị Thanh Tâm           0.0495
  3    TCB                     Hồ Anh Minh           0.0392
  4    TCB               Nguyễn Phương Hoa           0.0216
  5    TCB               Nguyễn Hương Liên           0.0198
  6    TCB                     HỒ HÙNG ANH           0.0112
  7    TCB              Nguyễn Thiều Quang           0.0086
  8    TCB                     Hồ Thủy Anh           0.0064
  9    TCB                            Khác           0.0292
```

## Các chỉ số tài chính cơ bản

```python
company_fundamental_ratio (symbol='TCB', mode='simplify', missing_pct=0.8)
```

```shell
>>> company_fundamental_ratio (symbol='TCB', mode='simplify', missing_pct=0.8).T
                                         0
ticker                                 TCB
costOfFinancing.industryAvgValue     0.056
interestMargin.industryAvgValue      0.034
nonInterestOnToi.industryAvgValue    0.215
costToIncome.industryAvgValue        0.437
preProvisionOnToi.industryAvgValue   0.449
postTaxOnToi.industryAvgValue        0.322
depositOnEarnAsset.industryAvgValue  0.725
cancelDebt.industryAvgValue          0.007
badDebtPercentage.industryAvgValue   0.024
provisionOnBadDebt.industryAvgValue  0.609
loanOnDeposit.industryAvgValue        0.96
equityOnTotalAsset.industryAvgValue  0.086
badDebtOnAsset.industryAvgValue      0.015
```

## Mức biến động giá cổ phiếu

```python
ticker_price_volatility (symbol='TCB')
```

```shell
>>> ticker_price_volatility (symbol='TCB').T
                                  0
ticker                          TCB
ticker_highestPrice         35750.0
ticker_lowestPrice          20700.0
ticker_highestPricePercent   -0.143
ticker_lowestPricePercent     0.481
```


## Thông tin sự kiện quyền

```python
company_events (symbol='TPB', page_size=10, page=0)
```

```
>>> company_events (symbol='TPB', page_size=10, page=0)
        id ticker  price  priceChange  priceChangeRatio  ...             exerDate         regFinalDate          exRigthDate                                          eventDesc eventNote
0  2563370    TPB  18100         -350            -0.019  ...  2023-07-07 00:00:00  1753-01-01 00:00:00  1753-01-01 00:00:00  <p>Ngân hàng Thương mại Cổ phần Tiên Phong (TP...      None
1  2563135    TPB  18535         -215            -0.011  ...  2023-06-09 00:00:00  2023-06-12 00:00:00  2023-06-09 00:00:00  <p>Ngân hàng Thương mại Cổ phần Tiên Phong (TP...      None
2  2561933    TPB  15668          -64            -0.004  ...  2023-04-26 00:00:00  2023-03-29 00:00:00  2023-03-28 00:00:00  <p>Ngân hàng Thương mại Cổ phần Tiên Phong (TP...      None
3  2561033    TPB  15441          -97            -0.006  ...  2023-04-03 00:00:00  2023-03-21 00:00:00  2023-03-20 00:00:00  <p>Ngân hàng Thương mại Cổ phần Tiên Phong (TP...      None
4  2560718    TPB  14567            0             0.000  ...  1753-01-01 00:00:00  2023-01-17 00:00:00  2023-01-16 00:00:00  <p>Ngân hàng Thương mại Cổ phần Tiên Phong (TP...      None
5  2517318    TPB  25832          453             0.018  ...  2022-04-26 00:00:00  2022-03-28 00:00:00  2022-03-25 00:00:00  <p>Ngân hàng Thương mại Cổ phần Tiên Phong (TP...      None
6  2406108    TPB  27192            0             0.000  ...  2022-01-13 00:00:00  1753-01-01 00:00:00  1753-01-01 00:00:00  <DIV style="FONT-FAMILY: Arial; FONT-SIZE: 10p...
7  2395935    TPB  24936          719             0.030  ...  2021-12-20 00:00:00  2021-12-21 00:00:00  2021-12-20 00:00:00  <DIV style="FONT-FAMILY: Arial; FONT-SIZE: 10p...
8  2235221    TPB  31480          371             0.012  ...  2022-09-15 00:00:00  1753-01-01 00:00:00  1753-01-01 00:00:00  <DIV style="FONT-FAMILY: Arial; FONT-SIZE: 10p...
9  2215176    TPB  30665          519             0.017  ...  1753-01-01 00:00:00  2021-10-11 00:00:00  2021-10-08 00:00:00  <DIV style="FONT-FAMILY: Arial; FONT-SIZE: 10p...

[10 rows x 15 columns]

```


## Tin tức công ty

```python
company_news (symbol='TCB', page_size=10, page=0)
```

```
>>> company_news (symbol='TCB', page_size=10, page=0)
ticker  price  priceChange  priceChangeRatio  priceChangeRatio1W  priceChangeRatio1M        id                                              title source          publishDate
0    TCB  34500          500             0.015               0.021               0.006  10915190  TCB:  Báo cáo kết quả giao dịch cổ phiếu của n...   HOSE  2023-08-31 11:12:00
1    TCB  33650         -150            -0.004               0.035               0.004  10909083  TCB:  CBTT về việc giải tỏa cổ phiếu hạn chế c...   HOSE  2023-08-25 16:35:00
2    TCB  33100          350             0.011              -0.028               0.020  10905062  TCB: Con gái Chủ tịch đăng ký mua trên 82 triệ...   HOSE  2023-08-22 11:19:00
3    TCB  32750          250             0.008              -0.031               0.014  10904072  Báo cáo kết quả phân phối chứng quyền có bảo đ...   HOSE  2023-08-21 16:21:00
4    TCB  34700         -600            -0.017               0.036               0.088  10900206  Thông báo phát hành chứng quyền và Bản cáo bạc...   HOSE  2023-08-17 14:48:00
5    TCB  34700         -600            -0.017               0.036               0.088  10899331  Giấy chứng nhận chào bán chứng quyền có bảo đả...   HOSE  2023-08-17 08:55:00
6    TCB  33800          150             0.004              -0.016               0.058  10895913  Thông báo hủy đợt phát hành chứng quyền có bảo...   HOSE  2023-08-14 17:36:00
7    TCB  33500         -500            -0.015               0.000               0.047  10892819  TCB:  CBTT Chuyển quyền sở hữu cổ phiếu từ Côn...   HOSE  2023-08-10 17:55:00
8    TCB  34000            0             0.000               0.003               0.063  10891020  Thông báo phát hành chứng quyền và Bản cáo bạc...   HOSE  2023-08-09 16:55:00
9    TCB  34000            0             0.000               0.003               0.063  10890346  Báo cáo kết quả phân phối chứng quyền có bảo đ...   HOSE  2023-08-09 10:26:00

```