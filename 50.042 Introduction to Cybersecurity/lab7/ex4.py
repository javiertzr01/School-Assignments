import ex2
from Crypto.PublicKey import RSA
import random


if __name__ == "__main__":
    key = open('mykey.pem.pub', 'r').read()
    rsakey_pub = RSA.importKey(key)
    key = open('mykey.pem.priv', 'r').read()
    rsakey_priv = RSA.import_key(key)

    m = open("message.txt", "r").read()

    # Alice's public key
    e = rsakey_pub.e
    n_pub = rsakey_pub.n

    d = rsakey_priv.d
    n_priv = rsakey_priv.n

    # Alice's part
    # 1024-bit integer s
    s = random.getrandbits(1024)
    # Message from s
    x = ex2.square_multiply(s, e, n_pub)

    # Bob's part
    x_prime = ex2.square_multiply(s, e, n_pub)
    
    # Check if x_prime == x
    print(x == x_prime)
    assert(x == x_prime)