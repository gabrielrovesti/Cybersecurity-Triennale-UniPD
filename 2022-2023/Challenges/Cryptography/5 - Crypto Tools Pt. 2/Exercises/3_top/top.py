#!/usr/bin/env python3
import random
import sys
import time

cur_time = str(time.time()).encode('ASCII')
random.seed(cur_time)

msg = input('Your message: ').encode('ASCII')
key = [random.randrange(256) for _ in msg]
c = [m ^ k for (m,k) in zip(msg + cur_time, key + [0x88]*len(cur_time))] 
# 0x88 is the key for the last 4 bytes of the time and as a symbol is ^

with open(sys.argv[0], "wb") as f:
    f.write(bytes(c))
