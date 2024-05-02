pessoas = {}
dados = []
soma = media = 0

while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Nome: ')).upper()

    while True:
        pessoas['Sexo'] = str(input('Sexo (M/F): ')).upper()
        if pessoas['Sexo'] in 'MF':
            break
        print('Erro! Por favor digite apenas F ou M.')    

    pessoas['Idade'] = int(input('Idade: '))
    soma += pessoas['Idade']
    dados.append(pessoas.copy())
    while True:
        op = str(input('Quer continuar?(S/N): ')).upper()
        if op in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if op == 'N':
        break

print('-='*50)
print(f'- O grupo tem {len(dados)} pessoas.')

media = soma/len(dados)
print(f'- A média de idade é de {media:.2f} anos.')    

print(f'- As mulheres cadastradas foram: ',end= '')
for p in dados:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]}', end= '| ' )

print()
print('- Lista das pessoas que estão acima da média de idade: ')
for i in dados:
    if i['Idade'] > media:
        print('     ',end='')
        for k, v in i.items():
            print(f'{k} = {v}; ', end='')
        print()

print('<<< Encerrado >>>')
                      