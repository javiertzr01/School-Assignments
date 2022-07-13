import ex2
from Crypto.PublicKey import RSA

if __name__ == "__main__":
    key = open('mykey.pem.pub', 'r').read()
    rsakey_pub = RSA.importKey(key)
    key = open('mykey.pem.priv', 'r').read()
    rsakey_priv = RSA.importKey(key)

    m = open("message.txt", "r").read()

    e = rsakey_pub.e
    n_pub = rsakey_pub.n

    d = rsakey_priv.d
    n_priv = rsakey_priv.n
    
    value = 100
    multiplier = 2
    print("Encrypting:   " + str(value))
    y = ex2.encryption(value, e, n_pub)
    print("Result:\n" + str(y))
    y_s = ex2.square_multiply(multiplier, e, n_pub)
    m = y * y_s
    print("Modified to:\n" + str(m))
    decrypted = ex2.decryption(m, d, n_priv)
    print("Decrypted:   " + str(decrypted))
