alunos = list()

while True:
    nome = str(input('Nome do Aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    media = (nota1 + nota2) / 2
    
    alunos.append([nome, [nota1, nota2], media])

    op = str(input('Deseja continuar?(S/N): ')).upper().strip()

    if 'N' in op:
        break

print('-='*30)
print('Nº.  NOME          MÉDIA')
print('-'*30)

for i, v in enumerate(alunos):
    print(f'{i}   {v[0]:^9}      {v[2]:^.1f}')

while True:
    print('-'*30)
    op2 = int(input('Mostrar notas de qual aluno?(999 para sair): '))
    
    if op2 >= len(alunos):
        print('\nDigite um aluno cadastrado!')

    elif op2 <= len(alunos) - 1:
        print(f'\nNotas de {alunos[op2][0]} são: {alunos[op2][1]}')

    elif op2 == 999:
        print('\nFinalizando...')
        break    
   