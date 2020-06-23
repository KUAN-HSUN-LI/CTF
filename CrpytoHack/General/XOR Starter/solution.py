s = "label"
out = ''.join([chr(ord(c) ^ 13) for c in s])
print(out)
