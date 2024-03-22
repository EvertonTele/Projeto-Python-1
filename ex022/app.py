# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# O nome com todas as letras Maiúsculas 
# O nome com todas minúscula 
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome. 

nome = str(input('Digite seu nome Completo '))
print(nome.upper())
print(nome.lower())
print(len(nome.strip()))
print(nome[0::])

