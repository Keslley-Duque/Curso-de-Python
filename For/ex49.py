
n = int(input('Digite um numero para fazer uma tabuada:'))
print(f'\nA tabuada do numero {n}')
for i in range(0, 11):
    t = n * i
    print(f'{n} x {i}  = {t}')
