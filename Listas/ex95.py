jogador = {}
dados = []
numGols = []

while True:
    jogador['Nome'] = str(input('Nome do jogador: ')).upper()
    partidas = int(input('Numero de partidas: '))
    
    for i in range(0, partidas):
        numGols.append(int(input(f'Numero de Gols na partida {i+1}: ')))

    jogador['Gols'] = numGols[:]
    jogador['Total'] = sum(numGols)

    dados.append(jogador.copy())

    jogador.clear()
    numGols.clear()

    while True:
        op = str(input('Deseja cadastrar outro jogador?(S/N): ')).upper()
        if op in 'SN':
            break
        print('Erro! Digite S ou N!')
    if op == 'N':
        break    

print('-='*40)
print('Cod Nome            Gols          Total')
print('-'*80)

for k , v in enumerate(dados):
    print(f'{k:>2} ',end='')
    for i in v.values():
        print(f' {str(i):<15}',end='')
    print()
print('-='*40)

while True:
    op = int(input('Mostrar dados de qual jogador?(999 para sair): '))
    
    if op >= len(dados):
        print(f'ERRO! Não existe jogador com codigo {op}!')
        print('-'*80)
    else:        
        print(f'Dados do jogador {dados[op]["Nome"]}.')
        for i, v in enumerate(dados[op]["Gols"]):
            print(f'    => Na partida {i+1}, fez {v} gols.')
        print('-='*40)

    if op == 999:
        break

print('<<< Volte Sempre >>>')
