# Faça um programa que leia um angulo na tela o valor do seno, cosseno e tangente desse angulo. 
import math
hipotenusa = int(input('Digite uma largura '))
seno = math.sin(hipotenusa)
cosseno = math.cos(hipotenusa)
tangente = math.tan(hipotenusa)
print('O valor de Seno é {}, Cosseno {} e tangente {}'.format(seno, cosseno, tangente))

