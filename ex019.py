import random

aluno1 = str(input('Primeiro Aluno: '))
aluno2 = str(input('Segundo Aluno: '))
aluno3 = str(input('Terceiro Aluno: '))
aluno4 = str(input('Quarto Aluno: '))

lista_alunos = [aluno1, aluno2, aluno3, aluno4]

escolhido = random.choice(lista_alunos)

print('O aluno escolhido foi {}'.format(escolhido))
