import requests  # pip install requests

raw_url = 'http://aes.cryptohack.org/ecb_oracle/encrypt/'
ans_lst = "63727970746f7b70336e3675316e35"
table = [i for i in range(97, 128)] + [i for i in range(48, 97)] + [i for i in range(32, 48)]
for num in range(16, 0, -1):
    url = raw_url + "00" * num
    r = requests.get(url)
    ans = r.json()['ciphertext'][32:64]
    print(ans)
    for idx, i in enumerate(table):
        print(idx, end='\r')
        res = requests.get(url + ans_lst + hex(i)[2:])
        if res.json()['ciphertext'][32:64] == ans:
            ans_lst += hex(i)[2:]
            print(ans_lst)
            break
