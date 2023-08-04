import random

km = random.randint(65,120)

if km > 80:
    multa = 7 * (km - 80)
    print('\nLimite de Velocidade: 80 Km/h\nVelocidade: {} Km/h'.format(km))
    print('\nVocê ultrapassou o limite de velocidade, você será multado!')
    print('\nMulta de {} Reais!'.format(multa))

else:
    print('\nLimite de Velocidade: 80 Km/h\nVelocidade: {} Km/h'.format(km))
    print('\nVocê está dentro do limite de velocidade.')