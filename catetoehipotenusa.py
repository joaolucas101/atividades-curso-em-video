'''oposto = float(input("comprimneto do cateto oposto: "))
adja = float(input("comprimento do cateto adjascente: "))
res1 = oposto ** 2 + adja ** 2
res2 = res1 ** (1/2)
print("a hipotenusa vai medir {}!".format(res2))'''
import math
oposto = float(input("comprimneto do cateto oposto: "))
adja = float(input("comprimento do cateto adjascente: "))
hi = math.hypot(oposto, adja)
print ("a hipotenusa vai medir {}!".format(hi))