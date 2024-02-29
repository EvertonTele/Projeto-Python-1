# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e quantidade de dias pelos quais ele foi alugado. calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por KM rodado. 
dias_corrido = int(input('Digite a quantidade de dia '))
km_pecorridos = float(input('Digite o KM '))
valor_diária = 60
valor_km = 0.15
total = (valor_km*km_pecorridos) + valor_diária*dias_corrido
print ('O total da sua fatura será de {:.2f}'. format(total))
