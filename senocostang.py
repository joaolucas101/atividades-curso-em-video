import math
angulo = float(input('digite o angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print("o seno do angulo vale {:.2f}\n o cosseno {:.2f}\n e a tangente {:.2f}".format(seno, cosseno, tangente))
