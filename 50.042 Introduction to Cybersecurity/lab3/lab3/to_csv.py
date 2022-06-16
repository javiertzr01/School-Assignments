import csv
import hashlib

def MD5Hash(plaintext):
    result = hashlib.md5(plaintext.encode())
    return result.hexdigest()

def checkList(filein):
    ls = []
    with open(filein, "r") as fin:
        line = fin.readline()
        while line:
            line = line.replace("\n", "").strip()
            ls.append(line)
            line = fin.readline()
    return ls

def filterInformation(filein, ls):
    result = {}
    with open(filein, "r") as fin:
        line = fin.readline()
        while line:
            line = line.replace("\n", " ").strip()
            if line not in result and line != '':
                hashed = MD5Hash(line)
                if hashed in ls:
                    result[line] = hashed
                else:
                    print(hashed)
            line = fin.readline()
    return result

def writeToCsv(fileout, dictionary):
    with open(fileout, "w") as csvfile:
        for key in dictionary.keys():
            csvfile.write("%s, %s\n" % (dictionary[key], key))

if __name__ == "__main__":
    ls = checkList("hashes.txt")
    dictionary = filterInformation("challenge_plain.txt", ls)
    writeToCsv("ex5.csv", dictionary)