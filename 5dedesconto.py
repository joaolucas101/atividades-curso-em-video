produto = input('digite o nome do produto: ')
preco = float(input('digite o preço do(a) {}: '.format(produto)))
porcento5 = preco * (5/100)
res = preco - porcento5
print("o novo valor do(a) {} com desconto de 5% aplicado é: {}".format(produto,res ))