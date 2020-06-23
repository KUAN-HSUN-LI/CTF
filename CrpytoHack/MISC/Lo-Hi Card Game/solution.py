from pwn import *
import json
import base64
from functools import total_ordering
import gmpy2
r = remote("socket.cryptohack.org", 13383)

VALUES = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
          'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
SUITS = ['Clubs', 'Hearts', 'Diamonds', 'Spades']


@total_ordering
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return VALUES.index(self.value) > VALUES.index(other.value)


def json_recv():
    line = r.recvline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


cnt = 0
pivot = Card("Seven", "Clubs")
deck = [Card(value, suit) for suit in SUITS for value in VALUES]


def random_send(card):
    if card > pivot:
        to_send = {"choice": "lower"}
    else:
        to_send = {"choice": "higher"}
    json_send(to_send)
    received = json_recv()
    print(received)
    v = received['hand'].split()[0]
    s = received['hand'].split()[2]
    return VALUES.index(v) + SUITS.index(s) * 13


def send(card, ans_card):
    if card > ans_card:
        to_send = {"choice": "lower"}
    else:
        to_send = {"choice": "higher"}
    json_send(to_send)
    received = json_recv()
    print(received)
    if "hand" not in received:
        return
    v = received['hand'].split()[0]
    s = received['hand'].split()[2]
    return VALUES.index(v) + SUITS.index(s) * 13


def rebase(n, b=52):
    if n < b:
        return [n]
    else:
        return [n % b] + rebase(n//b, b)


received = json_recv()
print(received)
v = received['hand'].split()[0]
s = received['hand'].split()[2]
card = Card(v, s)
s1 = VALUES.index(v) + SUITS.index(s) * 13
for i in range(10):
    card_num = random_send(card)
    card = deck[card_num]
    s1 = s1*52 + card_num
s2 = 0
for i in range(11):
    card_num = random_send(card)
    card = deck[card_num]
    s2 = s2*52 + card_num
s3 = 0
for i in range(11):
    card_num = random_send(card)
    card = deck[card_num]
    s3 = s3*52 + card_num
mod = 2**61 - 1
m = gmpy2.divm(s3 - s2, s2 - s1, mod)
i = s3 - ((s2 * m) % mod)
if i < 0:
    i += mod
s4 = (s3 * m + i) % mod

ans_lst = rebase(s4)
s = 0
cnt = 0
while True:
    cnt += 1
    ans_card = deck[ans_lst.pop()]
    card_num = send(card, ans_card)
    if card_num == None:
        break
    card = deck[card_num]
    s = s * 52 + card_num
    if cnt == 11:
        cnt = 0
        ans_lst = rebase((s * m + i) % mod)
        s = 0
