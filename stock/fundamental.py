from .config import *
from bs4 import BeautifulSoup


## STOCK LISTING
def live_stock_list ():
    url = "https://wifeed.vn/api/thong-tin-co-phieu/danh-sach-ma-chung-khoan"
    response = requests.request("GET", url).json()
    df = pd.DataFrame(response['data'])
    df = df.rename(columns={'fullname_vi': 'organName', 'code': 'ticker', 'loaidn': 'organTypeCode', 'san': 'comGroupCode'})
    return df

def organ_listing (lang='vi', headers=ssi_headers):
    url = f"https://fiin-core.ssi.com.vn/Master/GetListOrganization?language={lang}"
    response = requests.request("GET", url, headers=headers)
    status = response.status_code
    if status == 200:
        data = response.json()
        print('Total number of companies: ', data['totalCount'])
        df = pd.DataFrame(data['items'])
        return df
    else:
        print('Error in API response', response.text)

def indices_listing (lang='vi', headers=ssi_headers):
    url = f"https://fiin-core.ssi.com.vn/Master/GetAllCompanyGroup?language={lang}"
    response = requests.request("GET", url, headers=headers)
    status = response.status_code
    if status == 200:
        data = response.json()
        df = pd.DataFrame(data['items'])
        df = df.sort_values(by='comGroupOrder').reset_index(drop=True)
        df = df[['comGroupCode', 'parentComGroupCode', 'comGroupOrder']]
        return df
    else:
        print('Error in API response', response.text)

def offline_stock_list (path='https://raw.githubusercontent.com/thinh-vu/vnstock/beta/data/listing_companies_enhanced-2023.csv'):
    df = pd.read_csv(path)
    return df

def listing_companies (live=False, source='Wifeed'):
    if live == True:
        if source == 'Wifeed':
            df = live_stock_list()
        elif source == 'SSI':
            df = organ_listing()
    elif live == False:
        df = offline_stock_list()
    return df

# COMPANY OVERVIEW
def company_overview (symbol):
    data = requests.get(f'https://apipubaws.tcbs.com.vn/tcanalysis/v1/ticker/{symbol}/overview').json()
    df = json_normalize(data)
    df = df[['ticker', 'exchange', 'industry', 'companyType',
            'noShareholders', 'foreignPercent', 'outstandingShare', 'issueShare',
            'establishedYear', 'noEmployees',  
            'stockRating', 'deltaInWeek', 'deltaInMonth', 'deltaInYear', 
            'shortName', 'industryEn', 'industryID', 'industryIDv2', 'website']]
    return df

# RECENTLY ADDED -------

def company_profile (symbol='TCB', headers=tcbs_headers):
    url = f"https://apipubaws.tcbs.com.vn/tcanalysis/v1/company/{symbol}/overview"
    response = requests.request("GET", url, headers=headers, data={}).json()
    df = json_normalize(response)
    df['ticker'] = symbol
    for col in df.columns:
        try:
            df[col] = df[col].apply(lambda x: BeautifulSoup(x, 'html.parser').get_text())
            df[col] = df[col].str.replace('\n', ' ')
        except:
            pass
    return df

def company_large_shareholders (symbol='TCB', headers=tcbs_headers):
    url = f"https://apipubaws.tcbs.com.vn/tcanalysis/v1/company/{symbol}/large-share-holders"
    response = requests.request("GET", url, headers=headers, data={}).json()
    df = json_normalize(response['listShareHolder'])
    df['ticker'] = symbol
    df.rename(columns={'name': 'shareHolder', 'ownPercent': 'shareOwnPercent'}, inplace=True)
    df.drop(columns=['no'], inplace=True)
    return df

def company_fundamental_ratio (symbol='TCB', mode='simplify', missing_pct=0.8, headers=tcbs_headers):
    url = f"https://apipubaws.tcbs.com.vn/tcanalysis/v1/finance/{symbol}/tooltip"
    response = requests.request("GET", url, headers=headers, data={}).json()
    df = json_normalize(response)
    df['ticker'] = symbol
    cols = df.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df = df[cols]
    if mode == 'simplify':
        df = df.loc[:,~df.columns.str.contains('Name')]
    df = df.loc[:, df.isnull().mean() < missing_pct]
    return df

