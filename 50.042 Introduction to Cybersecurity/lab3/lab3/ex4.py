import hashlib
import time
import random
import string

def RetrievePlaintext(filein):
    with open(filein, "r") as fin:
        ls = []
        line = fin.readline()
        while line:
            if line[0:10] == "Plaintext:":
                ls.append(line[11:16])
            line = fin.readline()
    return ls

def MD5Hash(plaintext):
    result = hashlib.md5(plaintext.encode())
    return result.hexdigest()

def getRandInt():
    randInt = random.randint(0,25)
    return randInt

def getLowercaseAlpha():
    return string.printable[10:36]

def saltedHash(ls):
    lowerCaseAlpha = getLowercaseAlpha()
    result = {}
    pw_ls = []
    for plaintext in ls:
        salt = lowerCaseAlpha[getRandInt()]
        new_plaintext = plaintext + salt
        hashed = MD5Hash(new_plaintext)
        result[hashed] = salt
        pw_ls.append(new_plaintext)
    return result, pw_ls

def writeHashedSaltToFile(fileout, saltedHashDict):
    with open(fileout, "w") as fout:
        for key, value in saltedHashDict.items():
            fout.write("Hashed: " + key + "\nSalt: " + value + "\n\n")
            
def writeHashedToFile(fileout, saltedHashDict):
    with open(fileout, "w") as fout:
        for key,value in saltedHashDict.items():
            fout.write(key + "\n")

def writePasswordToFile(fileout, pw_ls):
    with open(fileout, "w") as fout:
        for pw in pw_ls:
            fout.write(pw + "\n")

if __name__ == "__main__":
    plaintexts = RetrievePlaintext("ex2_hash.txt")
    saltedHashDict, pw_ls = saltedHash(plaintexts)
    print(saltedHashDict)
    print(pw_ls)
    writeHashedSaltToFile("salted6.txt", saltedHashDict)
    writeHashedToFile("hash6.txt", saltedHashDict)
    writePasswordToFile("plain6.txt", pw_ls)