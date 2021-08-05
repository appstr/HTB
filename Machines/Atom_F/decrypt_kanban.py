from des import *
import pybase64

#passwd_1 = b'Odh7N3L9aVSeHQmgK/nj7RQL8MEYCUMb'
passwd_2 = b'Odh7N3L9aVQ8/srdZgG2hIR0SSJoJKGi'

passwd = pybase64.b64decode(passwd_2, altchars='_:', validate=True)
key = DesKey(b'7ly6UznJ')
iv = b'XuVUm5fR'

decrypted_passwd = key.decrypt(passwd, initial=iv, padding=True)
print(decrypted_passwd)
