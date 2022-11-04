#open the text file
with open('challenge.txt', 'r') as file:
    challenge = file.read()

#extract uppercase letters
insight=''.join([c for c in challenge if c.isupper()])
print(insight)

#replace the zeros and ones in the numerical representation
insight = insight.replace('ZERO', '0')
insight = insight.replace('ONE', '1')
print(insight)

#let see the length
print(len(insight))

#since it is a multiple of 8, we can think that this is a series of
#ascii characters
result=''.join(chr(int(insight[i*8:i*8+8],2)) for i in range(len(insight)//8))
print(result)
