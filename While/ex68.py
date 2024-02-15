from random import randint
soma = cont = 0
while True:
    op = int(input('Escolha um numero: '))
    comp = randint(0,10)

    tipo = ''
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar![P/I]: ')).strip().upper()[0]

    soma = op + comp

    if soma % 2 == 0 and tipo == 'P':
        print(f'\nVocê jogou {op} e o computador jogou {comp}. O resultado deu {soma} DEU PAR.')
        print('Você colocou PAR!\nVocê ganhou!')
        cont += 1
    elif soma % 2 == 0 and tipo == 'I':
        print(f'\nVocê jogou {op} e o computador jogou {comp}. O resultado deu {soma} DEU PAR.')
        print('Você colocou IMPAR!\nVocê perdeu!')
        break
    elif soma % 2 == 1 and tipo == 'I':
        print(f'\nVocê jogou {op} e o computador jogou {comp}. O resultado deu {soma} DEU IMPAR.')
        print('Você colocou IMPAR!\nVocê ganhou!')
        cont += 1  
    elif soma % 2 == 1 and tipo == 'P':
        print(f'\nVocê jogou {op} e o computador jogou {comp}. O resultado deu {soma} DEU IMPAR.')
        print('Você colocou PAR!\nVocê perdeu!')
        break

print(f'\nGAME OVER! Você venceu {cont} vezes.')
