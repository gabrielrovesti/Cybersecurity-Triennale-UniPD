import random
import string

#define the vocabulary
vocabulary = list(string.ascii_letters) + list(string.digits)
#this is like sayin, combine letters with numbers and make them into vocabulary
#as noticed at this point, Python doesn't use semicolons (;)

#if you uncomment the following line, you allow the reproducibility
#random.seed(123)

#set final variable
password = ''

#define number of iterations
password_size = 10

for i in range(password_size):
    #shuffle the vocabulary
    random.shuffle(vocabulary)

    #update the password. We take the first element of the vector
    password += vocabulary[0]

print(f"Password generated=\t{password}")
# \t is like an escape character, in particular defines the end of the string
# (#) defines a single line comment
