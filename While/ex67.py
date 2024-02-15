while True:
    num = int(input('Digite um numero para fazer uma tabuada: '))
    if num < 0:
        break
    print('-'*30)
    print(f'Tabuada do {num}')
    print('-'*30)

    for c in range(1,11):
        print(f'{num} x {c} = {num*c}')

    print('-'*30) 
print('PROGRAMA DE TABUADA ENCERRADO. VOLTE SEMPRE!')       