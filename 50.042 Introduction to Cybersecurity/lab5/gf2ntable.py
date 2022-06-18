from gf2n import Polynomial2, GF2N

ip = Polynomial2([1,0,0,1,1])

with open("table.txt", "w") as fout:
    for i in range(2**4):
        for j in range(2**4):
            g1 = GF2N(i, 4, ip)
            g2 = GF2N(j, 4, ip)
            
            fout.write(f"g1: {g1}, g2: {g2}\n")
            fout.write(f"add: {g1.add(g2)}\n")
            fout.write(f"mul: {g1.mul(g2)}\n\n")
