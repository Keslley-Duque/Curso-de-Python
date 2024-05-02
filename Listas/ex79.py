lista = []

while True:
    num = int(input('Digite um numero: '))

    if num not in lista:
        lista.append(num)
        print('\nValor adcionado!')
    else:
        print('\nO numero digitado ja está na lista!\nValor não adicionado!')

    op = str(input('\nDeseja continuar? (S/N): ')).upper().strip()
    if op in 'N':
        break   

lista.sort()
print(f'\nLista de numeros: {lista}')
