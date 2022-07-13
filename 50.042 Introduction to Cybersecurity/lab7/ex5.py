from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_PSS 
from Crypto.Hash import SHA256

def generate_RSA(bits=1024):
    key_priv = RSA.generate(bits)
    key_pub = key_priv.publickey()
    with open('generated_priv_key.pem', 'wb') as f:
        f.write(key_priv.exportKey('PEM'))
    with open('generated_pub_key.pem', 'wb') as f:
        f.write(key_pub.exportKey('PEM'))

def encrypt_RSA(public_key_file, message):
    # Read Public Key from file
    key = open(public_key_file, 'r').read()
    # Use RSA.importKey() to import the key
    rsakey_pub = RSA.importKey(key)
    # Create a new PKCS1_OAEP object 
    cipher = PKCS1_OAEP.new(rsakey_pub)
    # Use its encrypt method
    ciphertext = cipher.encrypt(message.encode())
    
    return ciphertext

def decrypt_RSA(private_key_file, ciphertext):
    # Read Private Key from file
    key = open(private_key_file, 'r').read()
    # Use RSA.importKey() to import the key
    rsakey_priv = RSA.importKey(key)
    # Create a new PKCS1_OAEP object
    cipher = PKCS1_OAEP.new(rsakey_priv)
    # Use its encrypt method
    plaintext = cipher.decrypt(ciphertext).decode()

    return plaintext
    
def sign_data(private_key_file, data):
    # Read Private Key from file
    key = open(private_key_file, 'r').read()
    # Use RSA.importKey() to import the key
    rsakey_priv = RSA.importKey(key)
    # Hash data
    hashed_data = SHA256.new(data.encode())
    # Readable hash data for debugging
    hashed_data_digest = hashed_data.hexdigest()
    # Create a new PKCS1_PSS object
    signature_holder = PKCS1_PSS.new(rsakey_priv)
    # Signing the data
    signature = signature_holder.sign(hashed_data)
    
    return signature

def verify_sign(public_key_file, sign, data):
    # Read Public Key from file
    key = open(public_key_file, 'r').read()
    # Use RSA.importKey() to import the key
    rsakey_pub = RSA.importKey(key)
    # Create a new PKCS1_PSS object
    signature_holder = PKCS1_PSS.new(rsakey_pub)
    # Hash data for verification
    hashed_data = SHA256.new(data.encode())
    # Readable hash data for debugging
    hashed_data_digest = hashed_data.hexdigest()
    # Verify
    try:
        signature_holder.verify(hashed_data, sign)
    except (ValueError, TypeError):
        return False
    
    return True

if __name__ == "__main__":
    # Generate key pair files
    generate_RSA()
    # Get data from mydata.txt
    message = open("mydata.txt", 'r').read()
    # Encrypt mydata.txt
    ciphertext = encrypt_RSA("generated_pub_key.pem", message)
    # Decrypt mydata.txt
    plaintext = decrypt_RSA("generated_priv_key.pem", ciphertext)
    # Signing text
    signature = sign_data("generated_priv_key.pem", plaintext)
    # Verify signature
    verification = verify_sign("generated_pub_key.pem", signature, plaintext)
    print(f"Signature verified? {verification}\n")
    
    
    
    # Protocol Attack
    plaintext = "100"
    print("Encrypting:   " + plaintext + "\n")
    multiplier = "2"
    # Encrypt plaintext
    ciphertext = encrypt_RSA("generated_pub_key.pem", plaintext)
    print("Result:\n" + str(ciphertext) + "\n")
    # Change ciphertext to integer
    ciphertext_in_int = int.from_bytes(ciphertext, 'big')
    # Encrypt multiplier
    multiplier_encrypted = encrypt_RSA("generated_pub_key.pem", multiplier)
    # Change encrypted multiplier to integer
    multiplier_encrypted_in_int = int.from_bytes(multiplier_encrypted, 'big')
    # Multiply them for new ciphertext
    compromised_ciphertext_in_int = ciphertext_in_int * multiplier_encrypted_in_int
    # Change compromised ciphertext to bytes
    compromised_ciphertext = compromised_ciphertext_in_int.to_bytes((compromised_ciphertext_in_int.bit_length() + 7) // 8, 'big')
    print("Modified to:\n" + str(compromised_ciphertext) + "\n")
    
    try:
        # Decrypt compromised ciphertext
        modified_plaintext = decrypt_RSA("generated_priv_key.pem", compromised_ciphertext)
        print("Decrypted:   " + modified_plaintext + "\n")
    except ValueError:
        # Cannot Decrypt, Ciphertext with incorrect length
        print("ValueError: Cannot decrypt. Ciphertext with incorrect length")
