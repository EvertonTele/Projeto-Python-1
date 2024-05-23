# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: 

# - Abaixo de 18.5: Abaixo do Peso 
# - Entre 18.5 e 25: Peso ideal 
# - 25 até 30: Sobrepeso 
# - 30 até 40: Obesidade 
# - Acima de 40: Obesidade mórbida

Peso = float(input('Digite o Peso: '))
Altura = float(input('Digite a Altura '))
imc = Peso/(Altura*Altura)
print('Seu IMC é {:.2f}'.format(imc))
if imc > 40:
    print('Você está com Obesidade Mórbida! ')
elif 30< imc <=40:
    print('Você está Obeso! ') 
elif 25 < imc <=30:
    print('Você está com Sobre peso! ')
elif 18.5 < imc <=25:
    print('Você está com o Peso Ideal! ')
else:
    print('Você está abaixo do peso! ')
    