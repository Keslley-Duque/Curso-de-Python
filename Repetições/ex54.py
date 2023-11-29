from datetime import date
y = date.today().year
maior = 0
menor = 0

for x in range(1,8):
    ano = int(input(f'Em que ano a {x}ª pessoa nasceu?: '))
    idade = (y - ano)

    if idade < 18:
        menor += 1
    else:
        maior += 1

print(f'Existem {maior} pessoas maiores de idade!')
print(f'Existem {menor} pessoas que ainda não atingiu a maioridade!')
