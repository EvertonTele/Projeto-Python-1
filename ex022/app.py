# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# O nome com todas as letras Maiúsculas 
# O nome com todas minúscula 
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome. 

nome = str(input('Digite seu nome Completo '))
print(nome.upper())
print(nome.lower())
print(len(nome.strip()))
dividindo = nome.split()
print(dividindo[0])

# Correção do exercicio 
# nome = str(input('Digite seu nome completo ')).strip()
# print('Analisando seu nome... ' )
# print('Seu nome em maiúsculo é {}'.format(nome.upper()))
# print('Seu nome em minúsculo é{}'.format(nome.lower()))
# print('Seu nome tem ao todo {} letras '.format(len(nome) - nome.count('')))
# # print ( 'Seu primeiro nome tem{} letras'. format(nome.find('')))
# separa = nome.split
# print('Seu primeiro nome é {} e ele tem {} letras'. format(separa[0], len(separa)))
