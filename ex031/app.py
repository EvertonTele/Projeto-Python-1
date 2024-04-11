# Desenvolva um programa que pergunte a distância
# de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de atpe 200KM e R$0,45 para viagens mais longas.  

distancia = float(input('Digite a Distância: '))
viagem_ate_200 = distancia * 0.50
viagens_longas = distancia * 0.45
if distancia <= 200:
    print('O valor da sua viagem R${:.2f}'.format(viagem_ate_200))
else:
    print('Valor daviagem acima de 200KM R${:.2f}'.format(viagens_longas))




