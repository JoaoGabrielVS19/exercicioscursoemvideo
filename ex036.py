casa = float(input("Valor casa: R$"))
salario = float(input("Salario Mensal: R$"))
anos = int(input("Parcelado em Qnts Anos: "))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

if prestacao <= minimo:
    print("Aprovado")
else:
    print("Negado")
