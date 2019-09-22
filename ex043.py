peso = float(input("Qual seu peso? (Kg) "))
altura = float(input("Qual sua altura? "))

calc = altura * altura
calc2 = peso / calc

print("Seu IMC é {:.2f}".format(calc2))
if calc2 <= 18.5:
    print("Você esta ABAIXO do peso!")

elif calc2 > 18.5 and calc2 <= 25:
    print("Você esta com peso IDEAL!!")

elif calc2 > 25 and calc2 < 30:
    print("Você esta com SOBREPESO!!")

elif calc2 > 30 and calc2 < 40:
    print("Você esta com OBSIDADE!!")

else:
    print("Você esta com OBESIDADE MÓRBIDA!!")