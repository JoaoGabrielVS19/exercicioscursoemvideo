''' faze um programa que peça 3 numeros e mostre o maior e o menor'''

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

if n1 > n2 and n1 > n3:
    print('O número maior é {}'.format(n1))

if n2 > n1 and n2 > n3:
    print('O número maior é {}'.format(n2))

if n3 > n1 and n3 > n2:
    print('O númerp maior é {}'.format(n3))


if n1 < n2 and n1 < n3:
    print('O número menor é {}'.format(n1))

if n2 < n1 and n2 < n3:
    print('O número menor é {}'.format(n2))

if n3 < n1 and n3 < n2:
    print('O número menor é {}'.format(n3))