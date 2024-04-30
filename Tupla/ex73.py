times = ('Corinthians', 'Atlético-GO', 'Atlético-MG', 'Bahia', 'Botafogo', 'Bragantino',
'Athletico', 'Criciúma', 'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio',
'Internacional', 'Juventude', 'Vitória', 'São Paulo', 'Vasco', 'Palmeiras')

print('Brasileirão Séria A')
print('-='*10)

print(f'Os cinco primeiros colocados são: {times[0:5]}')
print('-='*50)

print(f'Os ultimos quatro colocados são: {times[-4:]}')
print('-='*40)

print(f'Lista dos times em ordem alfabetica: {sorted(times)}')
print('-='*30)

print(f'O time do Corinthians está na {times.index("Corinthians")+1}ª posição.')
print('-='*20)