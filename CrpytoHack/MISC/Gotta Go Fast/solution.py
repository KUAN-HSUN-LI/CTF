from Crypto.Util.number import long_to_bytes
import hashlib

flag = bytes.fromhex("7a2e5634fb7bd72680249c30ba37f28db71c2c410e6d66fcd2360495")
current_time = 1589821901
key = long_to_bytes(current_time)
key = hashlib.sha256(key).digest()
plaintext = b''
print(len(flag))
print(len(key))
for i in range(len(flag)):
    plaintext += bytes([flag[i] ^ key[i]])
print(plaintext)
