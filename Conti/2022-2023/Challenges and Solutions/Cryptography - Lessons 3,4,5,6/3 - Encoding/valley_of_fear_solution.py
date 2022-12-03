#The hard drive may be corrupted, but you were able to recover a small chunk of text (see "book.txt").
#Scribbled on the back of the hard drive is a set of mysterious numbers. Can you discover the meaning behind these numbers? (1, 9, 4) (4, 2, 8) (4, 8, 3) (7, 1, 5) (8, 10, 1)

keys = [(1, 9, 4), (4, 2, 8), (4, 8, 3), (7, 1, 5), (8, 10, 1)]

with open("book.txt") as book:
    text = book.read() #read the content
    paragraphs = [p.split("\n") for p in text.split("\n\n")] #split the content into paragraphs and breaking the lines
    #saving the words from paragraph into a list
    #using the lambda function to define inline
    #a function to search inside the paragraphs and splitting the spaces in between
    words = list(map(lambda p: list(map(lambda s: s.split(" "), p)), paragraphs)) 
    #split the paragraphs into sentences
    flag = " ".join(words[key[0] - 1][key[1] - 1][key[2] - 1] for key in keys) 
#get the words from the keys array [i-1] to avoid going out of bounds
print(flag)
