import math

catop = float(input('Digite o comprimento do cateto oposto: '))

catad = float(input('Digite o comprimento do cateto adjacente: '))

hipo = math.hypot(catop,catad)

print("\nA hipotenusa é: {:.2f}".format(hipo))
