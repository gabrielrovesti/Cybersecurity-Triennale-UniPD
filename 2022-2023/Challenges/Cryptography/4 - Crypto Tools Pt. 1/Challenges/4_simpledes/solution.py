#Larry is working on an encryption algorithm based on DES.
#
#He hasn't worked out all the kinks yet, but he thinks it works.
#
#Your job is to confirm that you can decrypt a message, given the algorithm and parameters used.
#
#His system works as follows:
#   
#	1. Choose a plaintext that is divisible into 12bit 'blocks'
#	2. Choose a key at least 8bits in length
#	3. For each block from i=0 while i<N perform the following operations
#	4. Repeat the following operations on block i, from r=0 while r<R
#	5. Divide the block into 2 6bit sections Lr,Rr
#	6. Using Rr, "expand" the value from 6bits to 8bits.
#		Do this by remapping the values using their index, e.g.
#		1 2 3 4 5 6 -> 1 2 4 3 4 3 5 6
#	7. XOR the result of this with 8bits of the Key beginning with Key[iR+r] and wrapping back to the beginning if necessary.
#	8. Divide the result into 2 4bit sections S1, S2
#	9. Calculate the 2 3bit values using the two "S boxes" below, using S1 and S2 as input respectively.
#
#	S1	0	1	2	3	4	5	6	7
#	0	101	010	001	110	011	100	111	000
#	1	001	100	110	010	000	111	101	011
#	
#	S2	0	1	2	3	4	5	6	7
#	0	100	000	110	101	111	001	011	010
#	1	101	011	000	111	110	010	001	100
#	
#	10. Concatenate the results of the S-boxes into 1 6bit value
#	11. XOR the result with Lr
#	12. Use Rr as Lr and your altered Rr (result of previous step) as Rr for any further computation on block i
#	13. increment r
#	
#He has encrypted a message using Key="Mu", and R=2. See if you can decipher it into plaintext.
#
#Submit your result to Larry in the format Gigem{plaintext}.
#
#Binary of ciphertext: 01100101 00100010 10001100 01011000 00010001 10000101
#Ascii of the text: Bin: ASCII: "MiN0n!"

#Rule 9 - Calculate the 2 3bit values using the two "S boxes" below, using S1 and S2 as input respectively.
def S1(binary):
    #index row and column in s1 avoiding going out of bounds
    row = int(binary[0])
    col = int(binary[1:], 2)

    s1 = [['101','010','001','110','011','100','111','000'],
        ['001',	'100','110','010','000','111','101','011']]

    return s1[row][col]

def S2(binary):
    #index row and column in s1
    row = int(binary[0])
    col = int(binary[1:], 2)

    s2 = [['100','000','110','101','111','001','011','010'],
        ['101',	'011','000','111','110','010','001','100']]

    return s2[row][col]

def text_to_binary(text):
    #return ''.join(f"{ord(c):08b}" for c in text) 
    return ''.join(format(ord(x), 'b') for x in text)

