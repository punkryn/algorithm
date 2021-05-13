from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

with open('AlicePrivKey.pem', 'r') as apkr:
    AlicePrivKey = RSA.import_key(apkr.read(), passphrase="!@#$")

message = 'To be signed'
h = SHA256.new(message.encode('utf-8'))
signature = pkcs1_15.new(AlicePrivKey).sign(h)
print("Alice sent (", message, signature, ") to Bob.")

with open('message', 'w') as mes:
    mes.write(message)

with open('signature', 'wb') as sig:
    sig.write(signature)