from datetime import date

atual = date.today().year


idade = int(input("Quantos anos você tem? "))
nasc = atual - idade
print("Você nasceu em {}, tem {}anos".format(nasc, idade))
if idade == 18:
    print("Deve se alistar IMEDIATAMENTE!")

elif idade < 18:
    ano_alistar = 18 - idade
    print("Ainda falta {} anos para você se alistar".format(ano_alistar))

else:
    ano_alistado = idade - 18
    print("Você deveria ter se alistado a {} ano atraz".format(ano_alistado))




