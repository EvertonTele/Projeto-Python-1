# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. se o valor digitado for impar, desconsidere-o
s = 0
for c in range(6):
    numero=int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        s  += numero
print('A soma dos pares é {}'. format(s))
# else:
# print('')

    