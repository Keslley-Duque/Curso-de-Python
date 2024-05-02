lista = []
expr = str(input('Digite uma expressão que use parenteses: '))
for simb in expr:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break        

if len(lista) == 0:
    print('Sua expressão está correta!')
else:
    print(f'Sua expressão está errada!')    