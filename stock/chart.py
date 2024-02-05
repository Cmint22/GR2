from .config import *
from .technical import *

import plotly.graph_objs as go


# CANDLESTICK CHART
def candlestick_chart(df, title='Candlestick Chart with MA and Volume', x_label='Date', y_label='Price', ma_periods=None, show_volume=True, figure_size=(15, 8), reference_period=None, colors=('#00F4B0', '#FF3747'), reference_colors=('blue', 'black')):
    candlestick_trace = go.Candlestick(
        x=df['time'],
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close'],
        name='Candlestick',
    )

    fig = go.Figure(data=[candlestick_trace])
    if show_volume:
        volume_trace = go.Bar(
            x=df['time'],
            y=df['volume'],
            name='Volume',
            yaxis='y2',  # Use the secondary y-axis for volume
            marker=dict(color=[colors[0] if close >= open else colors[1] for close, open in zip(df['close'], df['open'])]),  # Match volume color to candle color
        )
        fig.add_trace(volume_trace)

    if ma_periods:
        for period in ma_periods:
            ma_name = f'{period}-day MA'
            df[ma_name] = df['close'].rolling(period).mean()
            ma_trace = go.Scatter(
                x=df['time'],
                y=df[ma_name],
                mode='lines',
                name=ma_name,
            )
            fig.add_trace(ma_trace)

    if reference_period:
        df['lowest_low'] = df['low'].rolling(reference_period).min()
        df['highest_high'] = df['high'].rolling(reference_period).max()
        lowest_low_trace = go.Scatter(
            x=df['time'],
            y=[df['lowest_low'].iloc[-1]] * len(df),  
            mode='lines',
            name=f'Lowest Low ({reference_period} days)',
            line=dict(color=reference_colors[0], dash='dot'),
        )
        highest_high_trace = go.Scatter(
            x=df['time'],
            y=[df['highest_high'].iloc[-1]] * len(df),  
            mode='lines',
            name=f'Highest High ({reference_period} days)',
            line=dict(color=reference_colors[1], dash='dot'),
        )
        fig.add_trace(lowest_low_trace)
        fig.add_trace(highest_high_trace)

    fig.update_layout(
        title=title,
        xaxis_title=x_label,
        yaxis_title=y_label,
        xaxis_rangeslider_visible=True,
        yaxis2=dict(
            title='Volume',
            overlaying='y',
            side='right',
        ),
        width=figure_size[0] * 100,  
        height=figure_size[1] * 100,
        margin=dict(l=50, r=50, t=70, b=50),  
    )
    return fig


def bollinger_bands(df, window=20, num_std_dev=2):
    df['middle_band'] = df['close'].rolling(window=window).mean()
    df['rolling_std'] = df['close'].rolling(window=window).std()
    df['upper_band'] = df['middle_band'] + (num_std_dev * df['rolling_std'])
    df['lower_band'] = df['middle_band'] - (num_std_dev * df['rolling_std'])
    df.drop(columns=['rolling_std'], inplace=True)
    return df

def bollinger_bands_chart(df, use_candlestick=True, show_volume=True, fig_size=(15, 8), chart_title='Bollinger Bands Chart', xaxis_title='Date', yaxis_title='Price', bollinger_band_colors=('gray', 'orange', 'gray'), volume_colors=('#00F4B0', '#FF3747')):
    fig = go.Figure()
    if use_candlestick:
        candlestick_trace = go.Candlestick(
            x=df['time'],
            open=df['open'],
            high=df['high'],
            low=df['low'],
            close=df['close'],
            name='Candlestick',
        )
        fig.add_trace(candlestick_trace)
    else:
        close_price_trace = go.Scatter(
            x=df['time'],
            y=df['close'],
            mode='lines',
            name='Close Price',
        )
        fig.add_trace(close_price_trace)

    upper_band_trace = go.Scatter(
        x=df['time'],
        y=df['upper_band'],
        mode='lines',
        line=dict(color=bollinger_band_colors[0]),
        name='Upper Bollinger Band',
    )
    middle_band_trace = go.Scatter(
        x=df['time'],
        y=df['middle_band'],
        mode='lines',
        line=dict(color=bollinger_band_colors[1]),
        name='Middle Bollinger Band',
    )
    lower_band_trace = go.Scatter(
        x=df['time'],
        y=df['lower_band'],
        mode='lines',
        line=dict(color=bollinger_band_colors[2]),
        name='Lower Bollinger Band',
    )
    fig.add_trace(upper_band_trace)
    fig.add_trace(middle_band_trace)
    fig.add_trace(lower_band_trace)

    if show_volume:
        volume_color = [volume_colors[0] if close >= open else volume_colors[1] for close, open in zip(df['close'], df['open'])]
        volume_trace = go.Bar(
            x=df['time'],
            y=df['volume'],
            name='Volume',
            marker=dict(color=volume_color),
            yaxis='y2',
        )
        fig.add_trace(volume_trace)

    fig.update_layout(
        title=chart_title,
        xaxis_title=xaxis_title,
        yaxis_title=yaxis_title,
        xaxis_rangeslider_visible=True,
        legend=dict(orientation="h", y=1.05),
        yaxis2=dict(title='Volume', overlaying='y', side='right'),
        width=fig_size[0] * 100,  
        height=fig_size[1] * 100,  
    )
    return fig
