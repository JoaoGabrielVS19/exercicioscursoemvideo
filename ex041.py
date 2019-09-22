try:
    idade = int(input("Informe uma Idade: "))
    if idade <= 9:
        print("Atleta Mirim")

    elif idade > 9 and idade <= 14:
        print("Atleta Infantil")

    elif idade > 14 and idade <=19:
        print("Atleta Junior")

    elif idade > 19 and idade <= 25:
        print("Atleta Sênior")

    else:
        print("Atleta Master")

except:
    print("Algo deu errado! tente novamento")