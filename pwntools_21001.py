from pwn import *

r = remote('140.130.34.35', 21001)  # ip,port
r.recvuntil(b'\n')
for i in range(1000):   
    s = r.recvuntil(b'\n')
    print(s)
    q=s.split()
    ans=0
    if q[0]==b'Bye':
        break
    if q[1]==b'-':
        ans=int(q[0])-int(q[2])
    if q[1]==b'+':
        ans=int(q[0])+int(q[2])
    if q[1] == b'x':
        ans = int(q[0])*int(q[2])
    r.sendline(bytes(ans))

r.interactive()
