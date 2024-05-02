lista = []
cont = 0
while True:
    num = int(input('Digite um numero: '))
    lista.append(num)

    cont+=1

    op = str(input('\nDeseja continuar?(S/N): ')).upper().strip()

    if op in 'N':
        break

lista.sort(reverse= True)

print(f'\nForam digitados {cont} numeros.')
print(f'Valores da lista: {lista}')

if 5 in  lista:
    print(f'O valor 5 foi digitado {lista.count(5)} vez(es) e está na posição: ', end='')

    for p , v in enumerate(lista):
        if v == 5:
            print(f'[{p}]', end=' ')

else:
    print('O numero 5 não foi digitado!')    