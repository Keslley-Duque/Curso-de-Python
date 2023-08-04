import random

num = random.randint(0,5)

ad = int(input('Tente advinhar um numero de 0 a 5: '))

if ad==num:
    print('\nParabens você acertou!!!')
else:
    print('\nQue pena você errou. :(')
    
print('\nO numero é: ',num)