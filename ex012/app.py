# Faça um algoritmo que leia a preço de um produto e mostre seu novo preço, com 5% de desconto.
# Ex: qual o preço do produto? 50, na liquidação o preço terá 5% de desconto
Valor_produto = float(input('Digite o valor do produto '))
desconto = 5 
valor_com_desconto = (Valor_produto*desconto)/100
print ('Valor do produto {}, valor do desconto {}, total de desconto {}'.format(Valor_produto, desconto, valor_com_desconto))