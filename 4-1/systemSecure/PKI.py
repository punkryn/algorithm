from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import pickle

def genCertificate(myPubKey, CAPrivKey):
    myPubKey = str(myPubKey).encode('utf8')
    h = SHA256.new(myPubKey)
    signature = pkcs1_15.new(CAPrivKey).sign(h)

    return [myPubKey, signature]

def veriCertificate(aCertificate, CACertificate):
    h = SHA256.new(str(aCertificate[0]).encode('utf8'))

    try:
        pkcs1_15.new(CACertificate[0]).verify(h, aCertificate[1])
        return True
    except(ValueError, TypeError):
        return False

# a.
CAPrivKey = RSA.generate(2048)
with open('CAPriv.pem', 'wb') as cppw:
    cppw.write(CAPrivKey.export_key('PEM', passphrase="CA"))

# b.
with open('CAPub.pem', 'wb') as cpupw:
    cpupw.write(CAPrivKey.publickey().export_key('PEM'))

# c.
with open('CAPub.pem', 'r') as cppr:
    CAPubkey = RSA.import_key(cppr.read())
with open('CAPriv.pem', 'r') as cappr:
    CAPrivateKey = RSA.import_key(cappr.read(), passphrase="CA")

with open('CACertCA.plk', 'wb') as cpw:
    pickle.dump(genCertificate(CAPubkey, CAPrivKey), cpw)

# d.
BobPrivKey = RSA.generate(2048)
with open('BobPriv.pem', 'wb') as bppw:
    bppw.write(BobPrivKey.export_key('PEM', passphrase="Bo"))

# e.
with open('BobPub.pem', 'wb') as bpupw:
    bpupw.write(BobPrivKey.publickey().export_key('PEM'))

# f.
with open('BobPub.pem', 'r') as bpupr:
    Bob_pub = RSA.import_key(bpupr.read())

with open('BobCertCA.plk', 'wb') as bccpw:
    pickle.dump(genCertificate(Bob_pub, CAPrivateKey), bccpw)

# g.
M = "I bought 100 doge coins."
h = SHA256.new(M.encode('utf8'))

with open('BobPriv.pem', 'r') as bppr:
    bobPrivateKey = RSA.import_key(bppr.read(), passphrase="Bo")
    Bobsignature = pkcs1_15.new(bobPrivateKey).sign(h)

with open('BobCertCA.plk', 'rb') as bccpr:
    Bob_pub2, S_Bob_CA = pickle.load(bccpr)
    print("Bob sent (", M, Bobsignature, [Bob_pub, S_Bob_CA], ") to Alice.")

# h.
# i.
with open('CACertCA.plk', 'rb') as cccpr:
    rootCert = pickle.load(cccpr)
    CA_pub, S_CA = rootCert

# j.
with open('CAPriv.pem', 'r') as cppr:
    CAPrivateKey = RSA.import_key(cppr.read(), passphrase="CA")

    h = SHA256.new(str(CA_pub).encode('utf8'))
    sig = pkcs1_15.new(CAPrivateKey).sign(h)

h = SHA256.new(str(CAPubkey).encode('utf8'))
signature = pkcs1_15.new(CAPrivKey).sign(h)

if veriCertificate([CA_pub, sig], [CAPubkey, signature]):
    print("verified")
else:
    print("fail")

# k.
with open('CAPriv.pem', 'r') as cppr:
    CAPrivateKey = RSA.import_key(cppr.read(), passphrase="CA")
    h = SHA256.new(str(Bob_pub).encode('utf8'))
    sig = pkcs1_15.new(CAPrivateKey).sign(h)

if veriCertificate([Bob_pub, sig], [CAPubkey, signature]):
    print("Bob verified")
else:
    print("Bob fail")

# i.
if veriCertificate([M, Bobsignature], [Bob_pub, Bobsignature]):

    print("Message verified")
else:
    print("Message fail")

# m.
print("Good job. Well done !")