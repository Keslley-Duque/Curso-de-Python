nome = str(input('Digite o seu nome completo: ')).strip().upper()

nome = nome.split()

print('\nPrimeiro nome: {}\nUltimo nome: {}'.format(nome[0],nome[len(nome)-1]))
