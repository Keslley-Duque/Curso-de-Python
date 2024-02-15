primeiro = int(input('Qual o primeiro termo?: '))
r = int(input('Qual a razão da PA?: '))
x = 1

while x != 11 :
    print(f'Termo {x} = {primeiro}')
    primeiro += r
    x+=1