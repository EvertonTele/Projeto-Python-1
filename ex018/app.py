# Faça um programa que leia um angulo na tela o valor do seno, cosseno e tangente desse angulo. 
# import math
# hipotenusa = float(input('Digite uma largura '))
# seno = math.sin(hipotenusa)
# cosseno = math.cos(hipotenusa)
# tangente = math.tan(hipotenusa)
# print('O valor de Seno é {:.2f}, Cosseno {:.2f} e tangente {:.2f}'.format(seno, cosseno, tangente))

from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo'))
seno = sin(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem o TANGENTE {:.2f}'.format(angulo, tangente))