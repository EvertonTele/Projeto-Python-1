# Crie um programa que faça o computador jogar jokenpô com você 
from random import randint
from time import sleep # colocando pra demorar 1 segundo 
itens = ('Pedra', 'Papel', 'tesoura' )
computador = randint (0, 2) # O computador vai jogar o número de 1 a 2
print('''Suas opções:
[0] Pedra 
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qul a sua jogada? '))
print('JO')
sleep(1)  # Colocando para demora na tela 1 segundo. 
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-='*10)
print('Computadr jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*10)
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogador INVÀLIDO! ')
elif computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogador INVÀLIDO! ')
elif computador == 2: #Computador jogou tesoura 
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogador INVÀLIDO! ')


