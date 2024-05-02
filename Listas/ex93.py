jogador = {}
numGols = []
totGols = 0

jogador['Nome'] = str(input('Nome do jogador: ')).upper()
partidas = int(input('Numero de partidas: '))

for i in range(0, partidas):
    gols = int(input(f'Numero de Gols na partida {i+1}: '))
    numGols.append(gols)
    jogador['Gols'] = numGols[:]
    totGols += gols

jogador['Total'] = totGols

print('-='*50)
print(jogador)
print('-='*50)

for i,v in jogador.items():
    print(f'O campo {i} tem o valor {v}.')
print('-='*50)

print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for i, v in enumerate(numGols):
    print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {totGols} gols.')
print('-='*50)