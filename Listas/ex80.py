lista = []
for i in range(0,5):
    num = int(input('Digite um numero: '))
    if i == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado no Final da lista!')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista!')
                break    
            pos += 1    

print(f'Lista Organizada: {lista}')