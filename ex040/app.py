# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média antiga: 

# - Média abaixo de 5.0: Reprovado 
# - média entre 5.0 e 6.9: Recuperação 
# - média 7.0 : aprovado

nota1 = int(input('Digite sua primeira nota: '))
nota2 = int(input('Digite sua segunda nota! '))
media = (nota1+nota2)/2
print('A média do aluno é {}'.format(media))
if media >=7.0:
    print('Você está aprovado! ')
elif media >= 5.0  and 6.9:
    print('Você está de recuperação! ')
else:
    print('Você está reprovado! ')