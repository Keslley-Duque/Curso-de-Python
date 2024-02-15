primeiro = int(input('Qual o primeiro termo?: '))
r = int(input('Qual a razão da PA?: '))
x = 1
op = 10
total = 0 
while op != 0 :
    total += op
    while x <= total:
        print(f'Termo {x} = {primeiro}')
        primeiro += r
        x+=1
    op = int(input('Quantos termos você quer mostrar?:'))
   
print('FIM DO PROGRAMA...')