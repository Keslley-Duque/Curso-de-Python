import random

a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o nome do segundo aluno: ')
c = input('Digite o nome do terceiro aluno: ')
d = input('Digite o nome do quarto aluno: ')

alu = [a, b, c, d]

escolhido = random.choice(alu)

print('\n{}'.format(escolhido))
