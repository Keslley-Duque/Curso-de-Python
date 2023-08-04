nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2

if media < 5:
    print(f'\nVocê foi REPROVADO! A sua média é: {media:.1f}')
elif media >= 5 and media < 7:
    print(f'\nVocê está de RECUPERAÇÃO! A sua média é: {media:.1f}')
elif media >= 7:
    print(f'\nVocê foi APROVADO! A sua média é: {media:.1f}')        