#!/usr/bin/env python3
# SUTD 50.042 FCS Lab 1
# Simple file read in/out


# Import libraries
import sys
import argparse
import string

# In Python, strings are represented as arrays of Unicode code points. To reveal their ordinal values, call ord() on each of the characters
# https://realpython.com/python-bitwise-operators/ 

def encrypt(character, key):
    return((ord(character) + key)%256)

def decrypt(character, key):
    return((ord(character) - key)%256)

def doStuff(filein, fileout, key, mode):
    # PROTIP: pythonic way
    with open(filein, mode="rb") as fin:
        with open(fileout, mode="wb") as fout:
            # READING BINARY FILE IN PYTHON
            # https://www.stackvidhya.com/python-read-binary-file/#:~:text=You%20can%20open%20the%20file%20using%20open()%20method%20by,binary%20file%20in%20read%20mode.&text=b%20%E2%80%93%20To%20specify%20it's%20a,string%20attempt%20will%20be%20made. 
            byte = fin.read(1)
            # do stuff
            arr = bytearray()
            while byte:
                if mode == "e":
                    #Encrypt Data
                    arr.append(encrypt(byte, key))
                elif mode == "d":
                    #Decrypt Data
                    arr.append(decrypt(byte, key))
                else:
                    print("Error in handling mode")
                    return
                byte = fin.read(1)
            fout.write(arr)
            # file will be closed automatically when interpreter reaches end of the block


# our main function
if __name__ == "__main__":
    # set up the argument parser
    av = []
    for x in range(0, 256):
        av.append(x)
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="filein", help="input file")
    parser.add_argument("-o", dest="fileout", help="output file")
    parser.add_argument("-k", "--key", type=int, choices=av, help="Specify key")
    parser.add_argument("-m", "--mode", type=str, default="e", choices={"e","d"}, help="Encryption or Decryption")

    # parse our arguments
    args = parser.parse_args()
    filein = args.filein
    fileout = args.fileout
    mode = args.mode
    key = args.key

    doStuff(filein, fileout, key, mode)

    # all done
