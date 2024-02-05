from .config import *

def derivatives_historical_match (symbol='VN30F2308', date='2023-07-24', cookie=rv_cookie, headers=rv_headers):
    headers['Cookie'] = cookie
    url = "https://livedragon.vdsc.com.vn/general/intradaySearch.rv"
    date = datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%Y')
    payload = f"stockCode={symbol}&boardDate={date}"
    response = requests.request("POST", url, headers=headers, data=payload).json()
    df = pd.DataFrame(response['list'])
    df = df[['Code'] + [col for col in df.columns if col != 'Code']]
    return df