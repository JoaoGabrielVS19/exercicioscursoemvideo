distancia_viagem = int(input('Qual a distancia da viagem em KM: '))

if distancia_viagem >= 200:
    valor = (distancia_viagem *0.45)
    print('O valor sera de R${:.2f}'.format(valor))
else:
    valor2 = (distancia_viagem * 0.50)
    print('O valor sera de R${:.2f}'.format(valor2))
