import random

num = random.randint(0,10)
acerto = 0
tentativas = 1

while acerto == 0:    
    ad = int(input('Tente advinhar um numero de 0 a 10: '))
    if ad == num:
        print('\nParabens você acertou!!!')
        acerto += 1
    else:
        print('\nQue pena você errou. :(')
        tentativas += 1
        if ad > num:
            print('Menor...Tente novamente!')
        if ad < num:
            print('Maior...Tente novamente!')    

print(f'\nO numero é: {num}')
print(f'Você tentou {tentativas} vezes!')