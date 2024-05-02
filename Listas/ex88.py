from time import sleep
from random import randint

num = list()
jogos = list()
tot = 1

print('-'*30)
print('      JOGA NA MEGA SENA')
print('-'*30)

op = int(input('Quantos jogos você quer que eu sorteie?: '))

while tot <= op:
    cont = 0
    while True:
        ale = randint(1,60)
        if ale not in num:
            num.append(ale)
            cont +=1
        if cont >= 6:
            break    
    num.sort()
    jogos.append(num[:])
    num.clear()
    tot+=1
    
print('-='*3,    f' SORTEANDO {op} JOGOS ', '-='*3)

for i, v in enumerate(jogos):
    print(f'JOGO {i+1}: {v}')
    sleep(1)

print('-='*5, '< BOA SORTE! >', '-='*5)