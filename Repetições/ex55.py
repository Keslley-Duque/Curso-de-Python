maior = 0
menor = 0
for x in range(1, 6):
    peso = float(input(f'Digite o peso da {x}ª pessoa: '))
    if x == 1:
        maior = peso
        menor = peso
    else:    
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso    

print(f'Maior peso: {maior}Kg')
print(f'Menor peso: {menor}Kg')