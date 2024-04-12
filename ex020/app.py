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

