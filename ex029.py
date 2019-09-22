# Radar eletronico


velocidade_carro = int(input('A quantos KM/H você esta: '))
multa = (velocidade_carro - 80) * 7

if velocidade_carro >= 80:
    print('Você esta acima da velocidade permitida sua muta é de R${}'.format(multa))

else:
    print('Você esta na velocidade permitida!')
