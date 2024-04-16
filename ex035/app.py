# Desenvolva um programa que leia o comprimento de três retas e diga ao usuáio se elas podem ou não formar um triângulo. 
# Ex: 
# r1----------
# r2--------
# r3-----------
# # essas retas podem formar um triangulo ? 

print('-='*20)
print('Analisador de Triaângulos ')
print('-='*20)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMA triângulo! ')
else:
    print('Os segmentos acima NÂO PODEM FORMAR triângulo! ')