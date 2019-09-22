'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

rodado = float(input('Km Rodado: '))
dias = int(input('Dias Alugados: '))
valor = ((rodado * 0.15) + (dias * 60))

print('O Valor Total Será De R${}'.format(valor))
