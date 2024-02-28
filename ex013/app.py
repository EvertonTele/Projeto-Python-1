# Faça um algoritimo que leia o salario de um funcionário e mostre seu novo salário com 15% de aumento
# ex: 
salario_funcionario = float(input('Informe seu salário '))
porcentagem  = 15
salario_aumento = (salario_funcionario*porcentagem)/100
salario_novo = salario_aumento+salario_funcionario
print ('O salario com aumento será de R${:.2f}'.format(salario_novo))
