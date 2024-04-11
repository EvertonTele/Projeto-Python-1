# Faça um programa que leia um ano qualquer e mostre se ele é um ano BISSEXTO
ano = int(input('Digite o ano'))
if ano %4 == 0:
    print('Estamos em um ano Bissexto ')
else:
    print('Não estamos em um ano Bissexto ')