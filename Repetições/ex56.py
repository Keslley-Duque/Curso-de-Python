
soma = 0
media = 0
mulher20 = 0
velho = 0
nomevelho = ''

for x in range(1, 5):
    print(f'\n-----{x}ª Pessoa-----')
    nome = str(input('Digite o nome: ')).upper()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo (F ou M): ')).upper()
    
    soma += idade

    if x == 1 and sexo == 'M':
        velho = idade
        nomevelho = nome

    if sexo == 'M' and idade > velho:
        velho = idade
        nomevelho = nome 

    if sexo == 'F' and idade < 20:
        mulher20 += 1

media =  soma/x

print(f'\nA media da idade do grupo é {media} anos!')
print(f'O homem mais velho tem {velho} anos e se chama {nomevelho}!')
print(f'Existe(m) {mulher20} mulher(es) que possui(em) menos de 20 anos!')