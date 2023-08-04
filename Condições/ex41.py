from datetime import date

d = int(input('Digite o ano que você nasceu: '))

ano = date.today().year - d

print(f'\nVocê tem {ano} anos de idade!')

if ano <= 9:
    print('\nSua categoria é: MIRIM!')
elif ano <= 14:
    print('\nSua categoria é: INFANTIL!')
elif ano <= 17:
    print('\nSua categoria é: JUNIOR!')
elif ano <= 20:
    print('\nSua categoria é: SÊNIOR!')
else:
    print('\nSua categoria é: MASTER!')
