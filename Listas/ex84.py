dado = list()
pessoa = list()
maior = menor = 0

while True:
    pessoa.append(str(input('Digite o nome: ')))
    pessoa.append(int(input('Digite o peso: ')))

    if len(dado) == 0:
        maior = menor = pessoa[1]
    else:
        if maior < pessoa[1]:
            maior = pessoa[1]
        if menor > pessoa[1]:
            menor = pessoa[1]

    dado.append(pessoa[:])
    pessoa.clear()
    
    op = str(input('Deseja continuar?(S/N): ')).upper().strip()

    if op in 'N':
        break

print('-='*30)
print(f"Pessoas cadastradas: {len(dado)}")       
print(f'O maior peso foi de {maior}Kg. Peso de ',end='')
for p in  dado:
    if p[1] == maior:
        print(f'[{p[0]}] ',end='')

print(f'\nO menor peso foi de {menor}Kg. Peso de ',end='')
for p in dado:
    if p[1] == menor:
        print(f'[{p[0]}] ',end='')  
