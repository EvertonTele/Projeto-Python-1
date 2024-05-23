# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: 

# - Á vista dinheiro/ cheque: 10% de desconto 
# - Á vista no cartão: 5% de desconto 
# - em até 2x no cartão: preço normal 
# - 3x ou mais no cartão 20% de juros. 

Valor = float(input('Digite o valor do produto: '))
print('Escola a forma de pagamento! ')
print('1. Valor a vista dinheiro/ Cheque: 10(%) de desconto! ')
print('2. Valor á vista no cartão: 5(%) de desconto! ')
print('3.Valor dividido em até 2x no cartão: Preçop normal! ')
print('4. Valor 3x ou mais no cartão 20(%) de juros! ')
Opcao = int(input('Escolha a opção de 1-4: '))
if  Opcao ==1:
    Valor_final = Valor *0.90
    print('Você escolheu a forma á vista sua forma de pagamento, o valor cobrado será de R${}'.format(Valor_final))
elif Opcao == 2:
    valor_final = Valor*0.95
    print('Você escolheu a forma de pagamento á vista no cartão, o valor a ser cobrado é de R${}'.format(valor_final))
elif Opcao == 3:
    valor_final = Valor
    print('Você escolheu dividir em até 2x no cartão seu valor é de R${}'.format(valor_final))
else:
    valor_final = Valor* 1.20
    print('Você escolheu a forma de pagamento acima de 3x no cartão, o valor a ser cobrado é de R${}'.format(valor_final))



