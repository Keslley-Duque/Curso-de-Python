import math

ang = float(input('Digite um angulo a se calcular: '))

seno = math.sin(math.radians(ang))
cose = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('\nO Seno do numero {:.0f} é: {:.2f}, o Cosseno é: {:.2f} e a Tangente é: {:.2f}'.format(ang,seno,cose,tan))