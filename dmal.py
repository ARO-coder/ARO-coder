#!/usr/bin/python3
import os
from cryptography.fernet import Fernet
files = []
for file in os.listdir():
    if file == "mal.py" or file == "thekey.key" or file == "dmal.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)
with open("thekey.key","rb") as key:
    secretkey = key.read()

for file in files:
    with open(file,"rb") as thefile:
        contents =thefile.read()
    contents_dnc =Fernet(secretkey).decrypt(contents)
    with open(file,"wb") as thefile:
        thefile.write(contents_dnc)
