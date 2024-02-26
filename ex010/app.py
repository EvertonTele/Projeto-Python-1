# Crie um programa que leia quanto dinheiro de uma pessoa tem na certeira e mostre quantos dólares ele pode comprar. considere US$1,00=R$3,27
valor_real_carteira = float(input('valor em real R$ '))
valor_dolar = 1
valor_real = 3.27
valor_cambio = valor_dolar/ valor_real
valor_total = valor_cambio* valor_real_carteira
print (' e o valor que eu terei após a troca é de {:.2f} dolares  '.format(valor_total))




