# Escreva um programa que leia número inteiro qualquer e peçar para o usuário escolher qual será a base de conversão:

# - 1 para binário
# - 2 para octal 
# - 3 para hexadecimal

numero_conversão = int(input('Digite um número: '))
print('Escolha a base de conversão')
print('[1] - Binário ')
print('[2]- Octal ')
print('[3] - Hexadecimal ')
Opcao = int(input('Digite a opção desejada: '))
if Opcao == 1:
    print('O número {} em binário {}'.format(numero_conversão, bin(numero_conversão)[2:])) #Processo de fatiação [2:] tirando o inicio deixando só os números. 
elif Opcao == 2:
    print('o nuemro {} um número em octal é {}! '.format(numero_conversão, oct(numero_conversão)[2:]))
elif Opcao == 3:
    print ('o numero {} em  exadecimal é {}! '.format(numero_conversão, hex(numero_conversão)[2:]))
    





