from .config import *

## STOCK TRADING HISTORICAL DATA
def stock_historical_data (symbol='TCB', start_date='2023-06-01', end_date='2023-06-17', resolution='1D', type='stock', beautify=True, decor=False, source='DNSE'): # DNSE source (will be published on vnstock)
    if source.upper() == 'DNSE':
        df = ohlc_data(symbol, start_date, end_date, resolution, type, headers=entrade_headers)
    elif source.upper() == 'TCBS':
        if resolution == '1D':
            resolution = 'D'
            df = longterm_ohlc_data(symbol, start_date, end_date, resolution, type, headers=tcbs_headers)
        else:
            print('TCBS only support longterm daily data. Please set resolution to 1D')
            return None
    df = df[['time', 'open', 'high', 'low', 'close', 'volume', 'ticker']]
    if beautify:
        if type == 'stock':
            df[['open', 'high', 'low', 'close']] = df[['open', 'high', 'low', 'close']] * 1000
            df[['open', 'high', 'low', 'close']] = df[['open', 'high', 'low', 'close']].astype(int)
    if decor == True:
        df.columns = df.columns.str.title()
        df = df.set_index('Time')
    return df

def longterm_ohlc_data (symbol='REE', start_date='2022-01-01', end_date='2023-10-31', resolution='D', type='stock', headers=tcbs_headers):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    delta = (end_date - start_date).days
    end_date_stp = int(end_date.timestamp())
    print(f'Time range is {delta} days. Looping through {delta // 365 + 1} requests')
    if delta > 365:
        df = pd.DataFrame()
        while delta > 365:
            if type in ['stock', 'index']:
                url = f"https://apipubaws.tcbs.com.vn/stock-insight/v2/stock/bars-long-term?ticker={symbol}&type={type}&resolution={resolution}&to={end_date_stp}&countBack=365"
            elif type == 'derivative':
                url = f'https://apipubaws.tcbs.com.vn/futures-insight/v2/stock/bars-long-term?ticker={symbol}&type=derivative&resolution={resolution}&to={end_date_stp}&countBack=365'
            response = requests.request("GET", url, headers=headers)
            status_code = response.status_code
            if status_code == 200:
                data = response.json()
                df_temp = pd.DataFrame(data['data'])
                df_temp['time'] = pd.to_datetime(df_temp['tradingDate']).dt.strftime('%Y-%m-%d')
                df_temp.drop('tradingDate', axis=1, inplace=True)
                df = pd.concat([df_temp, df], ignore_index=True)
                end_date_stp = int(datetime.strptime(df['time'].min(), '%Y-%m-%d').timestamp())
                delta = delta - 365
            else:
                print(f'Error {status_code}. {response.text}')
        if type in ['stock', 'index']:
            url = f"https://apipubaws.tcbs.com.vn/stock-insight/v2/stock/bars-long-term?ticker={symbol}&type={type}&resolution={resolution}&to={end_date_stp}&countBack={delta}"
        elif type == 'derivative':
            url = f'https://apipubaws.tcbs.com.vn/futures-insight/v2/stock/bars-long-term?ticker={symbol}&type=derivative&resolution={resolution}&to={end_date_stp}&countBack={delta}'
        response = requests.request("GET", url, headers=headers)
        status_code = response.status_code
        if status_code == 200:
            data = response.json()
            df_temp = pd.DataFrame(data['data'])
            df_temp['time'] = pd.to_datetime(df_temp['tradingDate']).dt.strftime('%Y-%m-%d')
            df_temp.drop('tradingDate', axis=1, inplace=True)
            df = pd.concat([df_temp, df], ignore_index=True)
        else:
            print(f'Error {status_code}. {response.text}')
        df = df[(df['time'] >= start_date.strftime('%Y-%m-%d')) & (df['time'] <= end_date.strftime('%Y-%m-%d'))]
        df['ticker'] = symbol
        df = df[(df['time'] >= start_date.strftime('%Y-%m-%d')) & (df['time'] <= end_date.strftime('%Y-%m-%d'))]
        if type == 'stock':
            df[['open', 'high', 'low', 'close']] = round(df[['open', 'high', 'low', 'close']] / 1000, 2)
        df[['open', 'high', 'low', 'close']] = df[['open', 'high', 'low', 'close']].astype(float)
        df['volume'] = df['volume'].astype(int)
        return df
    else:
        if type in ['stock', 'index']:
            url = f"https://apipubaws.tcbs.com.vn/stock-insight/v2/stock/bars-long-term?ticker={symbol}&type={type}&resolution={resolution}&to={end_date_stp}&countBack={delta}"
        elif type == 'derivative':
            url = f'https://apipubaws.tcbs.com.vn/futures-insight/v2/stock/bars-long-term?ticker={symbol}&type=derivative&resolution={resolution}&to={end_date_stp}&countBack={delta}'
        response = requests.request("GET", url, headers=headers)
        status_code = response.status_code
        if status_code == 200:
            data = response.json()
            df = pd.DataFrame(data['data'])
            df['time'] = pd.to_datetime(df['tradingDate']).dt.strftime('%Y-%m-%d')
            df.drop('tradingDate', axis=1, inplace=True)
            df['ticker'] = symbol
            df = df[(df['time'] >= start_date.strftime('%Y-%m-%d')) & (df['time'] <= end_date.strftime('%Y-%m-%d'))]
            if type == 'stock':
                df[['open', 'high', 'low', 'close']] = round(df[['open', 'high', 'low', 'close']] / 1000, 2)
            df[['open', 'high', 'low', 'close']] = df[['open', 'high', 'low', 'close']].astype(float)
            df['volume'] = df['volume'].astype(int)
            return df
        else:
            print(f'Error {status_code}. {response.text}')
            return None
        
