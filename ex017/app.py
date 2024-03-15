# Faça um programa que leia o comprimento do cateto aposto e do cateto adjacente de um triangulo retângulo, calcule e mostre o comprimento hipotenusa. 
import math 
cateto1 = float(input('Digite o comprimento  '))
cateto2 = float(input('Digite o comprimento '))
hipotenusa = math.sqrt (cateto1**2+cateto2**2) 
print('A hipotenusa é {:.2f}'.format(hipotenusa))



# Outra possibilidade 
# import math 
# cateto1 = float(input('Digite o comprimento  '))
# cateto2 = float(input('Digite o comprimento '))
# hipotenusa = math.hypot (cateto1, cateto2) 
# print('A hipotenusa é {:.2f}'.format(hipotenusa))
