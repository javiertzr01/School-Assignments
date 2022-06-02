import hashlib
import string
from timeit import default_timer as timer

def getPossibleChars():
    return string.printable[0:36]

def MD5Hash(plaintext):
    result = hashlib.md5(plaintext.encode())
    return result.hexdigest()

def getHashes(filein):
    result = {}
    with open(filein, "r") as fin:
        line = fin.readline()
        while line:
            line = line[0:32]
            result[line] = "NIL"
            line = fin.readline()
    return result

def checkHash(dictionary, value):
    if value in dictionary:
        if dictionary[value] != "NIL":
            raise Exception("Collision Detected")
        elif dictionary[value] == "NIL":
            return True
    else:
        return False
    
def decodeDict(dictionary, fileout):
    with open(fileout, "w") as fout:
        for key, value in dictionary.items():
            fout.write("Plaintext: " + value + "\nHash: " + key + "\n\n")
        
    
def permutateFive(input, filein):
    textList = []
    length = len(input)
    hashes = getHashes(filein)
    counter = 0
    for one in range(length):
        if counter == 15:
            break
        print("processing" + str(one))
        if len(textList) == 0:
            textList.append(input[one])
        else:
            textList[0] = input[one]
        for two in range(length):
            if counter == 15:
                break
            if len(textList) == 1:
                textList.append(input[two])
            else:
                textList[1] = input[two]
            for three in range(length):
                if counter == 15:
                    break
                if len(textList) == 2:
                    textList.append(input[three])
                else:
                    textList[2] = input[three]
                for four in range(length):
                    if counter == 15:
                        break
                    if len(textList) == 3:
                        textList.append(input[four])
                    else:
                        textList[3] = input[four]
                    for five in range(length):
                        if counter == 15:
                            break
                        if len(textList) == 4:
                            textList.append(input[five])
                        else:
                            textList[4] = input[five]
                        text = "".join(map(str,textList))
                        textHash = MD5Hash(text)
                        if checkHash(hashes, textHash) == True:
                            hashes[textHash] = text
                            counter += 1
        textList = []
    return hashes
#create a dictionary to hold the hash as key and the string as value


if __name__ == "__main__":
    start = timer()
    answerDict = permutateFive(getPossibleChars(), "hash5.txt")
    end = timer()
    timeTaken = end - start
    print(timeTaken)
    print(answerDict)
    decodeDict(answerDict,"ex2_hash.txt")