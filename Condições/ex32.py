from datetime import date

a = int(input('Digite um ano qualquer ou digite 0 para o ano atual: '))

if a == 0:
    a = date.today().year

if a%4 == 0 and a%100 != 0 or a%400 == 0:
    print(f'\nO ano {a} é bissexto!')
else:
    print(f'\nO ano {a} não é bissexto!')    