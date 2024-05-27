# Faça um programa que leia o ano de um jovem e informe, de acordo com sua idade: 

# - Se ele ainda vai se alistar ao serviço militar. 
# - Se é hora de se alistar. 
# - se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o campo que falta ou que passou do prazo. 

from datetime import date
ano_taual = date.today().year
data = int(input('Ano de Nascimento: '))
idade = ano_taual - data
tempo = data - idade
print('Ano de nascimento {}'.format(idade))
if idade <=17:
    print('Você ainda vai se alistar no serviço militar! ')
elif idade ==18:
    print('Está na hora de se alista ao servço militar! ')
else:
    print('Você passou do tempo de alistamento! ')
    print('{} anos que você passou do seu alistamento. '.format(tempo))

 

# ano_atual = date.today().today
# data = int(input('Ano de nascimento: '))
# idade = ano_atual - data
# print('Ano de nascimento {}'.format(idade))
# if idade <=17:
#     print('Você ainda vai se alistar ao serviço militar! ')
# elif idade ==18:
#     print('Está na hora se alistar no serviço militar! ')
# else:
#     print('Você passsou do tempo de alistamento! ')

