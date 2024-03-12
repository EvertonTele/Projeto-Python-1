#  Um professor que sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido. 
# O profesor que sortear um dos alunos para pagar o quadro. 
import random
nome1 = str(input('Digite seu nome '))
nome2 = str(input('Digite seu nome  '))
nome3 = str(input('Digite seu nome  '))
nome4 = str(input('Digite seu nome  '))
lista = [nome1, nome2, nome3, nome4 ]
sorteio = random.choice(lista)
print('o nome sorteado é {}'.format(sorteio))




