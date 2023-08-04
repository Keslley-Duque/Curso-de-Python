from datetime import date

ano = int(input('Digite o ano em que nasceu: '))

d = date.today().year

idade = d - ano

if idade < 18:  
    print(f'\nVocê tem {idade} anos em {d} e ainda vai ter que esperar {18 - idade} anos para se alistar!')
    print(f'\nSeu alistamento será feito em {d + (18 - idade)}')
elif idade == 18:
    print(f'\nVocê ja tem {idade} anos em {d} e deve se alistar! Vá a uma junta militar o quanto antes!')
elif idade > 18:
    print(f'\nVocê tem {idade} anos em {d} e passou {idade - 18} anos do tempo para se alistar!\nO seu alistamento foi em {d - (idade - 18)}!')
