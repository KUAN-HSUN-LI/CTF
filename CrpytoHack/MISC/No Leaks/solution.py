from pwn import *
import json
import base64
r = remote("socket.cryptohack.org", 13370)


def json_recv():
    line = r.recvline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


mis_data = [set() for i in range(20)]
received = r.recvline()
print(received)
to_send = {"msg": "request"}
num = 0
while True:
    cnt = 0
    num += 1
    json_send(to_send)
    received = json_recv()
    if "error" in received:
        continue
    msg = base64.b64decode(received['ciphertext'].encode())
    for idx, c in enumerate(msg):
        mis_data[idx].add(c)
    for i in range(20):
        print(len(mis_data[i]), end=' ')
        if len(mis_data[i]) >= 255:
            cnt += 1
    print()
    print(num, cnt)
    if cnt == 20:
        break
for s in mis_data:
    for i in range(256):
        if i not in s:
            print(chr(i), end='')
            break
