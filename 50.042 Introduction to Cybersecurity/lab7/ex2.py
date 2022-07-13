from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

def square_multiply(a, x, n):
    res = 1
    for i in bin(x).lstrip('0b'):
        res = res * res % n
        if (i == '1'):
            res = res * a % n
    # return 1
    return res

def encryption(m, e, n):
    return square_multiply(m, e, n)

def decryption(c, d, n):
    return square_multiply(c, d, n)

def convert_string_to_int(m):
    message_in_bytes = m.encode()
    message_in_int = int.from_bytes(message_in_bytes, 'big')
    return message_in_int

def convert_int_to_string(i):
    message_in_bytes = i.to_bytes((i.bit_length() + 7) // 8, 'big')
    """
    For future references:
    x.bit_length() returns the number of bits needed to represent the integer
    (x.bit_length() + 7) // 8 returns the number of BYTES needed to represent the integer
    """
    message_in_string = message_in_bytes.decode()
    return message_in_string

if __name__ == "__main__":
    key = open('mykey.pem.pub', 'r').read()
    rsakey_pub = RSA.importKey(key)
    key = open('mykey.pem.priv', 'r').read()
    rsakey_priv = RSA.import_key(key)

    
    
    m = open("message.txt", "r").read()

    e = rsakey_pub.e
    n_pub = rsakey_pub.n

    d = rsakey_priv.d
    n_priv = rsakey_priv.n
    
    
    # Hashing the original message
    m_hashed = SHA256.new(m.encode())
    # Get string from SHA256 hash object
    m_hashed_string = m_hashed.hexdigest()
    # Convert string to int
    m_hashed_int = convert_string_to_int(m_hashed_string)
    # Undergo decryption function
    signature = decryption(m_hashed_int, d, n_priv)     # signature is an int
    
    
    # verify signature
    signature_verify = encryption(signature, e, n_pub)  # signature_verify is an int
    # Convert int back to string
    m_hashed_prime = convert_int_to_string(signature_verify)
    
    # To confirm that the resulting exponentiation must be the same as the hash value of the plaintext
    print(m_hashed_string == m_hashed_prime)
    assert(m_hashed_string == m_hashed_prime)