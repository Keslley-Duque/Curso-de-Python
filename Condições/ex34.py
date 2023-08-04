s = float(input('Qual é o valor do seu salário: '))

if s > 1250:
    s = (s * 1.1)
else:
    s = (s * 1.15)

print(f'\nO seu novo salário após o aumento é de: {s:.2f} Reais')        