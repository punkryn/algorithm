from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

with open('AlicePubKey.pem', 'r') as apukr:
    AlicePubKey = RSA.import_key(apukr.read())

with open('message', 'r') as mr:
    message = mr.read()

with open('signature', 'rb') as sr:
    signature = sr.read()

print("Bob received message (", message, signature, ")from Alice")
h = SHA256.new(message.encode('utf-8'))
try:
    pkcs1_15.new(AlicePubKey).verify(h, signature)
    print("The signature is valid")
except(ValueError, TypeError):
    print("the signature is not valid.")