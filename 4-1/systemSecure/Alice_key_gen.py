from Crypto.PublicKey import RSA

AlicePrivKey = RSA.generate(2048)
with open('AlicePrivKey.pem', 'wb') as apkw:
    apkw.write(AlicePrivKey.export_key('PEM', passphrase="!@#$"))

with open('AlicePubKey.pem', 'wb') as apukw:
    apukw.write(AlicePrivKey.publickey().export_key('PEM'))