def ticker_price_volatility (symbol='TCB', headers=tcbs_headers):
    url = f"https://apipubaws.tcbs.com.vn/tcanalysis/v1/ticker/{symbol}/price-volatility"
    response = requests.request("GET", url, headers=headers, data={}).json()
    df = json_normalize(response)
    df.columns = ['ticker_' + col if col != 'ticker' else col for col in df.columns]
    return df

def company_insider_deals (symbol='TCB', page_size=20, page=0, headers=tcbs_headers):
    url = f"https://apipubaws.tcbs.com.vn/tcanalysis/v1/company/{symbol}/insider-dealing?page={page}&size={page_size}"
    response = requests.request("GET", url, headers=headers, data={}).json()
    df = json_normalize(response['listInsiderDealing'])
    df.drop(columns=['no'], inplace=True)
    df.rename(columns={'anDate': 'dealAnnounceDate', 'dealingMethod': 'dealMethod', 'dealingAction': 'dealAction', 'quantity': 'dealQuantity', 'price': 'dealPrice', 'ratio': 'dealRatio'}, inplace=True)
    df['dealAnnounceDate'] = pd.to_datetime(df['dealAnnounceDate'], format='%d/%m/%y')
    df.sort_values(by='dealAnnounceDate', ascending=False, inplace=True)
    df['dealMethod'].replace({1: 'Cổ đông lớn', 2: 'Cổ đông sáng lập', 0: 'Cổ đông nội bộ'}, inplace=True)
    df['dealAction'].replace({'1': 'Bán', '0': 'Mua'}, inplace=True)
    return df


def company_subsidiaries_listing (symbol='TCB', page_size=100, page=0, headers=tcbs_headers):
    df_ls = []
    if page_size > 100:
        max_page = page_size // 100
        page_size = 100
        for page in range(max_page):
            try:
                url = f"https://apipubaws.tcbs.com.vn/tcanalysis/v1/company/{symbol}/sub-companies?page={page}&size={page_size}"
                response = requests.request("GET", url, headers=tcbs_headers, data={}).json()
                df = json_normalize(response['listSubCompany'])
                df_ls.append(df)
            except:
                print(f'Error getting data from page {page}')
                with open(f'{DB_APPDATA_PATH}/log/subsidiaries_error-{today}.txt', 'a') as f:
                        f.write(f'Error when getting subsidiaries data of {symbol} at page {page}\n')
                        f.close()
                continue
    else:
        url = f"https://apipubaws.tcbs.com.vn/tcanalysis/v1/company/{symbol}/sub-companies?page={page}&size={page_size}"
        response = requests.request("GET", url, headers=headers, data={}).json()
        df = json_normalize(response['listSubCompany'])
        df_ls.append(df)
    df = pd.concat(df_ls, ignore_index=True)
    df['ticker'] = symbol
    df.drop(columns=['no'], inplace=True)
    df.rename(columns={'companyName': 'subCompanyName', 'ownPercent': 'subOwnPercent'}, inplace=True)
    return df


def company_officers (symbol='TCB', page_size=20, page=0, headers=tcbs_headers):
    url = f"https://apipubaws.tcbs.com.vn/tcanalysis/v1/company/{symbol}/key-officers?page={page}&size={page_size}"
    response = requests.request("GET", url, headers=headers, data={}).json()
    df = json_normalize(response['listKeyOfficer'])
    df['ticker'] = symbol
    df.drop(columns=['no'], inplace=True)
    df.rename(columns={'name': 'officerName', 'position': 'officerPosition', 'ownPercent':'officerOwnPercent'}, inplace=True)
    df.sort_values(by=['officerOwnPercent', 'officerPosition'], ascending=False, inplace=True)
    return df


def company_events (symbol='TPB', page_size=15, page=0, headers=tcbs_headers):
    url = f"https://apipubaws.tcbs.com.vn/tcanalysis/v1/ticker/{symbol}/events-news?page={page}&size={page_size}"
    response = requests.request("GET", url, headers=headers, data={}).json()
    df = pd.DataFrame(response['listEventNews'])
    return df

