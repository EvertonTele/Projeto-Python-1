# Crie um programa que faça o computador jogar jokenpô com você 
from random import randint
itens = ('PEDRA', 'PAPEL','TESOURA')
computador = randint (0,2) # randint faz o computador escolher um número desejado. 
jogada = int(input('Qual o número da jogada? '))
print('='*20)
print('''JO
KEN
PO!!!''')
print('='*20)
print('O computador mandou escolheu {}'.format(itens, [computador]))


