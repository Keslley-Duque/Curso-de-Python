produtos = ('RX 580', 500, 'RX 6650 XT', 1399, 'GTX 1050 Ti', 1000, 'RTX 3050', 1500, 'RXT 4060', 2000,
        'Ryzen 5 3500', 400, 'Ryzen 5 5500', 600, 'Intel Core I5 7600K', 760, 'Intel Core I9 12600K', 1600)
print('-='*30)
print('----------Lista de Produtos----------')
print('-='*30)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}R$ ',end='')
    else:
        print(f'{produtos[pos]:.2f}')    
print('-='*30)
#nt(f' x ' if c > 1 else ' = ',end='')
