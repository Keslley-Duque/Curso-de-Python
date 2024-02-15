import pygame
print('Iniciando o Menu....')
v1 = int(input('Digite o primeiro valor:'))
v2 = int(input('Digite o segundo valor:'))

op = 0
while op != 5:
    
    print('''
    Digite [1] para somar
    Digite [2] para multiplicar
    Digite [3] para maior
    Digite [4] para novos numeros
    Digite [5] para sair''')
    op = int(input('\nDigite a opção desejada:'))
    
    if op == 1:
       soma = v1 + v2
       print(f'\n{v1} + {v2} é = {soma}')
       pygame.time.wait(1500)
    elif op == 2:
        mult = v1 * v2
        print(f'\n{v1} X {v2} é = {mult}')
        pygame.time.wait(1500)
    elif op == 3:
        if v2 > v1:
            maior = v2
        elif v1 > v2:
            maior = v1    
        print(f'\nO maior numero entre {v1} e {v2} = {maior}')
        pygame.time.wait(1500)    
    elif op == 4:
        print('\nInforme os valores novamente:')
        v1 = int(input('\nDigite o novo primeiro valor:'))
        v2 = int(input('Digite o novo segundo valor:'))
        print(f'\nOs numeros foram alterados = {v1} e {v2}')
        pygame.time.wait(1500)
    elif op == 5:
        print('Saindo...')
    else:
        print('Opção invalida....')
        pygame.time.wait(1000)

