a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))

maior = a

if b > a:
    maior = b
if c > a:
    maior = c         
    
menor = a
    
if b < a:
    menor = b
if c < a:
     menor = c

print(f'\nO numero {maior} é o maior!')
print(f'\nO numero {menor} é o menor!')