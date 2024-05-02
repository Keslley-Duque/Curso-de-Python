lista = []
for i in range(0,5):
    num = int(input(f'Digite um numero na posição {i}: '))
    lista.append(num)

maior = max(lista)
menor = min(lista)

print(f'\nLista de numeros {lista}') 
print(f'O maior numero digitado foi {maior} nas posições: ', end='')
for p , v in enumerate(lista):
    if v == maior:
        print(f'[{p}]',end=' ')

print(f'\nO menor numero digitado foi {menor} nas posições: ', end='') 
for p , v in enumerate(lista):
    if v == menor:
        print(f'[{p}]', end=' ')   
