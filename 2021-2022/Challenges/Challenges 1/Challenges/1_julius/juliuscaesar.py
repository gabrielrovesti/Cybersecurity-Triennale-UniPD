import base64
import binascii

message=''
base64_message = "fYZ7ipGIjFtsXpNLbHdPbXdaam1PS1c5lQ=="
#caesar_message='Q2Flc2FyCg=='

base64_message = '}{[l^KlwOmwZjmOKW9'
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')

print(message)

shift = 3

for c in message:

    # check if character is an uppercase letter
    if c.isupper():

        # find the position in 0-25
        c_unicode = ord(c)

        c_index = ord(c) - ord("A")

        # perform the negative shift
        new_index = (c_index - shift) % 26

        # convert to new character
        new_unicode = new_index + ord("A")

        new_character = chr(new_unicode)

        # append to plain string
        plain_text = plain_text + new_character

    else:

        # since character is not uppercase, leave it as it is
        plain_text += c

        print(plain_text)
"""
base64_bytes = base64_message.encode("ascii")
message_bytes = base64.b64decode(base64_bytes)
#message = message_bytes.decode("ascii")
message = (''.join(message)).encode('utf-8')
"""

#--shuffle for bruteforce (beta)
#temp = list(message.values())
#random.shuffle(temp)