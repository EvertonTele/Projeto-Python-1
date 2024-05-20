# Refaça o Desafio 035 dos triângulos acrecentando o recurso de mostrar que tipo de riâmgulo será formado:

# - Equilátero: Todos os lados iguais 
# - Isósceles=: dois lados iguais 
# - Escaleno: Todos os lados direferentes. 

print('-='*20)
print('Analisador de Triaângulos ')
print('-='*20)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('O triângulo é um Equilatero, todos os lados são iguais.  ')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('O triângylo é um Isóceles dois lados apenas são iguais. ')
else:
    print('O triangulo não foi formado é um Escaleno!  ')