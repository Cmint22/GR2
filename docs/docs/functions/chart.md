# Biểu diễn dữ liệu

```shell
pip install plotly
```

## Đồ thị nến

```python
from vnstock import * #import all functions, including functions that provide OHLC data for charting
from vnstock.chart import * # import chart functions
df = stock_historical_data("VIC", "2022-01-01", "2023-10-10", "1D", "stock")
fig = candlestick_chart(df, ma_periods=[50,200], show_volume=False, reference_period=300, figure_size=(15, 8), 
                        title='VIC - Candlestick Chart with MA and Volume', x_label='Date', y_label='Price', 
                        colors=('lightgray', 'gray'), reference_colors=('black', 'blue'))
fig.show()
```


```python
from vnstock import * #import all functions

df = stock_historical_data(symbol='VNINDEX', start_date='2022-01-01', end_date='2023-10-10', resolution='1D', type='index')
fig = candlestick_chart(df, 
                  title='VNINDEX Candlestick Chart with MA and Volume', x_label='Date', y_label='Price', ma_periods=[50,200], 
                  show_volume=True, figure_size=(15, 8), reference_period=300, 
                  colors=('lightgray', 'gray'), reference_colors=('black', 'blue'))
fig.show()
```

## Đồ thị Bollinger Bands

```python
from vnstock import * #import all functions
df = stock_historical_data(symbol='VNINDEX', start_date='2022-01-01', end_date='2023-10-10', resolution='1D', type='index')
bollinger_df = bollinger_bands(df, window=20, num_std_dev=2)
fig = bollinger_bands_chart(bollinger_df, use_candlestick=True, show_volume=True, 
                            fig_size=(15, 8), chart_title='Bollinger Bands Chart', xaxis_title='Date', yaxis_title='Price', 
                            bollinger_band_colors=('gray', 'orange', 'gray'), volume_colors=('#00F4B0', '#FF3747'))
fig.show()
```