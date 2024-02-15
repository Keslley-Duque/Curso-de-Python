
s = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]

while s not in 'MF':
    s = str(input('Dados invalidos! Digite o seu sexo: ')).strip().upper()[0]
    
print(f'Sexo {s} registrado com sucesso!')
