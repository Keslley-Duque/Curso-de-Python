n = int(input('Digite um numero inteiro [Digite 999 para Parar]: '))
cont = soma = 0
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um numero inteiro [Digite 999 para Parar]: '))

print(f'Numeros digitados = {cont}\nSoma dos numeros digitados = {soma}')
