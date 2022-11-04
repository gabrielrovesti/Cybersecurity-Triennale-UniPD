#Crack the cipher: vhixoieemksktorywzvhxzijqni
#
#Your clue is:
#
#"caesar is everything. But he took it to the next level."
#

#The hint "to the next level" says everything
#cause it actually refers to the Vigeneré cipher
#which is a Caesar cipher with a key word

text='vhixoieemksktorywzvhxzijqni'

#The key word is "caesar"
#and we define an algorithm in order to use the Vigeneré cipher
def vigenere(text, key):
    key = key * (len(text) // len(key) + 1) #repeat the key word
    return ''.join([chr((ord(text[i]) - ord(key[i])) % 26 + ord('a')) for i in range(len(text))])
    #the algorithm is the same as the Caesar cipher
    #but we use the key word instead of a single letter
    #so we make a shift subtracting from the key word from the text
    #modulo 26 to keep the letters in the alphabet
    #and adding the ascii code of 'a' to get the right letter
    #we do this for every letter in the text

print (vigenere(text, 'caesar'))
#the result is "theforceisstrongwiththisone"