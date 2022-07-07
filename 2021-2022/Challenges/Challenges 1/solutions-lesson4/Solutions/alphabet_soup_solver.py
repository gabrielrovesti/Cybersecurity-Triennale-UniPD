#we only have an encrypted message
puzzle = "MKXU IDKMI DM BDASKMI NLU XCPJNDICFQ! K VDMGUC KW PDT GKG NLKB HP LFMG DC TBUG PDTC CUBDTCXUB. K'Q BTCU MDV PDT VFMN F WAFI BD LUCU KN KB WAFI GDKMINLKBHPLFMGKBQDCUWTMNLFMFMDMAKMUNDDA"

#since I do not have any clue, I try to use the cryptanalysis strategy
#in the ciphers, in general, each letter is associated to a given alphabet
# we can try to find possible associations.

#the first step is to see the frequency of each characters
chr2freq = {}
for c in puzzle:
    if c not in chr2freq:
        chr2freq[c] = 1
    else:
        chr2freq[c] += 1

sorted_x = sorted(chr2freq.items(), key=lambda kv: kv[1], reverse = True)
print(sorted_x)

# hypothesis 1: the text is english written
# we can find online what are the most used english characters
# e.g., http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html

# we see that the 'K' is "alone", and we can think to
# K = I
voc = {'K': 'i'}
dec = ''.join(c if c not in voc else voc[c] for c in puzzle)
print(voc, '\n' ,dec)

#then there is an 'i'Q', which is likely an M
voc['Q'] = 'm'
dec = ''.join(c if c not in voc else voc[c] for c in puzzle)
print(voc, '\n' ,dec)

#F -> 'a'
voc['F'] = 'a'
dec = ''.join(c if c not in voc else voc[c] for c in puzzle)
print(voc, '\n' ,dec)

## the semilast word contains four letters, and the third character
# is an 'a'. This word could be flag
voc['W'] = 'f'
voc['A'] = 'l'
voc['I'] = 'g'
dec = ''.join(c if c not in voc else voc[c] for c in puzzle)
print(voc, '\n' ,dec)

#not a lot of info...
#however, there is a word with GiG ... G must be a 'D'
voc['G'] = 'd'
dec = ''.join(c if c not in voc else voc[c] for c in puzzle)
print(voc, '\n' ,dec)

#then there is a sentence with "if PDT did"
# PDT could be "you", a likely word with letters not used yet
voc['P'] = 'y'
voc['D'] = 'o'
voc['T'] = 'u'
dec = ''.join(c if c not in voc else voc[c] for c in puzzle)
print(voc, '\n' ,dec)

#slightly better. The second word is goiMg
# M->n
voc['M'] = 'n'
dec = ''.join(c if c not in voc else voc[c] for c in puzzle)
print(voc, '\n' ,dec)

#back on the second sentence
# if you did NLiB Hy ... seems "if you did this by"
voc['N'] = 't'
voc['L'] = 'h'
voc['B'] = 's'
voc['H'] = 'b'
dec = ''.join(c if c not in voc else voc[c] for c in puzzle)
print(voc, '\n' ,dec)

#the fourth word must be "solving"
voc['S'] = 'v'
dec = ''.join(c if c not in voc else voc[c] for c in puzzle)
print(voc, '\n' ,dec)

#fifth word is the
voc['U'] = 'e'
dec = ''.join(c if c not in voc else voc[c] for c in puzzle)
print(voc, '\n' ,dec)

#then, "I wonder if you ..."
voc['V'] = 'w'
voc['C'] = 'r'
dec = ''.join(c if c not in voc else voc[c] for c in puzzle)
print(voc, '\n' ,dec)

#ready to conclude. we can see the flag .. but lets finish the job
#niXe -> nice
voc['X'] = 'c'
dec = ''.join(c if c not in voc else voc[c] for c in puzzle)
print(voc, '\n' ,dec)

#the last word of the fist sentence is cryptogram
voc['J'] = 'p'
dec = ''.join(c if c not in voc else voc[c] for c in puzzle)
print(voc, '\n' ,dec)


## we did it
#  nice going on solving the cryptogram!
#i wonder if you did this by hand or used your resources.
#i'm sure now you want a flag so here it is
#flag doingthisbyhandismorefunthananonlinetool
