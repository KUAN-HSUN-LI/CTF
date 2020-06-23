from pwn import *  # pip install pwntools
import json
import base64
import codecs
from Crypto.Util.number import bytes_to_long, long_to_bytes
r = remote('socket.cryptohack.org', 13377, level='debug')


def json_recv():
    line = r.recvline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


def decode(encoding, encoded_str):
    decoded_str = ""

    if encoding == "base64":
        decoded_str = base64.b64decode(encoded_str).decode()
    elif encoding == "hex":
        decoded_str = bytes.fromhex(encoded_str).decode('utf-8')
    elif encoding == "rot13":
        decoded_str = codecs.decode(encoded_str, 'rot13')
    elif encoding == "bigint":
        print(encoded_str)
        decoded_str = long_to_bytes(int(encoded_str, 16)).decode()
    elif encoding == "utf-8":
        decoded_str = ''.join([chr(b) for b in encoded_str])
    return decoded_str


for i in range(101):
    received = json_recv()
    print("Received type: ", received["type"])
    print("Received encoded value: ", received["encoded"])
    encoding = received["type"]
    encoded_str = received["encoded"]

    to_send = {
        "decoded": decode(encoding, encoded_str)
    }
    json_send(to_send)
