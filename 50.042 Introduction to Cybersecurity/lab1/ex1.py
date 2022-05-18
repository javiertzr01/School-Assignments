#!/usr/bin/env python3
# SUTD 50.042 FCS Lab 1
# Simple file read in/out


# Import libraries
import sys
import argparse
import string

def encrypt(character, key):
    return(string.printable[(string.printable.index(character) + key)%100])

def decrypt(character, key):
    return(string.printable[(string.printable.index(character) - key)%100])

def doStuff(filein, fileout, key, mode):
    # # open file handles to both files
    # fin = open(filein, mode="r", encoding="utf-8", newline="\n")  # read mode
    # fin_b = open(filein, mode="rb")  # binary read mode
    # fout = open(fileout, mode="w", encoding="utf-8", newline="\n")  # write mode
    # fout_b = open(fileout, mode="wb")  # binary write mode
    # c = fin.read()  # read in file into c as a str
    # # and write to fileout

    # # close all file streams
    # fin.close()
    # fin_b.close()
    # fout.close()
    # fout_b.close()

    # PROTIP: pythonic way
    with open(filein, mode="r", encoding="utf-8", newline="\n") as fin:
        with open(fileout, mode="w", encoding="utf-8") as fout:
            text = fin.read()
            # do stuff
            if mode == "e":
                #Encrypt Data
                output = "".join(encrypt(character, key) for character in text)
            elif mode == "d":
                #Decrypt Data
                output = "".join(decrypt(character, key) for character in text)
            else:
                print("Error in handling mode")
                return
            fout.write(output)
            # file will be closed automatically when interpreter reaches end of the block


# our main function
if __name__ == "__main__":
    # set up the argument parser
    av = []
    for x in range(1, len(string.printable)):
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
