dados = {}

dados['Nome'] = str(input('Digite um nome: '))
dados['Media'] = float(input(f'Digite a media de {dados["Nome"]}: '))

if dados['Media'] >= 7:
    dados['Situacao'] = 'Aprovado'
else:
    dados['Situacao'] = 'Reprovado'

for i, v in dados.items():
    print(f'{i} é igual a {v}.')        