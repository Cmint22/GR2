from datetime import datetime, timedelta
import os
import platform

def get_date(n, unit):
    if unit == 'day':
        return (datetime.now() - timedelta(days=n)).strftime('%Y-%m-%d')
    elif unit == 'month':
        return (datetime.now() - relativedelta(months=n)).strftime('%Y-%m-%d')
    elif unit == 'year':
        return (datetime.now() - relativedelta(years=n)).strftime('%Y-%m-%d')

def get_username():
    try:
        username = os.getlogin()
        return username
    except OSError as e:
        print(f"Error: {e}")
        return None
    
def get_os():
    try:
        os = platform.system()
        return os
    except OSError as e:
        print(f"Error: {e}")
        return None

def get_cwd():
    try:
        cwd = os.getcwd()
        return cwd
    except OSError as e:
        print(f"Error: {e}")
        return None

def get_path_delimiter():
    return '\\' if os.name == 'nt' else '/'
