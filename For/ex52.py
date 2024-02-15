n = int(input('Digite um numero: '))
i = 0

for x in range(1,n+1):
    if(n % x == 0):
        print('\033[33m',end='')
        i += 1
    else:
        print('\033[m',end='')
        
    print('{}'.format(x),end=' ')

if(i == 2):
    print('\033[m\n\nMuliplo apenas de 1 de dele mesmo!\nO numero é primo!')
else:
    print('\033[m\nPossui {} multiplos!\nO numero não é primo!'.format(i))            