n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))
media = (n1 + n2 + n3)

print("O aluno que tirou {} no primeiro, {} no segundo, {} no terceiro trimestre tem a média anual de {}"
      .format(n1, n2, n3, media))

if media > 180:
    print("Aluno(a) APROVADO!")

else:
    print("Aluno(a) REPROVADO!")
