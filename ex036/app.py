# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

# valor_do_imovel = int(input('Qual o valor da sua casa?'))
# salario = int(input('Digite seu salário'))
# # prazo = int(input('Prazo de Pagamento'))

imovel = float(input('Qual o valor da sua casa?'))
salario = float(input('Digite seu salário'))
prazo = float(input('Prazo de Pagamento'))
parcela =  imovel / prazo
prestacao_mensal = salario + salario *0.30
if parcela >= prestacao_mensal:
    print(f'a parcela não pode exceder 30 % do seu salário, valor da parcela {parcela:.2f}')
else:
    print(f' valor da parcela é de {parcela:.2f}')