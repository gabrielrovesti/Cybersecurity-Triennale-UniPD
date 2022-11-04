#Julius,Q2Flc2FyCg==
#-------------------
#
#World of Cryptography is like that Unsolved Rubik's Cube, given to a child that has no idea about it. A new combination at every turn.
#
#Can you solve this one, with weird name?
#
#ciphertext: fYZ7ipGIjFtsXpNLbHdPbXdaam1PS1c5lQ==

import base64

ciphertext = 'fYZ7ipGIjFtsXpNLbHdPbXdaam1PS1c5lQ=='
#We can see the string is a base64 one, so we define a function to decode it

def base64decode(text):
    return str(base64.b64decode(text).decode('ascii', 'ignore'))

decoded=base64decode(ciphertext)
print(decoded)
# As of now, we have this kind of string:
# b'}\x86{\x8a\x91\x88\x8c[l^\x93KlwOmwZjmOKW9\x95' (25 characters in total)
# Let's try to implement a bruteforce algorithm in order to decrypt it
flag = ''
for i in range(len(decoded)):
    code = ord(decoded[i]) - 24
    flag += chr(code)

print(flag)
