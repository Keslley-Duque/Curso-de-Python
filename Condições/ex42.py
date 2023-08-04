r1 = float(input('\033[mDigite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))

if r1+r2 > r3 and r2+r3 > r1 and r3+r1 > r2:
    print('\n\033[1;32mÉ possivel fazer um triangulo com essas medidas!')

    if r1 == r2 and r2 == r3 and r1 == r3:
        print('\nO triangulo é Equilátero!')
    elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r2 == r3 and r1 != r3:
        print('\nO triangulo é Isósceles!')
    elif r1 != r2 and r2 != r3 and r3 != r1: 
        print('\nO triangulo é Escaleno!')
else:
    print('\n\033[1;31mNão é possivel fazer um triangulo com essas medidas!')    