#in the encryption function we do consider the key as a binary string
def encrypt(text, key, R):
    text_encoded=''
    #convert the text and the key to binary
    text_binary = text_to_binary(text)
    key_binary = text_to_binary(key)
    #Check if plaintext that is divisible into 12bit 'blocks'
    if(len(text_binary) % 12 != 0):
        raise Exception("Plaintext is not divisible into 12bit blocks")
    #Check if key at least 8bits in length
    if(len(key_binary) < 8):
        raise Exception("Key is not at least 8bits in length")

    for i in range(0, len(text_binary), 12):
        #define the block
        block=text_binary[i:i+12]

        for r in range(R):
            #divide the block into two 6bit sections
            Lr=block[:6]
            Rr=block[6:]
            #expand the value from 6bits to 8bits
            Rr_expanded = Rr[0] + Rr[1] + Rr[3] + Rr[2] + Rr[3] + Rr[2] + Rr[4] + Rr[5]
            #XOR the result of this with 8bits of the Key beginning with Key[iR+r] and wrapping back to the beginning if necessary
            #xor_result = str(int(Rr_expanded, 2) ^ int(key_binary[(i*R+r)%len(key_binary):((i*R+r)%len(key_binary))+8], 2)) #xor the expanded Rr with the key
            xor_result = str(int(Rr_expanded, 2) ^ int(key_binary[(i*R+r):((i*R+r)+8)], 2)) #xor the expanded Rr with the key (converted in string to iterate on it)
            #Divide the result into 2 4bit sections S1, S2
            Rr_xor_1 = xor_result[:4] 
            Rr_xor_2 = xor_result[4:]
            #Calculate the 2 3bit values using the two "S boxes" below, using S1 and S2 as input respectively
            Rr_xor_1_split=S1(Rr_xor_1)
            Rr_xor_2_split=S2(Rr_xor_2)
            #Concatenate the results of the S-boxes into 1 6bit value
            Rr_s_split = Rr_xor_1_split + Rr_xor_2_split
            #check if the length of the xor result is 6
            if(len(Rr_s_split) != 6):
                raise Exception("The length of the xor result is not 6")
            #XOR the result with Lr
            Rr_alt = int(Lr, 2) ^ int(Rr_s_split, 2)
            #Use Rr as Lr and your altered Rr (result of previous step) as Rr for any further computation on block i
            Lr = Rr
            Rr = str(bin(Rr_alt))[2:].zfill(6) #convert the result to binary and fill with 0s to have 6bits
        #concatenate the results
        text_encoded+=Lr+Rr
    return text_encoded

#now, we're going to write the decryption function
#the core of it is taking the reasoning of the previous function
#and reversing the loop applying the same logic and checks

def decrypt(text, key, R):
    text_decoded=''
    #convert the key in binary, cause the text is already in the right formatting
    key_binary = text_to_binary(key)
    #Check if plaintext that is divisible into 12bit 'blocks'
    if(len(text_binary) % 12 != 0):
        raise Exception("Plaintext is not divisible into 12bit blocks")
    #Check if key at least 8bits in length
    if(len(key_binary) < 8):
        raise Exception("Key is not at least 8bits in length")
    for i in range(0, len(text), 12):
        #define the block
        block=text[i:i+12]
        #now we do need to reverse the loop
        for r in range(R-1, -1, -1):
            #divide the block into two 6bit sections
            Rr=block[:6]
            Rr_alt=block[6:]
            #expand the value from 6bits to 8bits
            Rr_alt_expanded = Rr_alt[0] + Rr_alt[1] + Rr_alt[3] + Rr_alt[2] + Rr_alt[3] + Rr_alt[2] + Rr_alt[4] + Rr_alt[5]
            #XOR the result of this with 8bits of the Key beginning with Key[iR+r] and wrapping back to the beginning if necessary
            xor_result = str(int(Rr_expanded, 2) ^ int(key_binary[(i*R+r)%len(key_binary):((i*R+r)%len(key_binary))+8], 2)) #xor the expanded Rr with the key
            #Divide the result into 2 4bit sections S1, S2
            Rr_xor_1 = xor_result[:4]
            Rr_xor_2 = xor_result[4:]
            #Calculate the 2 3bit values using the two "S boxes" below, using S1 and S2 as input respectively
            Rr_xor_1_split=S1(Rr_xor_1)
            Rr_xor_2_split=S2(Rr_xor_2)
            #Concatenate the results of the S-boxes into 1 6bit value
            Rr_s_split = Rr_xor_1_split + Rr_xor_2_split
            #check if the length of the xor result is 6
            if(len(Rr_s_split) != 6):
                raise Exception("The length of the xor result is not 6")
            #XOR the result with Lr
            Lr = xor(int(Rr_alt, 2), int(Rr_s_split, 2))
            #Use Rr as Lr and your altered Rr (result of previous step) as Rr for any further computation on block i
            block = Lr + Rr
        #concatenate the results
        text_decoded+=block
    return text_decoded

#Lastly, we do write the test calls of both function
#and print the results
puzzle = "011001010010001010001100010110000001000110000101"
key_ex = 'Mu'
R_ex = 2
decrypt(encrypt(puzzle, key_ex, R_ex), key_ex, R_ex)
