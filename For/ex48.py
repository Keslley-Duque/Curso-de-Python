s = 0
for i in range(1,501, 2):
    if i % 3 == 0:    
        s += i
print(f'A soma dos numeros que são impares e multiplos de três entre 1 e 500 é: {s}')    
