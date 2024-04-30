numeros = (int(input('Primeiro numero: '))
        ,int(input('Segundo numero: '))
        ,int(input('Terceiro numero: '))
        ,int(input('Quarto numero: ')))

print('-='*40)
print(f'Você digitou os valores {numeros}')
print('-='*40)
print(f'O valor nove apareceu {numeros.count(9)} vezes!')
print('-='*40)

if 3 not in numeros:
    print(f'O valor três não foi digitado nenhuma posição!')
else:    
    print(f'O valor três apareceu na {numeros.index(3)+1}ª posição')

print('-='*40)
print('O numeros pares foram: ', end= '')
for n in numeros:
    if n %2 == 0:
        print(n, end=' ')
