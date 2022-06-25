# 50.042 FCS Lab 6 template
# Year 2021

import random
# square_multiply(a, x, n)
# {
#   y = 1
#   # n_b is the number of bits in x
#   for( i = n_b-1 downto 0 )
#   {
#     # square
#     y = y^2 mod n
#     # multiply only if the bit of x at i is 1
#     if (x_i == 1) y = a*y mod n
#   }
#   return y
# }

def square_multiply(a,x,n):
    y = 1
    x_in_bit = bin(x)[2:]
    x_bit_len = len(x_in_bit)
    for i in range(x_bit_len-1,-1,-1):
        y = (y*y)%n
        if x_in_bit[i-(x_bit_len-1)] == '1':    # Check from MSB
            y = (a*y)%n
    return y

def miller_rabin(n, a):
    pass

def gen_prime_nbits(n):
    pass

if __name__=="__main__":
    print(pow(11,13,53))
    print(square_multiply(11,13,53))
    
    
    # print('Is 561 a prime?')
    # print(miller_rabin(561,2))
    # print('Is 27 a prime?'
    # print(miller_rabin(27,2))
    # print('Is 61 a prime?'
    # print(miller_rabin(61,2))

    # print('Random number (100 bits):')
    # print(gen_prime_nbits(100))
    # print('Random number (80 bits):')
    # print(gen_prime_nbits(80))
