import base64

original_data = "El Psy Congroo"
encrypted_data = "IFhiPhZNYi0KWiUcCls="
encrypted_flag = "I3gDKVh1Lh4EVyMDBFo="
#we can note that all of the strings have the same lenght
#since we have an example of encryption, and we know that this is a xor,
#we can simply try to obtain the key in the example, and apply it to the
#crypted flag

def base64tostring(text):
    return base64.b64decode(text).decode('utf-8', errors="ignore")


#decode the encryption from base64
enc_data= base64tostring(encrypted_data)
enc_flag= base64tostring(encrypted_flag)

#we know apply the xor to obtain the key
key = ''.join([chr(ord(x) ^ ord(y))for x, y in zip(original_data, enc_data)])

print('key:\t',key)
#this seems a reasonalble key

flag = ''.join([chr(ord(x) ^ ord(y))for x, y in zip(enc_flag, key)])
print("Flag:\t", flag)
#flag: FLAG=Alpacaman
