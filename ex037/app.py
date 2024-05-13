# Escreva um programa que leia número inteiro qualquer e peçar para o usuário escolher qual será a base de conversão:

# - 1 para binário
# - 2 para octal 
# - 3 para hexadecimal

numero_conversão = float(input('Digite um número: '))
print('Escolha a base de conversão')
print('1 - Binário ')
print('2 - Octal ')
print('3 - Hexadecimal ')
Opcao = str('Digite a opção desejada')

if Opcao == 1:
    print('O número é binário', bin(numero_conversão))
elif Opcao == 2:
    print('é um número octal! ', oct(numero_conversão))
elif Opcao == 3:
    print ('É um núemro exadecimal! ', hex(numero_conversão))
