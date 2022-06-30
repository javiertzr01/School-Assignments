import primes
import babygiant
import dhke
import answer
import random

if __name__ == "__main__":
    p = 262147
    alpha = random.randint(2,p-2)
    a_priv = dhke.gen_priv_key(p)
    b_priv = dhke.gen_priv_key(p)
    A = dhke.get_pub_key(alpha, a_priv, p)
    B = dhke.get_pub_key(alpha, b_priv, p)
    sharedkey = dhke.get_shared_key(B, a_priv, p)
    a = babygiant.baby_giant(alpha, A, p)
    b = babygiant.baby_giant(alpha, B, p)
    guesskey1 = primes.square_multiply(A, b, p)
    guesskey2 = primes.square_multiply(B, a, p)
    print("Length of key is %d bits." % sharedkey.bit_length())
    print("Guess key 1:", guesskey1)
    print("Guess key 2:", guesskey2)
    print("Actual shared key :", sharedkey)