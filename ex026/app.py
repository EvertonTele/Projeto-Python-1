# Um programa que leia uma frase pelo teclado e mostre:
# Qunatas vezes aparece a letra 'A'.
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

# nome = str(input('Digite seu nome completo '))
# nome1 = str(nome)
# print('A letra A aparece {}'.format (nome.count('a')))
# print(nome.upper().count('A'))



# Resolvendo o exercicio 
Frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase. '.format(Frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(Frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(Frase.rfind('A')+1))
