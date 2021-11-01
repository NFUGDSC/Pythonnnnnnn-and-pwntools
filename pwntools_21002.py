from pwn import *

r = remote('140.130.34.35', 21002)# ip,port
s = r.recvline()
while s!='\n':
    print(chr(int(s)),end="")
    s=r.recvline()

r.interactive()
