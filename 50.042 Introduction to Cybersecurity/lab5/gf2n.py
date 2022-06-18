# 50.042 FCS Lab 5 Modular Arithmetics
# Year 2021

import copy
class Polynomial2:
    def __init__(self,coeffs):
        self.coeffs = coeffs
        self.coeffs_len = len(coeffs)

    def check_degree(self, p2):
        p2_coeffs = copy.deepcopy(p2.coeffs)
        if p2.coeffs_len > self.coeffs_len:
            extra_needed = p2.coeffs_len - self.coeffs_len
            for i in range(extra_needed):
                self.coeffs.append(0)
                self.coeffs_len += 1
        if self.coeffs_len > p2.coeffs_len:
            extra_needed = self.coeffs_len - p2.coeffs_len
            for i in range(extra_needed):
                p2_coeffs.append(0)
        return Polynomial2(p2_coeffs)
    def add(self,p2):
        p2_new = self.check_degree(p2)
        result = []
        for i in range(self.coeffs_len):
            result.append(self.coeffs[i] ^ p2_new.coeffs[i])
        return Polynomial2(result)

    def sub(self,p2):
        return self.add(p2)

    def mul(self,p2,modp=None): # modulus is done with respect to modp
        p2_new = self.check_degree(p2) # To compute from p2, not exactly a replica of P2
        results = []
        result = Polynomial2([0])
        
        # For Polynomial
        for idx in range(self.coeffs_len):
            temp_result = Polynomial2(p2_new.coeffs)
            if self.coeffs[idx] == 0:
                continue
            else:
                for power in range(idx):
                    MSB = temp_result.coeffs[-1]
                    if modp == None:
                        temp_result = temp_result.shift_right()
                    elif MSB == 0:
                        temp_result = temp_result.shift_right() # Shift 1 bit to the left
                        temp_result = Polynomial2(temp_result.coeffs[:-1])
                    else:
                        temp_result = temp_result.shift_right()
                        if temp_result.coeffs_len >= modp.coeffs_len:
                            temp_result = Polynomial2(temp_result.coeffs[:(modp.coeffs_len-1)]).add(Polynomial2(modp.coeffs[:-1])) # XOR operation same as adding; only do a reduction if power too high
            results.append(temp_result)
        for item in results:
            result = result.add(item)
        return result
            

    def shift_right(self): # Shift one bit to the left means shift array to the right
        return Polynomial2([0] + self.coeffs)
    
    def deg(self):  # degree of polynomial
        for i in range(self.coeffs_len - 1, -1, -1):
            if self.coeffs[i] == 1:
                return i
        return 0
    
    def lc(self):   # leading coeff of polynomial
        return (self.coeffs[self.deg()])

    def div(self,p2): # self = a, p2 = b
        q = Polynomial2([0])
        r = copy.deepcopy(self)
        b = copy.deepcopy(p2)
        d = b.deg()
        c = b.lc()
        
        while r.deg() >= d:
            #compute s, s * b within remainder
                # set coeff of x to lead coeff of remainder/c
                # set power of x to : deg of remainder - deg of b
            # s = Polynomial2([0 for i in range(r.deg() - d)] + [(r.lc()//c)])
            s = Polynomial2([0 for i in range(r.deg() - d)] + [1])
            q = q.add(s)
            r = r.sub(s.mul(b))
        return q, r

    def __str__(self):
        result = []
        for i in range(self.coeffs_len-1, -1, -1):
            if self.coeffs[i] == 1:
                result.append(f"x^{i}")
        return "+".join(result)

    def getInt(self):
        result = 0
        for idx, coeff in enumerate(self.coeffs):
            result += (2**idx) * coeff
        return result


