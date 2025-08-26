import random
aluno1 = input("nome do primeiro aluno ")
aluno2 = input("nome do segundo aluno ")
aluno3 = input("nome do terceiro aluno ")
aluno4 = input("nome do quarto aluno ")
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print("a ordem dos alunos vai ser: {}".format(lista))