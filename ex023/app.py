#  Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados. 
# Ex: Digite um número:1834
# unidade:4
# dezena:3
# centena:8
# milhar:1
número = int(input('Digite um número: '))
n = str(número)
print('Unidade:',n[3])
print('Dezena:',n[2])
print('Centena:',n[1])
print('Milhar:',n[0])
