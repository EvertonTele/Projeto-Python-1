# Aconfederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: 

# - Até 9 anos: Mirim
# - A´te 14 anos: Infantil 
# - Até 19 anos: Junio
# - Até 20 anos: Sênior 
# - Acima: Master. 

from datetime import date
ano_atual = date.today().year
nascimento = int(input('Digite o ano de nascimento: '))
idade = ano_atual - nascimento
print('Você tem {} anos! '.format(idade))
if idade > 20:
    print ('Você pertence a classe Master ! ')
elif idade >=20:
    print('Você faz parte da classe Senior! ')
elif idade >=19:
    print('Você faz parte da classe junior! ')
elif idade >=14:
    print('Vocé faz parte da classe Infantil! ')
else:
    print('Você pertence a classe Mirim! ')