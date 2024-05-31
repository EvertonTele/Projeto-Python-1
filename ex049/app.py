# refaça o Desafio 09, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input('Digite um número para ver sua taboada! '))
print('numero da taboada {}'.format(num))
for nu in range (0, 11):
    resultado = num * nu
    print('{} x {} = {}'.format(num, nu, resultado))
