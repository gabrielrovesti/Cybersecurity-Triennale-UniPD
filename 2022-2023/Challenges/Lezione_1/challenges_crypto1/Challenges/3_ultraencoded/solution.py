#Fady didn't understand well the difference between encryption and encoding,
#so instead of encrypting some secret message to pass to his friend, he
#encoded it!
#The flag should be in the format: ALEXCTF 

import base64

with open("zero_one", 'r') as file:
    file = file.read()

file = file.replace('ZERO', '0')
file = file.replace('ONE', '1')
file = file.replace(' ', '')
file = file.strip()

flag = ''
#here we do have a string printed like '010000100100...'
#so we need what we did in the previous challenge
for i in range(0, len(file), 8):
    flag=''.join([flag, chr(int(file[i:i+8], 2))]) #2 is for binary and remember to concatenate the flag with the new character

decoded_flag=base64.b64decode(flag)
print(decoded_flag)
#here as a string we have the following:
#b'.- .-.. . -..- -.-. - ..-. - .... .---- ..... --- .---- ... --- ..... ..- .--. ...-- .-. --- ..... . -.-. .-. ...-- - --- - -..- -'
#we need to decode it using morse code, cause there are the signs
#in order to do that, we need to define a map of morse code
#and then we need to split the string into words
#translating and finding the flag
morse_code = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9', '-----': '0', '': ' '
}
#now we need to find the couple of characters and convert them into bytes
#and then decode them into ascii
flag = ''
for i in decoded_flag.decode('ascii').split(): #split the string into words
    flag = ''.join([flag, morse_code[i]]) #join the characters to form the flag
print(flag) #ALEXCTF{M0RSE_C0D3_1S_3ASY}