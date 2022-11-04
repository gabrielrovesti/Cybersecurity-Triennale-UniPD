#original data: "El Psy Congroo"
#encrypted data: "IFhiPhZNYi0KWiUcCls="
#encrypted flag: "I3gDKVh1Lh4EVyMDBFo="
#
#The flag is a composition of two names (two animals (?)).

import base64

original_data = "El Psy Congroo"
encrypted_data="IFhiPhZNYi0KWiUcCls="
encrypted_flag="I3gDKVh1Lh4EVyMDBFo="

decrypted_data=base64.b64decode(encrypted_data).decode('utf-8', errors="ignore")
decrypted_flag=base64.b64decode(encrypted_flag).decode('utf-8', errors="ignore")

#Given the hint from the text, we know the flag is a composition of two names. 
#We might try to xor the two names together to get the flag.
#This data that needs to be xor'd is the original data and the decrypted data.

def xor(a, b):
    result=''.join([chr(ord(x) ^ ord(y)) for (x,y) in zip(a,b)])
    return result

key=xor(original_data, decrypted_data)
flag=xor(decrypted_flag, key)
print(flag)
