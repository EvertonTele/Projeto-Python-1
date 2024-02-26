# Faça um programa que leia um numéro inteiro e mostre na tela o seu sucessor e seu antecessor
# Exemplo: ler o valor 8 depois do 8 vem 9 e antes do 8, 7
n1 = int(input('Digite um número'))
sucessor = n1+1 
antecessor = n1-1
print('sucesso igual a {} e o antecessor é {} '.format(sucessor, antecessor))