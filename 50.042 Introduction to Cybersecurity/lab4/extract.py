#!/usr/bin/env python3
# ECB plaintext extraction skeleton file for 50.042 FCS

import argparse
from itertools import count

def getInfo(headerfile):
    with open(headerfile, 'rb') as fin:
        header = fin.read()
        header_len = len(header)
    return header, header_len

def extract(infile,outfile,headerfile):
    header, header_len = getInfo(headerfile)
    encrypted = []
    with open(infile, 'rb') as fin:
        with open(outfile, 'wb') as fout:
            fin.read(header_len + 1)
            while True:
                block = fin.read(8)
                if block == b'':
                    break
                else:
                    encrypted.append(block)

            # Find the most common blocks --> either 0 or 1
            count_dict = {}
            for block in encrypted:
                if block not in count_dict:
                    count_dict[block] = 1
                else:
                    count_dict[block] += 1
            
            freq = 0
            for block, count in count_dict.items():
                if count > freq:
                    most_freq_block = block
                    freq = count
            
            # Since each block is 8 bytes, b'0' * 8
            decrypted = []
            for block in encrypted:
                if block == most_freq_block:
                    decrypted.append(b'0' * 8)
                else:
                    decrypted.append(b'1' * 8)
            
            decrypted_decoded = []
            for block in decrypted:
                decrypted_decoded.append(block.decode())
            decrypted_decoded = "".join(decrypted_decoded)
            decrypted_decoded = decrypted_decoded.encode()
            
            fout.write(header) # 15 bytes
            fout.write(b'\n')  # to make it 16 bytes
            fout.write(decrypted_decoded)
            
            return True

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Extract PBM pattern.')
    parser.add_argument('-i', dest='infile',help='input file, PBM encrypted format')
    parser.add_argument('-o', dest='outfile',help='output PBM file')
    parser.add_argument('-hh', dest='headerfile',help='known header file')

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    headerfile=args.headerfile

    print('Reading from: %s'%infile)
    print('Reading header file from: %s'%headerfile)
    print('Writing to: %s'%outfile)

    success=extract(infile,outfile,headerfile)
