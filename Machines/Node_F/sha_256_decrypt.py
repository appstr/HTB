import subprocess

data = [
    {
        "username":	"myP14ceAdm1nAcc0uNT",
        "password":	"dffc504aa55359b9265cbebe1e4032fe600b64475ae3fd29c07d23223334d0af"
    },
    {
        "username":	"tom",
        "password":	"f0e2e750791171b0391b682ec35835bd6a5c3f7c8d1d0191451ec77b4d75f240"
    },
    {
        "username":	"mark",
        "password":	"de5a1adf4fedcce1533915edc60177547f1057b61b7119fd130e1f7428705f73"
    },
    {
        "username":	"rastating",
        "password":	"5065db2df0d4ee53562c650c29bacf55b97e231e3fe88570abc9edd8b78ac2f0"
    }
]

for d in data:
    username = d["username"]
    print(f'{username}: ')
    subprocess.Popen(['sudo', 'hashcat', '-m', '1400', f'{d["password"]}', '/usr/share/wordlists/rockyou.txt', '--show']).wait()
