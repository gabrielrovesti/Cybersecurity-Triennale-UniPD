s=''
with open('challenge.txt', 'r') as file:
    challenge = file.read()
    for i in challenge:
        #Checking if the character is a letter
       if i.isupper(): #there are some uppercase letters, so we take them out
        s=s+i
s=s.replace('ZERO', '0') #replacing ZERO and ONE with 0 and 1
s=s.replace('ONE', '1')
#print(s) #here we do have a string printed like '010000100100...'

#the idea is having the string 's' and taking each 8 bytes
#as a single one and converting them into letters
#so we have to split the string into 8 bytes chunks
#and then convert them into letters
#and finally print the flag
for i in range(0, len(s), 8): 
    #the idea is iterating starting from '0', going up until the length of the string
    #and taking each 8 bytes as a single one
    #chr() function is used to get a string representing of a character which points to a Unicode code integer.
    #then we go ahead up until the last ''
    print(chr(int(s[i:i+8], 2)), end='') #2 is for binary

#BITSCTF{h1d3_1n_pl41n_5173}







