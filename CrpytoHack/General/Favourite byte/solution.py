s = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
to_bytes = bytes.fromhex(s)
for i in range(256):
    ans = ""
    for e in to_bytes:
        ans = ans + chr(i ^ e)
    if ans.find("crypto") >= 0:
        print(ans)
