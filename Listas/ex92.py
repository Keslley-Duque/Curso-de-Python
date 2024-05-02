from datetime import date

dados = {}

dados['Nome'] = str(input('Digite o nome: ')).upper().strip()
ano = int(input('Digite o ano de nascimento: '))
dados['idade'] = date.today().year - ano
dados['Carteira de Trabalho'] = int(input('Digite o numero da carteira de trabalho (0 se não tiver): '))

if dados['Carteira de Trabalho'] != 0:
    dados['Ano de contratação'] = int(input('Digite o ano de contratação: '))
    dados['Salario'] = float(input('Digite o salario(R$): '))
    dados['Aposentadoria'] = 35 - (date.today().year - dados['Ano de contratação']) + dados['idade']
else:
    dados['Carteira de Trabalho'] = 'Não possui!'    

print('-='*60)
print(dados)

for i, v in dados.items():
    print(f'{i} tem o valor {v}.')