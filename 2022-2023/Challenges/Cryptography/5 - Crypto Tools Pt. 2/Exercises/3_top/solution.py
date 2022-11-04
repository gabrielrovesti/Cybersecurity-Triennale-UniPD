#Perfectly secure. That's for sure! Or can break it and reveal my secret?
#We are given a encryption script and the a file which is encrypted with it

import time
import random

#useful to use "rb" to read in binary and open correctly the file
#otherwise, it won't work (infact, as a no extension file, is considered binary)
with open('top_secret', 'rb') as f:
    data = f.read()

#we need to reverse the encryption
#we know that the key is the same length as the message

print(len(data)) #75

#let's try to think about the algorithm
#there's a message which is encoded in ascii, 
#a key selected randomly using the current time as the seed
#and a xor function between the message and the key
#and 0x88, multiplied X times with the length of the current time

#we can see that the time length is added many times
#so we can xor it subtracting from the length of the data the length of the time

cur_time=str(time.time()).encode('ASCII') #we take the current time
encoded_time = data[-len(cur_time):] #we take the last bytes of the data

#we xor the encoded time with the current time
plain_time=''.join([chr(m ^ k) for (m, k) in zip(encoded_time, [0x88] * len(cur_time))])
print(plain_time) #513719133.8728752

#the time is used as the seed for the random function
#so it has to be used again to set the seed (otherwise, it will be different)
#also, we need to ascii encode it

random.seed(str(plain_time).encode('ASCII'))

#we can now take the key and the message, as we know of the same length
#and this also drives to the xor idea again
#as we saw, the key is created with a random range of 256
#and we do need to subtract it away from the data
key = [random.randrange(256) for _ in data[:-len(cur_time)]]

#we can now xor to get the text back, removing the time and xoring the key
text=''.join([chr(m ^ k) for (m, k) in zip(data[:-len(cur_time)], key)])
print(text.encode('ASCII'))

