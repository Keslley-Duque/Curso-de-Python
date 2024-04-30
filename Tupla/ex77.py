palavras = ('Chocolate', 'Cachorro', 'Mesa', 'Computador', 'Livro', 'Caneta', 'Janela')

for p in palavras:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')