class GF2N:
    affinemat=[[1,0,0,0,1,1,1,1],
                [1,1,0,0,0,1,1,1],
                [1,1,1,0,0,0,1,1],
                [1,1,1,1,0,0,0,1],
                [1,1,1,1,1,0,0,0],
                [0,1,1,1,1,1,0,0],
                [0,0,1,1,1,1,1,0],
                [0,0,0,1,1,1,1,1]]

    def __init__(self,x,n=8,ip=Polynomial2([1,1,0,1,1,0,0,0,1])):
        self.x = x
        self.n = n
        self.ip = ip

    def add(self,g2):
        result = self.p.add(g2.p)
        
        if result.coeffs_len >= self.ip.coeffs_len:
            result = Polynomial2(result.coeffs[:(self.ip.coeffs_len-1)]).add(Polynomial2(self.ip.coeffs[:-1]))
        
        return GF2N(result.getInt(), self.n, self.ip)
    def sub(self,g2):
        return self.add(g2.p)
    
    def mul(self,g2):
        result = self.p.mul(g2.p, self.ip)
        return GF2N(result.getInt(), self.n, self.ip)

    def div(self,g2):
        retq, retr = self.p.div(g2.p)
        return GF2N(retq.getInt(), self.n, self.ip), GF2N(retr.getInt(), self.n, self.ip)

    @property
    def p(self):
        return self.getPolynomial2()
    
    def getPolynomial2(self):
        binary_string = str(bin(self.x))[2::]
        reverse_binary_string = binary_string[::-1]
        ls = [int(i) for i in reverse_binary_string]
        return Polynomial2(ls)

    def __str__(self):
        return str(self.getInt())

    def getInt(self):
        return self.p.getInt()

    def mulInv(self):
        pass

    def affineMap(self):
        pass

print ('\nTest 1')
print ('======')
print ('p1=x^5+x^2+x')
print ('p2=x^3+x^2+1')
p1=Polynomial2([0,1,1,0,0,1])
p2=Polynomial2([1,0,1,1])
p3=p1.add(p2)
print ('p3= p1+p2 = ',p3)

print ('\nTest 2')
print ('======')
print ('p4=x^7+x^4+x^3+x^2+x')
print ('modp=x^8+x^7+x^5+x^4+1')
p4=Polynomial2([0,1,1,1,1,0,0,1])
# modp=Polynomial2([1,1,0,1,1,0,0,0,1])
modp=Polynomial2([1,0,0,0,1,1,0,1,1])
p5=p1.mul(p4,modp)
print ('p5=p1*p4 mod (modp)=',p5)

print ('\nTest 3')
print ('======')
print ('p6=x^12+x^7+x^2')
print ('p7=x^8+x^4+x^3+x+1')
p6=Polynomial2([0,0,1,0,0,0,0,1,0,0,0,0,1])    
p7=Polynomial2([1,1,0,1,1,0,0,0,1])
p8q,p8r=p6.div(p7)
print ('q for p6/p7=',p8q)
print ('r for p6/p7=',p8r)

####
print ('\nTest 4')
print ('======')
g1=GF2N(100)
g2=GF2N(5)
print ('g1 = ',g1.getPolynomial2())
print ('g2 = ',g2.getPolynomial2())
g3=g1.add(g2)
print ('g1+g2 = ',g3)

print ('\nTest 5')
print ('======')
ip=Polynomial2([1,1,0,0,1])
print ('irreducible polynomial',ip)
g4=GF2N(0b1101,4,ip)
g5=GF2N(0b110,4,ip)
print ('g4 = ',g4.getPolynomial2())
print ('g5 = ',g5.getPolynomial2())
g6=g4.mul(g5)
print ('g4 x g5 = ',g6.p)

print ('\nTest 6')
print ('======')
g7=GF2N(0b1000010000100,13,None)
g8=GF2N(0b100011011,13,None)
print ('g7 = ',g7.getPolynomial2())
print ('g8 = ',g8.getPolynomial2())
q,r=g7.div(g8)
print ('g7/g8 =')
print ('q = ',q.getPolynomial2())
print ('r = ',r.getPolynomial2())

# print '\nTest 7'
# print '======'
# ip=Polynomial2([1,1,0,0,1])
# print 'irreducible polynomial',ip
# g9=GF2N(0b101,4,ip)
# print 'g9 = ',g9.getPolynomial2()
# print 'inverse of g9 =',g9.mulInv().getPolynomial2()

# print '\nTest 8'
# print '======'
# ip=Polynomial2([1,1,0,1,1,0,0,0,1])
# print 'irreducible polynomial',ip
# g10=GF2N(0xc2,8,ip)
# print 'g10 = 0xc2'
# g11=g10.mulInv()
# print 'inverse of g10 = g11 =', hex(g11.getInt())
# g12=g11.affineMap()
# print 'affine map of g11 =',hex(g12.getInt())
