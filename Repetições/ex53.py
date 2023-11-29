frase = str(input('Digite uma frase para verificar: ')).strip().upper()
f = frase.replace(' ','')

t = len(f)
''' 
inverso = ''
inverso = [::-1]  
'''
if t == 0:
    x = False   
else:
    for i in range(t-1, -1, -1):
        '''inverso += f'''
        if f[i] != f[t - i - 1]:
            x = False
        else:
            x = True

print('A frase invertida é =',f) 

if x == False:
    print('Não é um palindromo!') 
else:       
    print('Essa palavra é um palindromo!')