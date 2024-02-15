num = int(input('Digite um numero inteiro: '))
media = op  = soma = cont = 0
menor = maior = num

while op != 2:
    if maior < num:
        maior = num
    elif menor > num:
        menor = num
    soma += num
    cont += 1        
    op = int(input('\nDigite [1] para continuar\nDigite [2] para sair: '))
    if op == 1:
        num = int(input('\nDigite um numero inteiro: '))
   
media = soma/cont

print(f'\nVocê digitou {cont} numeros e a media deles é = {media}\nO maior valor é = {maior}\nO menor valor é = {menor}')