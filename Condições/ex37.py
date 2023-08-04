n = int(input('Digite o numero a ser convertido: '))
print('Qual vai ser a base de conversão?\n 1 - Binário\n 2 - Octal\n 3 - Hexadecimal')
o = int(input('Digite a sua opção: '))

if o == 1:
    print(f'\nO numero {n} foi convertido em Binário!\nValor: {bin(n)[2:]}')    
elif o == 2:
    print(f'\nO numero {n} foi convertido em Octal!\nValor: {oct(n)[2:]}')    
elif o  == 3:
    print(f'\nO numero {n} foi convertido em Hexadecimal!\nValor: {hex(n)[2:]}')    
else:
    print('\nComando invalido!')
