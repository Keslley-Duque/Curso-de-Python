matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
spar = scol = maior = 0

for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l+1}:{c+1}]: '))
        
print('-='*20)

for l in range(0,3):
    for c in range(0,3):

        print(f'[{matriz[l][c]:^5}]',end='')

        if matriz[l][c]%2 == 0:
            spar += matriz[l][c]

        if c == 2:    
            scol += matriz[l][c]

        if l == 1:
            if maior < matriz[l][c]:
                maior = matriz[l][c]
                      
    print()    
print('-='*20) 

print(f'A soma dos valores pares: {spar}')
print(f'A soma dos valores da terceira coluna: {scol}')
print(f'O maior valor da segunda linha: {maior}')
print('-='*20)
