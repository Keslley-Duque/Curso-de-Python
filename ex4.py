#Teste 4

a = input('Digite uma palavra: ')
b = int(input('Digite um numero: '))
c = float(input('Digite um numero com virgula: '))
d = bool(input('Digite algo (ou não): '))


print('Palavra: ',a)
print('O tipo da variavel é: ',type(a))
print(a.isalpha())
print(a.isnumeric())
print(a.isidentifier())
print(a.isdecimal())
print('\nNumero inteiro: ',b)
print('\nO tipo da variavel é: ',type(b))
print('\nNumero com virgula: ',c)
print('\nO tipo da variavel é: ',type(c))
print('\nTem algo ou não: ', d)
print('\nO tipo da variavel é: ',type(d))
