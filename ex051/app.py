# Desenvolva um programa que leia o primeiro termo e a razão de um PA. no final, mostre os 10 primeiros termos dessa progressão.
num = int(input('Digite uma PA: '))
raz = int(input('Digite uma RAZÂO: '))
print('Os 10 primeiro temos da PA são: ')
for c in range(10):
    termo = num + c * raz
    print(termo)
