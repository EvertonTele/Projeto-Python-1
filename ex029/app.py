# Escrevea um programa que leia a velocidade de um carro. 

# Se ele ultrapassar 80k/h, mostre uma mensagem dizendo que ele foi multado. 

# A multa vai custar R$7,00 por cada KM acima do limite. 

Velocidade = float(input('Digite a velocidade '))
valor_multa = (Velocidade - 80) * 7.00
if Velocidade > 80:
    print('Você foi multado')
    print('A multa custa R$7,00 por KM acima do limite. ')
    # print('O valor da multa é R${:.2f}'.format(valor_multa))
    print(f'O valor da multa é R${valor_multa:.2f}')
else:
    print('Voce não foi multado...')



