# Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR
n = int(input('Digite um número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
mm = max(n, n2, n3)
m = min(n, n2, n3)
if mm&m:
    print('O maior número é {}'.format(mm))
    print('O menor número é {}'.format(m))
else:
    print('A sobra é {}')





# n = int(input('Digite um número: '))
# n2 = int(input('Digite o segundo número: '))
# n3 = int(input('Digite o terceiro número: '))


# # mm = max(n, n2, n3)
# # m = min(n, n2, n3)
# if :
#     print('O maior número é {}'.format(n))
#     print('O maior número é {}'.format(n))

# else:
#     print('O menor número é {}'.format(n))
