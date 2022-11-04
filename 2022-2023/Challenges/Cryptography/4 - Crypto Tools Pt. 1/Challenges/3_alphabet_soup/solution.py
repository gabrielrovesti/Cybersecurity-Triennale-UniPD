#Here we are given a string like this:
#MKXU IDKMI DM BDASKMI NLU XCPJNDICFQ! K VDMGUC KW PDT GKG NLKB HP LFMG DC TBUG PDTC CUBDTCXUB. K'Q BTCU MDV PDT VFMN F WAFI BD LUCU KN KB WAFI GDKMINLKBHPLFMGKBQDCUWTMNLFMFMDMAKMUNDDA

#Let's initialize it
puzzle = "MKXU IDKMI DM BDASKMI NLU XCPJNDICFQ! K VDMGUC KW PDT GKG NLKB HP LFMG DC TBUG PDTC CUBDTCXUB. K'Q BTCU MDV PDT VFMN F WAFI BD LUCU KN KB WAFI GDKMINLKBHPLFMGKBQDCUWTMNLFMFMDMAKMUNDDA"

#We do not have any clue here on how to proceed, so let's try to find a pattern
#in this case, I wouldn't strip the spaces, cause it seems like some random phrase
#thrown in there and then cyphered in order to have something more chaotic.
#A good idea would be to try to find the single frequency of each letter in the string

#Let's create a dictionary to store the frequency of each letter
freq = {}
for f in puzzle:
    if f in freq:
        freq[f] += 1
    else:
        freq[f] = 1

#Now let's print the dictionary sorted
sorted_dict = sorted(freq.items(), key=lambda item: item[1], reverse=True) 
#sort the dictionary by value in descending order (most frequent first)

#This here gives us the following output:
#[(' ', 30), ('D', 17), ('M', 15), ('K', 14), ('U', 11), ('B', 10), 
# ('C', 10), ('F', 9), ('N', 8), ('I', 7), ('L', 7), ('G', 7), 
# ('T', 7), ('P', 6), ('A', 5), ('W', 4), ('X', 3), ('Q', 3), 
# ('V', 3), ('H', 2), ('S', 1), ('J', 1), ('!', 1), ('.', 1), ("'", 1)]

#Now we have to substitute each occurrence of a specific character
#to one we are sure it is the right one.

#Let's try to find a match for example
guess={'D':'E'} #we puth the curly braces in order to not substitute the character (case, we are not sure
#this might be the exact match)
decoded=''.join(c if c not in guess else guess[c] for c in puzzle) 
#this is a list comprehension to substitute the letter 'D' with 'E'

#The K is alone and we might guess is the letter 'I'
guess['K']='I' 
#here, we do use the square bracket cause we are pretty sure this is the right match
#making a substitution manually
decoded=''.join(c if c not in guess else guess[c] for c in puzzle)

#Then, we can see the 'Q' might correspond to the letter 'M'
guess['Q']='M'
decoded=''.join(c if c not in guess else guess[c] for c in puzzle)

#Then, we can see the 'W' might correspond to the letter 'F'
guess['W']='F'
decoded=''.join(c if c not in guess else guess[c] for c in puzzle)

#Then, we can see the 'F' might correspond to the letter 'A', given is also alone
guess['F']='A'
decoded=''.join(c if c not in guess else guess[c] for c in puzzle)

guess['N']='S'
guess['B']='T'
guess['T']='S'
decoded=''.join(c if c not in guess else guess[c] for c in puzzle)

## the semilast word contains four letters, and the third character
# is an 'a'. This word could be flag
guess['W'] = 'F'
guess['A'] = 'L'
guess['I'] = 'G'
decoded = ''.join(c if c not in guess else guess[c] for c in puzzle)

#not a lot of info...
#however, there is a word with GiG ... G must be a 'D'
guess['G'] = 'D'
decoded = ''.join(c if c not in guess else guess[c] for c in puzzle)

#then there is a sentence with "if PDT did"
# PDT could be "you", a likely word with letters not used yet
guess['P'] = 'Y'
guess['D'] = 'O'
guess['T'] = 'U'
decoded = ''.join(c if c not in guess else guess[c] for c in puzzle)

#slightly better. The second word is goiMg
# M->n
guess['M'] = 'N'
decoded = ''.join(c if c not in guess else guess[c] for c in puzzle)

#back on the second sentence
# if you did NLiB Hy ... seems "if you did this by"
guess['N'] = 'T'
guess['L'] = 'H'
guess['B'] = 'S'
guess['H'] = 'B'
decoded = ''.join(c if c not in guess else guess[c] for c in puzzle)

#the fourth word must be "solving"
guess['S'] = 'V'
decoded = ''.join(c if c not in guess else guess[c] for c in puzzle)

#fifth word is the
guess['U'] = 'E'
decoded = ''.join(c if c not in guess else guess[c] for c in puzzle)

#then, "I wonder if you ..."
guess['V'] = 'W'
guess['C'] = 'R'
decoded = ''.join(c if c not in guess else guess[c] for c in puzzle)

#ready to conclude. we can see the flag .. but lets finish the job
#niXe -> nice
guess['X'] = 'C'
decoded = ''.join(c if c not in guess else guess[c] for c in puzzle)

#the last word of the fist sentence is cryptogram
guess['J'] = 'P'
decoded = ''.join(c if c not in guess else guess[c] for c in puzzle)
print(decoded)
