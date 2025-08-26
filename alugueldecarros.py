modelo = input('qual o modelo do carro? ')
km = float(input('quantos km ele rodou? '))
dias = int(input('quantos dias foi alugado? '))
res1 = dias * 60
res2 = km * 0.15
resfim = res1 + res2
print('o valor do aluguel do {1} alugado será: R${0} !'.format(resfim, modelo))