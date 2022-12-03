ciphertext = "yxyxxyy yxyxxxx yxyxxyx yxxyxxy yxyxyxx yxyyxyx yxxxxyy yxyxyxx yxxxyyx yyyyxy yyyyxyy yyxxyxy yyxyyyx yyxxxyy yyyxxyx yyyyxxy yyyxxxx yyyxyxx yyxyxxy yyxyyyy yyxyyyx yyxxxx yyxxxx yyxxxx yyxxxx yyxxxx yyxxxy yyyyyxy"

#We have no clue as of now, so we will try to make a frequency analysis

freq={}
for i in ciphertext:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

sorted_list=sorted(freq.items(), key=lambda x: x[1], reverse=True)
print(sorted_list)

#This has no purpose; infact, we can see that the frequency of x and y is almost equal
#Instead, we can think it as a ULTRAENCODED challenge,
#the one with only ZEROONE input. We're gonna try
#to use the replace() function in order to substitute the characters
#with 0 and 1

ciphertext=ciphertext.replace("x","0")
ciphertext=ciphertext.replace("y","1")
ciphertext=ciphertext.split(" ") #splitting the ciphertext into a list of words
print(ciphertext) #printing the ciphertext as list

#Print here of the result
#1010011 1010000 1010010 1001001 1010100 1011010 1000011 
#1010100 1000110 111101 1111011 1100101 1101110 1100011 
#1110010 1111001 1110000 1110100 1101001 1101111 1101110 
#110000 110000 110000 110000 110000 110001 1111101

#Here we can notice that some strings are 7 chars long, some are 6 chars long
#We can think of them as binary positions, so we can try to convert them
#to ASCII. Thing is, all of the characters are binary.
#We can simply convert them all to ASCII and get to the flag

for i in ciphertext:
    print(chr(int(i,2)),end="")
