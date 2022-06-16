#!/usr/bin/env python3
# ECB wrapper skeleton file for 50.042 FCS

from present import *
import argparse

nokeybits=80
blocksize=64


def ecb(infile,outfile,key,mode):
    with open(key, 'r') as key_fin:
        reading = key_fin.read()
        present_key = int(reading, 16)
    
    with open(infile, 'rb') as fin:
        with open(outfile, 'wb') as fout:
            file_read = fin.read() # Read in big-endian
            number_of_blocks = int(len(file_read)/(64/8)) # must do number_of_blocks + 1 | 64/8 means 8 bytes per block
            # remainding_bytes = int(len(file_read)%(64/8)) # remainder of 7 bytes
            print(number_of_blocks)
            result = b''
            #Encryption
            if mode == 'e':
                result = b''
                for i in range(number_of_blocks + 1):
                    block_in_hexstring = ''
                    start = 8 * i
                    block_in_bytes = file_read[start: start+8]
                    if len(block_in_bytes) < 8:
                            block_in_bytes = block_in_bytes.ljust(8, b'0')
                    for byte in block_in_bytes:
                        convert_to_hex = hex(byte).lstrip('0x')
                        missing_zero_count = 2 - len(convert_to_hex)
                        block_in_hexstring += ('0'*missing_zero_count + convert_to_hex)
                    block_in_hex = int((block_in_hexstring), 16)
                    encrypted_block = present(block_in_hex, present_key)
                    encrypted_block_in_bytes = encrypted_block.to_bytes(8, byteorder = 'big')
                    result = result + encrypted_block_in_bytes
                    if i % 1000 == 0:
                        print(str(round((i/(number_of_blocks+1) * 100),1)) + "%" + " done")
                fout.write(result)
            # Decryption 
            if mode == 'd':
                result = b''
                for i in range(number_of_blocks + 1):
                    block_in_hexstring = ''
                    start = 8 * i
                    block_in_bytes = file_read[start: start+8]
                    for byte in block_in_bytes:
                        convert_to_hex = hex(byte).lstrip('0x')
                        missing_zero_count = 2 - len(convert_to_hex)
                        block_in_hexstring += ('0'*missing_zero_count + convert_to_hex)
                    if block_in_hexstring == '':
                        continue
                    block_in_hex = int((block_in_hexstring), 16)
                    encrypted_block = present_inv(block_in_hex, present_key)
                    encrypted_block_in_bytes = encrypted_block.to_bytes(8, byteorder = 'big')
                    
                    if i == number_of_blocks - 1:
                        encrypted_block_in_bytes = encrypted_block_in_bytes.rstrip(b'0')
                    
                    result = result + encrypted_block_in_bytes
                    if i % 1000 == 0:
                        print(str(round((i/(number_of_blocks+1) * 100),1)) + "%" + " done")
                fout.write(result)

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Block cipher using ECB mode.')
    parser.add_argument('-i', dest='infile',help='input file')
    parser.add_argument('-o', dest='outfile',help='output file')
    parser.add_argument('-k', dest='keyfile',help='key file')
    parser.add_argument('-m', dest='mode',help='mode')

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    keyfile=args.keyfile
    mode=args.mode
    
    # ecb(infile, outfile, keyfile, mode)
    ecb("Revision.pbm", "Tux_D.pbm", "key.txt", 'd')



