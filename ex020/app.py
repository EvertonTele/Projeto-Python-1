# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos de alunos. Faça o nome dos quatros alunos e mostre a ordem sorteada. 
import random
nome1 = str(input('Digite seu nome '))
nome2 = str(input('Digite seu nome  '))
nome3 = str(input('Digite seu nome  '))
nome4 = str(input('Digite seu nome  '))
lista = [nome1, nome2, nome3, nome4 ]
sorteio = random.choice(lista)
print('o nome sorteado é {}'.format(sorteio))
print('1º colocado é{}, 2º {}, 3º {}, 4º{}'.format(sorteio, nome1, nome2, nome3, nome4)) 

# resposta do exercicio 
# from random import shuffle
# n1 = str(input('Primeiro aluno'))
# n2 = str(input('Segundo aluno '))
# n2 = str(input('Terceiro aluno '))
# n4 = str(input ('Quarto aluno  '))
# lista = [n1, n2, n3, n4]
# shuffle(lista)
# print('A ordem de apresentação será ')
# print(lista)