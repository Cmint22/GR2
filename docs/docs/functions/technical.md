## Truy xuất dữ liệu giá lịch sử

```python
df =  stock_historical_data(symbol='GMD', 
                            start_date="2021-01-01", 
                            end_date='2022-02-25', resolution='1D', type='stock', beautify=True, decor=False, source='DNSE')
print(df)
```

    ```
    time        open     high     low      close    volume
    0  2021-01-04  32182.0  33157.0  31987.0  32279.0  4226500
    1  2021-01-05  32279.0  33596.0  31938.0  32962.0  4851900
    2  2021-01-06  33352.0  33352.0  32279.0  32572.0  3641300
    ```

- Lấy dữ liệu lịch sử của mã chỉ số
```python
df = stock_historical_data("VNINDEX", "2021-01-01", "2022-02-25", "1D", 'index')
print(df)
```

- Lấy dữ liệu lịch sử của hợp đồng phái sinh
```python
df = stock_historical_data("VN30F1M", "2023-07-01", "2023-07-24", "1D", 'derivative')
print(df)
```

## Dữ liệu khớp lệnh trong ngày giao dịch

```python
df =  stock_intraday_data(symbol='TCB', 
                            page_size=500, investor_segment=True)
print(df)
```

```shell
>>> stock_intraday_data (symbol='ACB', page_size=10, investor_segment=False)
  ticker      time orderType  volume    price  prevPriceChange
0    ACB  14:45:00            211500  22550.0           -100.0
1    ACB  14:29:53        BU    1000  22650.0              0.0
2    ACB  14:29:38        BU     100  22650.0              0.0
3    ACB  14:28:34        BU     300  22650.0             50.0
4    ACB  14:28:15        SD    1200  22600.0              0.0
5    ACB  14:28:15        SD     300  22600.0              0.0
6    ACB  14:28:15        SD     400  22600.0              0.0
7    ACB  14:28:15        SD     300  22600.0              0.0
8    ACB  14:28:15        SD     100  22600.0              0.0
9    ACB  14:28:15        SD     200  22600.0              0.0
```

```shell
>>> stock_intraday_data (symbol='ACB', page_size=10, investor_segment=True)
  ticker      time  orderType investorType  volume  averagePrice  orderCount  prevPriceChange
0    ACB  14:29:54     Buy Up        SHEEP    1000       22650.0           1              0.0
1    ACB  14:29:39     Buy Up        SHEEP     100       22650.0           1              0.0
2    ACB  14:28:34     Buy Up        SHEEP     300       22650.0           1             50.0
3    ACB  14:28:16  Sell Down        SHEEP    7000       22600.0          29            -50.0
4    ACB  14:28:11     Buy Up        SHEEP     200       22650.0           1              0.0
5    ACB  14:27:43     Buy Up        SHEEP    1000       22650.0           1             50.0
6    ACB  14:27:28  Sell Down        SHEEP    3200       22600.0           2              0.0
7    ACB  14:26:38  Sell Down        SHEEP     300       22600.0           1            -50.0
8    ACB  14:26:36     Buy Up        SHEEP     100       22650.0           1              0.0
9    ACB  14:26:21     Buy Up        SHEEP    3000       22650.0           1             50.0
```