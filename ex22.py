
nome = input('Digite o nome completo: ')

print('\nVersão do nome todo maiusculo: {}'.format(nome.upper()))
print('\nVersão do nome todo minusculo: {}'.format(nome.lower()))
print('\nQuantidade de letras sem espaço: {}'.format(len(nome.strip()) - nome.count(' ')))
nome = nome.split()
print('\nQuantidade de letras: {}'.format(len(nome[0])))
