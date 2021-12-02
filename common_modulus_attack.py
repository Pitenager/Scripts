from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes, inverse
 
def bezout(a, b):
    old_r = a
    r = b
    old_s = 1
    s = 0
    old_t = 0
    t = 1
 
    while (r != 0):
            q = old_r // r
            tmp_r = r
            r = old_r - q * tmp_r
            old_r = tmp_r
            tmp_s = s
            s = old_s - q * tmp_s
            old_s = tmp_s
            tmp_t = t
            t = old_t - q * tmp_t
            old_t = tmp_t
 
    return (old_s, old_t, old_r)
 
 
key1 = "./pub1.pem"
key2 = "./pub2.pem"
 
c_1 = 0x55cfe232610aa54dffcfb346117f0a38c77a33a2c67addf7a0368c93ec5c3e1baec9d3fe35a123960edc2cbdc238f332507b044d5dee1110f49311efc55a2efd3cf041bfb27130c2266e8dc61e5b99f275665823f584bc6139be4c153cdcf153bf4247fb3f57283a53e8733f982d790a74e99a5b10429012bc865296f0d4f408f65ee02cf41879543460ffc79e84615cc2515ce9ba20fe5992b427e0bbec6681911a9e6c6bbc3ca36c9eb8923ef333fb7e02e82c7bfb65b80710d78372a55432a1442d75cad5b562209bed4f85245f0157a09ce10718bbcef2b294dffb3f00a5a804ed7ba4fb680eea86e366e4f0b0a6d804e61a3b9d57afb92ecb147a769874
c_2 = 0x79834ce329453d3c4af06789e9dd654e43c16a85d8ba0dfa443aefe1ab4912a12a43b44f58f0b617662a459915e0c92a2429868a6b1d7aaaba500254c7eceba0a2df7144863f1889fab44122c9f355b74e3f357d17f0e693f261c0b9cefd07ca3d1b36563a8a8c985e211f9954ce07d4f75db40ce96feb6c91211a9ff9c0a21cad6c5090acf48bfd88042ad3c243850ad3afd6c33dd343c793c0fa2f98b4eabea399409c1966013a884368fc92310ebcb3be81d3702b936e7e883eeb94c2ebb0f9e5e6d3978c1f1f9c5a10e23a9d3252daac87f9bb748c961d3d361cc7dacb9da38ab8f2a1595d7a2eba5dce5abee659ad91a15b553d6e32d8118d1123859208
 
with open(key1, 'r') as key1:
    pub1 = RSA.import_key(key1.read())
 
with open(key2, 'r') as key2:
    pub2 = RSA.import_key(key2.read())
 
(x, y, z) = bezout(pub1.e, pub2.e)
 
if x < 0:
    c_1 = inverse(c_1, pub1.n)
    x = -x
if y < 0:
    c_2 = inverse(c_2, pub2.n)
    y = -y
    
m = (pow(c_1, x, pub1.n) * pow(c_2, y, pub1.n)) % pub1.n
 
flag = long_to_bytes(m)
 
print(flag.decode())
