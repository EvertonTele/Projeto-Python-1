# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintála, sabendo que cada litro de tinta, pinta uma área de 2m²
# Exemplo: qual a altura da parede, qual a area da parede 
largura = int(input(' digite a largura '))
altura = int(input(' digite a altura '))
area = largura * altura
litro_de_tinta = 2
litros_de_tinta = area/litro_de_tinta
print ('o valor da altura {}, o valor da largura {}, a parede tem {}m², então será necessário {}, litros de tintas '.format(altura, largura, area, litros_de_tinta))