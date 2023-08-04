v = float(input('Digite o valor da casa: '))
s = float(input('Digite o seu sálario: '))
a = int(input('Em quantos anos você quer pagar?: '))

p = v / (a * 12)

if p > s*0.3:
    print(f'\n\033[1;31mValor da prestação mensal: {p:.2f} Reais\nNão podemos realizar o emprestimo!\033[m')
else:
    print(f'\033[1;32m\nValor da prestação mensal: {p:.2f} Reais\nEmprestimo realizado com sucesso!\033[m')    
