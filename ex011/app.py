# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintála, sabendo que cada litro de tinta, pinta uma área de 2m²
# Exemplo: qual a altura da parede, qual a area da parede 
largura = float(input(' digite a largura '))
altura = float(input(' digite a altura '))
area = largura * altura
litro_de_tinta = 2
litros_de_tinta = area/litro_de_tinta
print ('o valor da altura {}, o valor da largura {}, a parede tem {}m², então será necessário {}, litros de tintas '.format(altura, largura, area, litros_de_tinta))


# Resposta do exercicio 
# larg = float(input('Largura da parede: '))
# alt = float(input('Altura da parede '))
# área = larg*alt 
# print('Sua parede tem a dimensão de {}x{} e sua área é de {}M²'.format(larg, alt, área))
# tinta = área/2 
# print ('Para pintar essa parede, voçê precisará de {}l de tinta.'.format(tinta))