def ohlc_data (symbol, start_date='2023-06-01', end_date='2023-06-17', resolution='1D', type='stock', headers=entrade_headers): 
    end_date = (datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
    start_timestamp = int(datetime.strptime(start_date, '%Y-%m-%d').timestamp())
    end_timestamp = int(datetime.strptime(end_date, '%Y-%m-%d').timestamp())
    if resolution != '1D':
        new_start_timestamp = int(datetime.now().timestamp()) - 90 * 24 * 60 * 60
        new_end_timestamp = int(datetime.now().timestamp()) - 90 * 24 * 60 * 60
        if end_timestamp < new_end_timestamp:
            print("The 'end_date' value in the report should be no more than 90 days from today for all resolutions shorter than 1 day.", "\n")
        elif new_start_timestamp > start_timestamp:
            start_timestamp = new_start_timestamp
            print("The retrieval of stock data is restricted to the most recent 90 days from today for all resolutions shorter than 1 day.", "\n")
    url = f"https://services.entrade.com.vn/chart-api/v2/ohlcs/{type}?from={start_timestamp}&to={end_timestamp}&symbol={symbol}&resolution={resolution}"
    response = requests.request("GET", url, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        df = pd.DataFrame(response_data)
        df['t'] = pd.to_datetime(df['t'], unit='s') 
        df = df.rename(columns={'t': 'time', 'o': 'open', 'h': 'high', 'l': 'low', 'c': 'close', 'v': 'volume'}).drop(columns=['nextTime'])
        df['ticker'] = symbol
        df['time'] = df['time'].dt.tz_localize('UTC').dt.tz_convert('Asia/Ho_Chi_Minh')
        if resolution == '1D':
            df['time'] = df['time'].dt.date
        else:
            df['time'] = df['time'].dt.strftime('%Y-%m-%d %H:%M:%S')
        df[['open', 'high', 'low', 'close']] = df[['open', 'high', 'low', 'close']].astype(float)
        df['volume'] = df['volume'].astype(int)
    else:
        print(f"Error in API response {response.text}", "\n")
    return df