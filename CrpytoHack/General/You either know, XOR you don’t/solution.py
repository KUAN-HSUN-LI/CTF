q = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
b = bytes.fromhex(q)
# key = "crypto{"
# for i in range(7):
#     for num in range(256):
#         c = chr(b[i] ^ num)
#         if c == key[i]:
#             print(chr(num))
# key = "}"
# for num in range(256):
#     c = chr(b[-1] ^ num)
#     if c == key:
#         print(chr(num))

key = "myXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkey"
ans = ""
for e, i in zip(b, key):
    ans = ans + chr(e ^ ord(i))

print(ans)
