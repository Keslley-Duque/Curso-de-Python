num = [[],[]]
valor = 0

for i in range(1, 8):
    valor = int(input(f'Digite o {i}º numero: '))
    
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)       

num[0].sort()
num[1].sort()
print('-='*30)
print(f'Numeros pares: {num[0]}\nNumeros impares: {num[1]}')                