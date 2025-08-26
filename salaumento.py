salario = float(input('digite seu salário: '))
porcento15 = salario * (15 / 100)
res1 = salario + porcento15
res2 = res1 - salario
print('o seu novo salario será de {}!\n portanto teve um aumento de R${}'.format(res1, res2))