def company_news (symbol='TCB', page_size=15, page=0, headers=tcbs_headers):
    url = f"https://apipubaws.tcbs.com.vn/tcanalysis/v1/ticker/{symbol}/activity-news?page={page}&size={page_size}"
    response = requests.request("GET", url, headers=headers, data={}).json()
    df = pd.DataFrame(response['listActivityNews'])
    df['ticker'] = symbol
    return df

# FINANCIAL REPORT
## Financial report from SSI
def financial_report (symbol='SSI', report_type='BalanceSheet', frequency='Quarterly', headers=ssi_headers): 
    symbol = symbol.upper()
    organ_code = organ_listing().query(f'ticker == @symbol')['organCode'].values[0]
    url = f'https://fiin-fundamental.ssi.com.vn/FinancialStatement/Download{report_type}?language=vi&OrganCode={organ_code}&Skip=0&Frequency={frequency}'
    response = requests.get(url, headers=headers)
    status = response.status_code
    if status == 200:
        df = pd.read_excel(BytesIO(response.content), skiprows=7).dropna()
        return df
    else:
        print(f'Error {status} when getting data from SSI. Details:\n {response.text}')
        return None

## report from TCBS
def financial_flow(symbol='TCB', report_type='incomestatement', report_range='quarterly', get_all=True): 
    if report_range == 'yearly':
        range = 1
    elif report_range == 'quarterly':
        range = 0
    data = requests.get(f'https://apipubaws.tcbs.com.vn/tcanalysis/v1/finance/{symbol}/{report_type}', params={'yearly': range, 'isAll': get_all}).json()
    df = json_normalize(data)
    df[['year', 'quarter']] = df[['year', 'quarter']].astype(str)
    if report_range == 'yearly':
        df['index'] = df['year']
    elif report_range == 'quarterly':
        df['index'] = df['year'].str.cat('-Q' + df['quarter'])
    df = df.set_index('index').drop(columns={'year', 'quarter'})
    return df

def financial_ratio_compare (symbol_ls=["CTG", "TCB", "ACB"], industry_comparison=True, frequency='Yearly', start_year=2010, headers=ssi_headers): 
    global timeline
    if frequency == 'Yearly':
        timeline = str(start_year) + '_5'
    elif frequency == 'Quarterly':
        timeline = str(start_year) + '_4'

    list_len = len(symbol_ls)
    if list_len == 1:
        url = f'https://fiin-fundamental.ssi.com.vn/FinancialAnalysis/DownloadFinancialRatio2?language=vi&OrganCode={symbol_ls[0]}&CompareToIndustry={industry_comparison}&Frequency={frequency}&Ratios=ryd21&Ratios=ryd25&Ratios=ryd14&Ratios=ryd7&Ratios=rev&Ratios=isa22&Ratios=ryq44&Ratios=ryq14&Ratios=ryq12&Ratios=rtq51&Ratios=rtq50&Ratios=ryq48&Ratios=ryq47&Ratios=ryq45&Ratios=ryq46&Ratios=ryq54&Ratios=ryq55&Ratios=ryq56&Ratios=ryq57&Ratios=nob151&Ratios=casa&Ratios=ryq58&Ratios=ryq59&Ratios=ryq60&Ratios=ryq61&Ratios=ryd11&Ratios=ryd3&TimeLineFrom={timeline}'.format(symbol_ls[0], industry_comparison, '', frequency, timeline)
    elif  list_len > 1:
        main_symbol = symbol_ls[0]
        company_join = '&CompareToCompanies=' + '&CompareToCompanies='.join(symbol_ls[1:])
        url = f'https://fiin-fundamental.ssi.com.vn/FinancialAnalysis/DownloadFinancialRatio2?language=vi&OrganCode={main_symbol}&CompareToIndustry={industry_comparison}{company_join}&Frequency={frequency}&Ratios=ryd21&Ratios=ryd25&Ratios=ryd14&Ratios=ryd7&Ratios=rev&Ratios=isa22&Ratios=ryq44&Ratios=ryq14&Ratios=ryq12&Ratios=rtq51&Ratios=rtq50&Ratios=ryq48&Ratios=ryq47&Ratios=ryq45&Ratios=ryq46&Ratios=ryq54&Ratios=ryq55&Ratios=ryq56&Ratios=ryq57&Ratios=nob151&Ratios=casa&Ratios=ryq58&Ratios=ryq59&Ratios=ryq60&Ratios=ryq61&Ratios=ryd11&Ratios=ryd3&TimeLineFrom={timeline}'
    r = requests.get(url, headers=headers)
    df = pd.read_excel(BytesIO(r.content), skiprows=7)
    df = df.dropna(how='all')
    df = df[~df['Chỉ số'].str.contains('Dữ liệu được cung cấp bởi FiinTrade')]
    df = df[~df['Chỉ số'].str.contains('https://fiintrade.vn/')]
    return df


