f = str(input('Digite uma frase: ')).strip().upper()

print('\nQuantidade de "A" na frase: {}\nAparece na posição {} pela primeira vez!'
      .format(f.count('A', ), f.find('A', ) + 1))
print('\nAparece na posição {} pela ultima vez!'.format(f.rfind('A',) + 1))
