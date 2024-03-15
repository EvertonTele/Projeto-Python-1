# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. 
# Exemplo: Digite um número:6.127 o número 6.127 tem a parte inteira 6. 
import math 
numero = float(input('Digite um numero '))
print('O numreo inteiro é {} e a sua porção inteira será {}'.format(numero, math.trunc(numero)))



# # Outra forma de se fazer

# from math import trunc 
# numero = float(input('Digite um numero '))
# print('O numreo inteiro é {} e a sua porção inteira será {}'.format(numero, trunc(numero)))


# A Forma que eu tinha feito 

# import math 
# numero = int(input('Digite um numero '))
# porção = math.sqrt(numero)
# print('O numreo inteiro é {:.2f}'.format(math.floor(numero, porção)))
