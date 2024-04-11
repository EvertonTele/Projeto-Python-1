# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários a R$1.250,00, calcule um aumento de 10%..
# Para os inferiores ou iguais, o aumento é de 15%..

salario = float(input('Digite seu salário '))
maior = 10
menor = 15
salario_meno = (salario*maior)/100
salario_mai = (salario*menor)/100
sala_n = salario_meno+salario
sala_nm = salario_mai+salario
if salario <= 1250:
    print('Seu salario é R${:.2f} '.format(sala_n))
else:
    print('Seu salario é R${:.2f}'.format(sala_nm))
