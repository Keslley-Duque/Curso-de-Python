p = float(input('Digite o seu peso (em kg): '))
a = float(input('Digite a sua altura (em centimetros): '))

imc = p /((a / 100) * (a / 100))

if imc <= 18.5:
    print(f'\nO seu IMC é: {imc:.2f}\nVocê está abaixo do peso!')
elif imc <= 25:
    print(f'\nO seu IMC é: {imc:.2f}\nVocê está com o peso ideal!')
elif imc <= 30:
    print(f'\nO seu IMC é: {imc:.2f}\nVocê está com sobrepeso!')
elif imc <= 40:
    print(f'\nO seu IMC é: {imc:.2f}\nVocê está com Obesidade!')
else:
    print(f'\nO seu IMC é: {imc:.2f}\nVocê está com Obesidade Morbida!')                