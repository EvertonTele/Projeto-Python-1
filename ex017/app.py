# Faça um programa que leia o comprimento do cateto aposto e do cateto adjacente de um triangulo retângulo, calcule e mostre o comprimento hipotenusa. 
import math 
cateto1 = int(input('Digite o comprimento  '))
cateto2 = int(input('Digite o comprimento '))
hipotenusa = math.sqrt (cateto1**2+cateto2**2) 
print('A hipotenusa é {:.2f}'.format(hipotenusa))
