num = int(input('Digite um numero de 0 a 9999: '))

print('\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(num // 1 % 10 ,num // 10 % 10 ,
     num // 100 % 10, num // 1000 % 10))


#Vesão do codigo usando a variavel como string sem laço de repetição (não funciona com numeros abaixo de 1000)
#numero = str(input('Digite um numero de 0 a 9999: '))

#numero = numero.casefold()

#print('\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(numero[3], numero[2],numero[1], numero[0]))
