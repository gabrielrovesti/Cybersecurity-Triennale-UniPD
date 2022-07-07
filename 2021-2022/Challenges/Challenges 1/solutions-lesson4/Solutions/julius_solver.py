#in the first line of the description contains an hint
# Julius,Q2Flc2FyCg==
# since it ends with ==, the first hypothesis is
#that this is a base64 encoding
#let's decodi it!
import base64
enc_b64 = 'Q2Flc2FyCg=='

#we define a function. It might be helpful in future
def base64tostring(text):
    return base64.b64decode(text).decode('utf-8', errors="ignore")

print(f"Decoding=\t{base64tostring(enc_b64)}")

#the hints says "caesar", and we know a famous cipher
#with this name. We can apply e reverse to the
# ciphered text given in description

puzzle = 'fYZ7ipGIjFtsXpNLbHdPbXdaam1PS1c5lQ=='
print("The length of the puzzle is:\t", len(puzzle))

# the length is a multiple of 4, and the alphabet seems too regular (no punctuation).
#we can think that this is a base64 encoded string
puzzle_dec = base64tostring(puzzle)
print("Decoded puzzle:", puzzle_dec)

# now we have a lot of no sense characters. We can try to apply
# the ceasar cipher
def ceasar_cracker(text, from_ = -30, to_=+30):
    for i in range(from_, to_): #possible keys [-30, 30]
        #decode
        curr_step = ''.join([chr(ord(c) + i) for c in text])

        #print
        print(f"Step={i}\t{curr_step}")

ceasar_cracker(puzzle_dec)
## we look for some readable flags. We find one at step -24
#FLAG: ecCTF3T_7U_BRU73?!
