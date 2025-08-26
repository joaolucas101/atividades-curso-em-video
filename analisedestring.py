frase = "joão é foda e gosta de estudar t.i"
print ("a frase tem {} caracteres".format(len(frase)))
'''aqui o len  vai identificar quantos caracteres tem a frase'''
print ("a frase tem {} vezes a letra 'o'".format(frase.count('o')))
'''ele vai contar quantas vezes tem 'o' na frase'''
print ("a frase tem {} vezes a letra 'o'".format(frase.count('o', 4, 35)))
'''ele vai contar quantas vezes tem 'o' do 0 ate o 45 que seria o final da frase, de acordo com a quantidade de caracteres na frase'''
print("foi encontrado a partir da posição {}".format(frase.find('oda')))
'''ele vai dizer a posição onde os caracteres escolhidos foram encontrados na frase'''
print("esta palavra existe em '{}'?\n {}".format(frase,'joão' in frase ))
'''ele vai procurar se a palavra ou caractere existe em 'frase' '''