num = list()
impar = []
par = []

while True:
    num.append(int(input('Digite um numero: '))) 

    op = str(input('Deseja continuar?(S/N): ')).upper().strip()

    if op in 'N':
        break
    
for i, c in enumerate(num):
    if c %2== 0:
       par.append(c)   
    else:
       impar.append(c)
        
print(f'\nValores digitados: {num}')
print(f'Numeros Pares: {par}')  
print(f'Numeros Impares: {impar}')    