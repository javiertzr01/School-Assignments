# 50.042 FCS Lab 6 template
# Year 2021

import math
from re import I
import primes


def baby_step(alpha, beta, p, fname):
    m = math.ceil(math.sqrt(p-1))
    with open(fname, 'w') as fout:
        for xb in range(m):
            fout.write((str(((alpha ** xb) * beta) % p)) + "\n")

def giant_step(alpha, p, fname):
    m = math.ceil(math.sqrt(p-1))
    with open(fname, 'w') as fout:
        for xg in range(m):
            fout.write((str((alpha ** (xg * m)) % p)) + "\n")


def baby_giant(alpha, beta, p):
    m = math.ceil(math.sqrt(p-1))

    baby_step(alpha, beta, p, "babystep.txt")
    giant_step(alpha, p, "giantstep.txt")
    
    with open("babystep.txt",'r') as fin:
        babyls = fin.read().split("\n")
        
    with open("giantstep.txt", 'r') as f_in: #change here, just do theintersection list thing
        giantls = f_in.read().split("\n")
        
    ls = list(set(babyls).intersection(set(giantls)))
    while "" in ls:
        ls.remove("")
    
    if len(ls) != 0:
        xb = babyls.index(ls[0])
        xg = giantls.index(ls[0])
        return (xg * m - xb)
    
    return -1





if __name__ == "__main__":
    """
    test 1
    My private key is:  264
    Test other private key is:  7265
    """
    p = 17851
    alpha = 17511
    A = 2945
    B = 11844
    sharedkey = 1671
    a = baby_giant(alpha, A, p)
    b = baby_giant(alpha, B, p)
    guesskey1 = primes.square_multiply(A, b, p)
    guesskey2 = primes.square_multiply(B, a, p)
    print("Guess key 1:", guesskey1)
    print("Guess key 2:", guesskey2)
    print("Actual shared key :", sharedkey)
