from .utils import *
import pandas as pd
import requests
from pandas import json_normalize
from io import BytesIO
import time
from datetime import datetime, timedelta
import json

ssi_headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'DNT': '1',
        'sec-ch-ua-mobile': '?0',
        'X-Fiin-Key': 'KEY',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-Fiin-User-ID': 'ID',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'X-Fiin-Seed': 'SEED',
        'sec-ch-ua-platform': 'Windows',
        'Origin': 'https://iboard.ssi.com.vn',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://iboard.ssi.com.vn/',
        'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7'
        }

entrade_headers = {
  'authority': 'services.entrade.com.vn',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9',
  'dnt': '1',
  'origin': 'https://banggia.dnse.com.vn',
  'referer': 'https://banggia.dnse.com.vn/',
  'sec-ch-ua': '"Edge";v="114", "Chromium";v="114", "Not=A?Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'cross-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1788.0'
}

tcbs_headers = {
  'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
  'DNT': '1',
  'Accept-language': 'vi',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Referer': 'https://tcinvest.tcbs.com.vn/',
  'sec-ch-ua-platform': '"Windows"'
}

vps_headers = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'en-US,en;q=0.9',
  'Connection': 'keep-alive',
  'DNT': '1',
  'Origin': 'https://banggia.vps.com.vn',
  'Referer': 'https://banggia.vps.com.vn/',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-site',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

fmarket_headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "vi",
    "content-type": "application/json",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "referrer": "https://fmarket.vn/"
}

rv_cookie = 'RV08835624=080035c91e77d96a1dcd7d9668d15032dca1c5c44e92ef5bbacedcc05701ff85c9486d38fb81e83857d5672616b9e3546504ee4846; _ga_KN4YPTLVCF=GS1.1.1690211515.1.0.1690211515.0.0.0; _gid=GA1.3.1634163694.1690211515; _gat_gtag_UA_120090926_1=1; _fbp=fb.2.1690211516077.1111198076; JSESSIONID=BFEB38A8B8419EEEC39DF45490E1B22D; vdsc-liv=\u00210CIhC2srW+VXY3rGJTT3LEhTmJvzwWLF5bKAMvgEjULUV+lBtkyTYFCLv7njgHRB4TgCdXik8NDWPQ==; hideMarketChartCKName=0; allCustomGroupsCkName=ALL_DEFAULT_GROUP_ID%23%23%23%23%23%23%23%23CTD%3BDHG%3BDRC%3BFPT%3BHPG%3BHSG%3BKDC%3BMWG%3BNT2%3BPAC%3BPC1%3BPNJ%3BTAC%3BVCB%3BVDS%3BVGC%3BVJC%3BVNM%3B%23%23%23%23%23%23%23%23T%C3%B9y%20ch%E1%BB%8Dn; rv_avraaaaaaaaaaaaaaaa_session_=DPHJFAEBJMBKENBPDOLDBOKIJCPLBLGFPHHGOCJEHFLMNGOGJINNIAOOIOPCNEILMDODFNCOCEGJIMDEHDNABIPKIJNKFFJCBEHPHADOFOLCEJEFFABNAAMIOLLMAEFI; _ga=GA1.1.1224611093.1690211515; _ga_D36ML1235R=GS1.1.1690211525.1.1.1690211543.0.0.0; RV9cd20160034=08557ab163ab2000054ec4478471ef19572f6aa45f46e6023a0505610ff398cf65052602d337f301084048ab69113000c7d3b36391060024abdc7de0506ec20cf57eadcbff388725325c25c6632a4cbda9a1e282112bd2a9d7d1e1c4471b850a'

rv_headers = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Accept-Language': 'en-US,en;q=0.9',
  'Connection': 'keep-alive',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'DNT': '1',
  'Origin': 'https://livedragon.vdsc.com.vn',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1788.0',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua': '"Edge";v="114", "Chromium";v="114", "Not=A?Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

fmarket_headers = {
  'authority': 'api.fmarket.vn',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'vi',
  'content-type': 'application/json',
  'dnt': '1',
  'origin': 'https://fmarket.vn',
  'referer': 'https://fmarket.vn/',
  'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

def api_request(url, headers=ssi_headers):
    r = requests.get(url, headers).json()
    return r


today_val = datetime.now()

def today():
    today = today_val.strftime('%Y-%m-%d')
    return today

def last_xd (day_num): 
    last_xd = (today_val - timedelta(day_num)).strftime('%Y-%m-%d')
    return last_xd

def start_xm (period): 
    date = pd.date_range(end=today, periods=period+1, freq='MS')[0].strftime('%Y-%m-%d')
    return date