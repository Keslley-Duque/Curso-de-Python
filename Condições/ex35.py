r1 = float(input('\033[mDigite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))

if r1+r2 > r3 and r2+r3 > r1 and r3+r1 > r2:
    print('\n\033[1;32mÉ possivel fazer um triangulo com essas medidas!')
else:
    print('\n\033[1;31mNão é possivel fazer um triangulo com essas medidas!')    