import pickle
import binascii
from pwn import *

with open("t.pkl", "rb") as f:
    d = pickle.load(f)


def recv_data():
    recv = r.recvline()
    print(recv)
    return recv


def send(num):
    n = 2 ** (num % 4)
    pos = 96 - num // 4
    msg = "0" * (pos - 1) + str(n) + "0" * (96 - pos)
    r.sendline(msg)


r = remote("challs.m0lecon.it", "11000")
recv = r.recvline()
print(recv)
s = recv.strip().split()[-1][:-1].decode()
r.sendline(str(d[s]))
recv = r.recvline()
print(recv)
encrypt_chall = r.recvline().decode().strip()
print(encrypt_chall)
secret = [-1] * 128
for i in range(128):
    if (127 - i) in secret:
        continue
    recv_data()
    recv_data()
    recv_data()
    r.sendline("1")
    recv = recv_data()
    send(i)
    recv_temp = recv_data()
    recv_temp = b"0" * (193 - len(recv_temp)) + recv_temp
    recv = recv_temp[128:160]
    pos1 = 0
    if recv.find(b"1") >= 0:
        pos1 = recv.find(b"1") * 4 + 3
    elif recv.find(b"2") >= 0:
        pos1 = recv.find(b"2") * 4 + 2
    elif recv.find(b"4") >= 0:
        pos1 = recv.find(b"4") * 4 + 1
    elif recv.find(b"8") >= 0:
        pos1 = recv.find(b"8") * 4
    secret[pos1] = 127 - i
    recv = recv_temp[96:128]
    pos2 = 0
    if recv.find(b"1") >= 0:
        pos2 = recv.find(b"1") * 4 + 3
    elif recv.find(b"2") >= 0:
        pos2 = recv.find(b"2") * 4 + 2
    elif recv.find(b"4") >= 0:
        pos2 = recv.find(b"4") * 4 + 1
    elif recv.find(b"8") >= 0:
        pos2 = recv.find(b"8") * 4
    secret[pos2] = pos1
    recv = recv_temp[64:96]
    pos3 = 0
    if recv.find(b"1") >= 0:
        pos3 = recv.find(b"1") * 4 + 3
    elif recv.find(b"2") >= 0:
        pos3 = recv.find(b"2") * 4 + 2
    elif recv.find(b"4") >= 0:
        pos3 = recv.find(b"4") * 4 + 1
    elif recv.find(b"8") >= 0:
        pos3 = recv.find(b"8") * 4
    secret[pos3] = pos2
    recv = recv_temp[32:64]
    pos4 = 0
    if recv.find(b"1") >= 0:
        pos4 = recv.find(b"1") * 4 + 3
    elif recv.find(b"2") >= 0:
        pos4 = recv.find(b"2") * 4 + 2
    elif recv.find(b"4") >= 0:
        pos4 = recv.find(b"4") * 4 + 1
    elif recv.find(b"8") >= 0:
        pos4 = recv.find(b"8") * 4
    secret[pos4] = pos3
    recv = recv_temp[:32]
    pos5 = 0
    if recv.find(b"1") >= 0:
        pos5 = recv.find(b"1") * 4 + 3
    elif recv.find(b"2") >= 0:
        pos5 = recv.find(b"2") * 4 + 2
    elif recv.find(b"4") >= 0:
        pos5 = recv.find(b"4") * 4 + 1
    elif recv.find(b"8") >= 0:
        pos5 = recv.find(b"8") * 4
    secret[pos5] = pos4
print(secret, encrypt_chall)
for i in range(9):
    encrypt_chall1 = encrypt_chall[:32]
    encrypt_chall2 = encrypt_chall[32:64]
    bin_chall2 = bin(int(encrypt_chall2, 16))[2:].rjust(128, '0')
    chaos_chall2 = int(''.join([str(bin_chall2[i]) for i in secret]), 2)
    new_chall2 = hex(int(encrypt_chall1, 16) ^ chaos_chall2)[2:]
    encrypt_chall = encrypt_chall[32:] + new_chall2
print(encrypt_chall)
recv_data()
recv_data()
recv_data()
r.sendline("2")
recv = recv_data()
r.sendline(binascii.unhexlify(encrypt_chall.encode()).decode())
recv = recv_data()
recv = recv_data()
recv = recv_data()
