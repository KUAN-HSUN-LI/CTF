with open("output.txt", "r") as f:
    key = eval(f.read())
p = 1007621497415251

for i in range(0, 224, 8):
    ans_arr = bytes()
    for j in range(8):
        if pow(key[i+j], (p-1)//2, p) == 1:
            ans_arr += b'1'
        else:
            ans_arr += b'0'
    print(chr(int(ans_arr, 2)), end="")
print()
