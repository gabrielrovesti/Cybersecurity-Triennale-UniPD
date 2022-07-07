# The description says:
# "ceasar is everything"

#maybe it is a ceasar cipher, and we need to
#crack it as in the previous exercise

puzzle = 'vhixoieemksktorywzvhxzijqni'

def ceasar_cracker(text, from_ = -30, to_=+30):
    for i in range(from_, to_): #possible keys [-30, 30]
        #decode
        curr_step = ''.join([chr(ord(c) + i) for c in text])

        #print
        print(f"Step={i}\t{curr_step}")

ceasar_cracker(puzzle)
# I don't see any proper flag. We need to find another way
# The description says that it is the "next level" of ceasar.
# After some investigation, we can find that the evolution
# of a ceasar cipher is the vigenere cipher.
#However, the vigenere requires also a key.
# Google can help us! There are some online bruteforce services
#for these kind of ciphers.
#https://www.guballa.de/vigenere-solver
#
# the flag is reached: theforceisstrongwiththisone
#
# the key is "ceasar" ... as the hint suggested
