from random import randint
from operator import itemgetter
jogador = {}

for i in range(1, 5):
    resultado = randint(1,6)
    jogador[f'Jogador {i}'] = resultado

print('Valores sorteados:')

for i, v in jogador.items():
    print(f'O {i} tirou {v}')    

print('\nRanking dos Jogadores:')
ranking = list()
ranking = sorted(jogador.items(), key= itemgetter(1), reverse= True)

for i , v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
