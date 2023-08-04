d = float(input("Digite a distancia da viagem(em Kilometros): "))
#p = d * 0.5 if d <= 200 else d * 0.45
if d <= 200:
    p = (d * 0.5)
else:
    p = (d * 0.45)

print('\nValor da passagem: {} Reais'.format(p))        