s = 0
for i in range(0,6):
    n = int(input('Digite um numero a ser somado: '))
    if n % 2 == 0:
        s += n
print(f'A soma dos numeros pares: {s}')            