import random

escolhas = random.randint(1,3)

print('PEDRA!PAPEL!TESOURA!\nDigite:\n 1 - Pedra\n 2 - Papel\n 3 - Tesoura')
n = int(input('Digite a sua Escolha: '))
print('\n')
if n == 1 and escolhas == 2:
    print('Você escolheu: PEDRA\nO oponente escolheu: PAPEL')
    print('\nVOCÊ PERDEU!')
elif n == 2 and escolhas == 3:
    print('Você escolheu: PAPEL\nO oponente escolheu: TESOURA')
    print('\nVOCÊ PERDEU!')
elif n == 3 and escolhas == 1:
    print('Você escolheu: TESOURA\nO oponente escolheu: PEDRA')
    print('\nVOCÊ PERDEU!')

elif n == 2 and escolhas == 1: 
    print('Você escolheu: PAPEL\nO oponente escolheu: PEDRA')
    print('\nVOCÊ GANHOU!')
elif n == 1 and escolhas == 3:
    print('Você escolheu: PEDRA\nO oponente escolheu: TESOURA')
    print('\nVOCÊ GANHOU!')
elif n == 3 and escolhas == 2:
    print('Você escolheu: TESOURA\nO oponente escolheu: PAPEL')
    print('\nVOCÊ GANHOU!')

elif n == escolhas:
    if n == 1:
        print('Você escolheu: PEDRA\nO oponente escolheu: PEDRA')
    if n == 2:
        print('Você escolheu: PAPEL\nO oponente escolheu: PAPEL')
    if n == 3:
        print('Você escolheu: TESOURA\nO oponente escolheu: TESOURA')    
    print('\nVOCÊ EMPATOU!')
else:
    print('\nJogada invalida! Digite um numero entre 1 e 3!')
print('\n')

# Programa feito usando Strings 
'''a = ['PEDRA', 'PAPEL', 'TESOURA']
escolhas = random.choice(a)
b = str(input('PEDRA, PAPEL OU TESOURA!: '))

print(f'O computador escolheu: {escolhas}')

if b == 'PEDRA' and escolhas == 'PAPEL':
    print('\nVOCÊ PERDEU!')
elif b == 'TESOURA' and escolhas == 'PEDRA':
    print('\nVOCÊ PERDEU!')
elif b == 'PAPEL' and escolhas == 'TESOURA':
    print('\nVOCÊ PERDEU!')

elif b == 'PAPEL' and escolhas == 'PEDRA': 
    print('\nVOCÊ GANHOU!')
elif b == 'PEDRA' and escolhas == 'TESOURA':
    print('\nVOCÊ GANHOU!')
elif b == 'TESOURA' and escolhas == 'PAPEL':
    print('\nVOCÊ GANHOU!')

elif b == escolhas:
    print('\nVOCÊ EMPATOU!')

print('\n')'''