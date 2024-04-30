numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito',
'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
'dezoito', 'dezenove', 'vinte')

n = int(input('Digite um numero entre 0 e 20: '))
while True:
    if n >= 0 and n <= 20:
        print(f'\nVoce digitou o numero {numeros[n]}')

        op = str(input('\nVoçê quer continuar?(S/N): ')).upper().strip()

        if op != 'S':
            break
        
        n = int(input('\nDigite um numero entre 0 e 20: '))
    else:    
        n = int(input('\nTente novamente. Digite um numero entre 0 e 20: '))
    
print('\nSaindo...')

