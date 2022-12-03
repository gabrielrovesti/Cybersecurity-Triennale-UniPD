ciphertext = "yxyxxyy yxyxxxx yxyxxyx yxxyxxy yxyxyxx yxyyxyx yxxxxyy yxyxyxx yxxxyyx yyyyxy yyyyxyy yyxxyxy yyxyyyx yyxxxyy yyyxxyx yyyyxxy yyyxxxx yyyxyxx yyxyxxy yyxyyyy yyxyyyx yyxxxx yyxxxx yyxxxx yyxxxx yyxxxx yyxxxy yyyyyxy"
 #               s      p      r        i         t       z       c        t    f       
S = 'yxyxxyy'
P = "yxyxxxx"
R = "yxyxxyx"
I = "yxxyxxy"
T = "yxyxyxx"
Z = "yxyyxyx"

cleanup = ciphertext.replace("yxyxxyy","S")
cleanup = cleanup.replace("yxyxxxx","P")
cleanup = cleanup.replace("yxyxxyx","R")
cleanup = cleanup.replace("yxxyxxy","I")
cleanup = cleanup.replace("yxyxyxx","T")
cleanup = cleanup.replace("yxyyxyx","Z")
cleanup = cleanup.replace("yxxxxyy","C")
cleanup = cleanup.replace("yxxxyyx","F")
print(cleanup)
dect =  dict()
vector = ciphertext.split(" ")
m = 0
for i in vector :
    
    x = -1
    for j in vector:
        if (j==i) :
            x = x+1
    dect[m] = x
    m = m+1
print(dect)

############SOLUZIONE TROVATA#####################

decipher = ciphertext.replace("x","0")
decipher = decipher.replace("y","1")
print(decipher)
vec = decipher.split(" ")

strif = ""
for i in vec :
    tmp = int(i,2)
    strif = strif + chr(tmp)
    print(strif)
print(strif)


######FINE SOL###########




    
    
