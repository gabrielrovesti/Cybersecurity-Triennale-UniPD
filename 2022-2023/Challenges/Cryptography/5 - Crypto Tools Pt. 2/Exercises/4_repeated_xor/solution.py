#we do have a txt file and we're gonna read it

with open('encrypted.txt', 'r') as f:
    data = f.read()
    data=data.replace(' ', '').replace('\n', '') #removing the \n from the end of the line and converting to ascii

#we do know the file is hex encoded, so we decode its bytes into
#decimal format and then we convert it to ascii
def hex_to_dec(text):
    result=[]
    #we take each pair of bytes and convert it to decimal (2), looping into hex (16)
    for i in range(0, len(text), 2):
        #taking each pair of bytes in the text and converting it to decimal
        current="".join(text[i:i+2])
        #appending the result considering each pair corresponds to a byte in hex
        result.append(int(current, 16))
    return result

decoded_data=hex_to_dec(data) #we decode the data (printed seems like a map of integers)

#We have a repeated xor problem here, so we have to make a frequency
#analysis in order to understand which characters are the most frequent ones
#and then we can guess the key
#First, we have to guess the key length; infact, if the key is shorter than the message,
#the key will repeat itself many times in order to cover the whole message.
#So, after converting to integers, we duplicate the key and xor
#the message with the duplicated key.

#Step 1 - Key length identification (we know it's probably 10 bytes long)
#Here, we do need to make an educate guess using the frequency analysis and a shift function,
#just to play out with some different lengths

def shift(text, n):
    return text[n:] + text[:n] #we shift the text by n bytes and sum them together

def count_same(a, b): #we count the same bytes in the text and simply return it
    count=0
    for x, y in zip(a,b):
        if x == y:
            count+=1
    return count

def guess_key_length(text, key_length):
    #what we are doing here is making a range based on the key length
    #then counting the same bytes in the text and making a shift of "n" bytes
    #in order to try all of the possible combinations

    #we return the key length with the highest count of same bytes
    #the higher the count, the more likely the key length is correct
    return max(range(1, key_length), key=lambda n: count_same(text, shift(text, n)))

print(guess_key_length(decoded_data, 10)) #we print the key length, which is 8

#Up until here, we completed step (1)

#Step 2 - Cryptoanalysis
#We do know the key length, so we can guess the XOR is made with 8 bytes block in mind
#Remember that the key is repeated every 8 bytes within the text,
#so the idea is to take the most frequent characters every 8 bytes based on the key length

from collections import Counter #we import the counter in order to count the most frequent characters

#Given it should be English text, the  most frequent characters would be
#e, t, a, o, i, n, s, h (in this order), thinking also '' (the space) should be the most frequent one

#Because XOR is its own inverse, we can find the key by XORing cipher text and known plain text 
#(given a character, in whatever column it appears, given the fixed key length, the XOR always gives the same result)
#Thus we can find the key if we know the most common character in english and the most common character in the nth column.

def most_frequent_chars(text, key_length):
    #we split the text into blocks of 8 bytes
    #then we count the most frequent characters in each block
    #and we return the result
    return [Counter(text[i::key_length]).most_common(1)[0][0] for i in range(key_length)] 
    #we return the most frequent character (hence the (1)) in each block (given the key length)

key_secure=most_frequent_chars(decoded_data, 8)
print(key_secure) #we print the map of the most frequent characters in the text, splitted by 8

#now, we need to find the key, which is the XOR of the most frequent characters in the text and the plain text itself
real_key = [k ^ ord(' ') for k in key_secure]

#decode the secret and print the flag
for i in range(len(decoded_data)):
    decoded_data[i] ^= real_key[i % len(real_key)] #we xor the data with the key given the 8 bytes split

print(bytes(decoded_data).decode('ascii')) #we print the final result (given it is the flag and all of the other text) as ascii