# STOCK FILTERING

def financial_ratio (symbol, report_range, is_all=False):
    if report_range == 'yearly':
        x = 1
    elif report_range == 'quarterly':
        x = 0
    
    if is_all == True:
      y = 'true'
    else:
      y = 'false'

    data = requests.get(f'https://apipubaws.tcbs.com.vn/tcanalysis/v1/finance/{symbol}/financialratio?yearly={x}&isAll={y}').json()
    df = json_normalize(data)
    df = df.dropna(axis=1, how='all')
    if report_range == 'yearly':
        df = df.set_index('year').drop(columns={'quarter'})
    elif report_range == 'quarterly':
        df['quarter'] = 'Q' + df['quarter'].astype(str)
        df['range'] = df['quarter'].str.cat(df['year'].astype(str), sep='-')
        df = df[['range'] + [col for col in df.columns if col != 'range']]
        df = df.set_index('range')
    df = df.T
    return df


def dividend_history (symbol):
    data = requests.get('https://apipubaws.tcbs.com.vn/tcanalysis/v1/company/{}/dividend-payment-histories?page=0&size=20'.format(symbol)).json()
    df = json_normalize(data['listDividendPaymentHis']).drop(columns=['no', 'ticker'])
    return df


## STOCK RATING
def  general_rating (symbol):
    data = requests.get('https://apipubaws.tcbs.com.vn/tcanalysis/v1/rating/{}/general?fType=TICKER'.format(symbol)).json()
    df = json_normalize(data).drop(columns='stockRecommend')
    return df

def biz_model_rating (symbol):
    data = requests.get('https://apipubaws.tcbs.com.vn/tcanalysis/v1/rating/{}/business-model?fType=TICKER'.format(symbol)).json()
    df = json_normalize(data)
    return df

def biz_operation_rating (symbol):
    data = requests.get('https://apipubaws.tcbs.com.vn/tcanalysis/v1/rating/{}/business-operation?fType=TICKER'.format(symbol)).json()
    df = json_normalize(data)
    return df

def financial_health_rating (symbol):
    data = requests.get('https://apipubaws.tcbs.com.vn/tcanalysis/v1/rating/{}/financial-health?fType=TICKER'.format(symbol)).json()
    df = json_normalize(data)
    return df


def valuation_rating (symbol):
    data = requests.get('https://apipubaws.tcbs.com.vn/tcanalysis/v1/rating/{}/valuation?fType=TICKER'.format(symbol)).json()
    df = json_normalize(data)
    return df


def industry_financial_health (symbol):
    data = requests.get('https://apipubaws.tcbs.com.vn/tcanalysis/v1/rating/{}/financial-health?fType=INDUSTRY'.format(symbol)).json()
    df = json_normalize(data)
    return df


def stock_evaluation (symbol='ACB', period=1, time_window='D', headers=tcbs_headers):
    url = f"https://apipubaws.tcbs.com.vn/tcanalysis/v1/evaluation/{symbol}/historical-chart?period={period}&tWindow={time_window}"
    response = requests.get(url, headers=headers).json()
    df = pd.DataFrame(response['data'])
    df.rename(columns={'pe': 'PE', 'pb': 'PB', 'industryPe': 'industryPE', 'industryPb': 'industryPB', 'indexPe': 'vnindexPE', 'indexPb': 'vnindexPB', 'from': 'fromDate', 'to': 'toDate'}, inplace=True)
    df['ticker'] = symbol
    df = df[['ticker', 'fromDate', 'toDate', 'PE', 'PB', 'industryPE', 'vnindexPE', 'industryPB', 'vnindexPB']]
    df['fromDate'] = pd.to_datetime(df['fromDate'])
    df['toDate'] = pd.to_datetime(df['toDate'])
    return df