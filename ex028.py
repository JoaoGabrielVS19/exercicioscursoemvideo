import random

pensa = [0, 1, 2, 3, 4, 5]
escolhacpu = random.choice(pensa)

palpite = int(input('Tente descobrir o número pensado pela CPU de 0 a 5: '))

if palpite == escolhacpu:
    print('Você acertou! GANHOU')

else:
    print('Você errou! PERDEU')
    print('O número pensado é {}'.format(escolhacpu))
