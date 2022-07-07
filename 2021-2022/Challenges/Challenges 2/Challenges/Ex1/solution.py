input = 'abc'
key = 2

#solution 1
output1 = '' #copy
for i in range(len(input)):
    output1 += chr(ord(input[i]) + key)

print(output1)

#solution 2
output2 = ''
for c in input:
    output2 += chr(ord(c) + key)

print(output2)

#solution 3
output3 = ''.join([chr(ord(c) + key) for c in input])
print(output3)

"""
Triple quotation marks (virgolette) represent a multiline comment

Definition of methods used above:
- chr() method returns a character (a string) from an integer (represents unicode code point of the character).
- ord() function returns an integer representing the Unicode character.
- join() method takes all items in an iterable and joins them into one string.

Also:
1) : represents the indented block
2) "in" is like sayin "to" in other types of for, while "range" represents
    the maximum length reached by the for cycle
3) a variable doesn't need to be inizialized, like shown in the for cycle above

"""