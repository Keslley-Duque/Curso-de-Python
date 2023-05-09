nome = str(input('Digite o seu nome: ')).strip()
nome = nome.upper()
print('\nNome: {}\nTem Silva?: {}'.format(nome, 'SILVA' in nome))