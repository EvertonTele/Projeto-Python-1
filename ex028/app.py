# Escreva um programa que faça um computador "Pensar" em um número inteiro entre 0 e 5 e peça para o usúário tentar descobrir qual foi o número escolhido pelo computador 

# O programa deverá escrever a tela se o usuário venceu ou perdeu 

from random import shuffle
numero = int('0')
numero1 = int('1')
numero2 = int('3')
numero3 = int('4')
numero4 = int('5')
n_aleaorio = [numero, numero1, numero2, numero3, numero4]
shuffle(n_aleaorio)
digite = int(input('Digite um núnmero: '))
print('o número sorteado é {} '.format(n_aleaorio [0]))
if digite == n_aleaorio:
    print('Você acertou o numero Parabéns!  ')
else:
    print('Tente novamente, Boa sorte!  ')

# if == n_aleaorio
#     print('Você acertou o numero  ')
# else:
#     print('Você acertou o numero  ')