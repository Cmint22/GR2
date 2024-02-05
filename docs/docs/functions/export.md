# Xuất dữ liệu

## Xuất file CSV

```python
from vnstock import * 
df =  stock_historical_data(symbol='GMD', 
                            start_date="2021-01-01", 
                            end_date='2022-02-25', resolution='1D', type='stock', beautify=True)
df.to_csv(r'ĐƯỜNG_DẪN_THƯ_MỤC_CỦA_BẠN/GMD.csv', index=False)
```


## Xuất file Excel

```python
from vnstock import * 
df =  stock_historical_data(symbol='GMD', 
                            start_date="2021-01-01", 
                            end_date='2022-02-25', resolution='1D', type='stock', beautify=True)
df.to_excel(r'ĐƯỜNG_DẪN_THƯ_MỤC_CỦA_BẠN/GMD.xlsx', index=False)
```