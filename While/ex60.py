n = int(input('Digite um numero para descobrir o seu fatorial:'))
f = 1
c = n
while c > 0:
    print(f'{c}',end='')
    print(f' x ' if c > 1 else ' = ',end='')
    f *=   c
    c -= 1
    
print(f'{f}')    