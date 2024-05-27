# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

# valor_do_imovel = int(input('Qual o valor da sua casa?'))
# salario = int(input('Digite seu salário'))
# # prazo = int(input('Prazo de Pagamento'))

imovel = float(input('Qual o valor da sua casa: R$ '))
salario = float(input('Digite seu salário: R$ '))
prazo = float(input('Prazo de Pagamento? '))
parcela =  imovel /(prazo*12) 
prestacao_mensal = salario *30 / 100
print('Para pagar uma casa de R${:.2f} em {}anos'.format(imovel, prazo), end='')
print('a prestação seá de R${:.2f}'.format(parcela))
if parcela <= prestacao_mensal:
    print('Parecla CONCEDIDA! ')
else:
    print('Parcela NEGADA! ')



