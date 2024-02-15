primeiro  = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
x = 1
ultimo = primeiro + (10 - 1) * r

print('||||||||||||||||')
for i in range(primeiro,ultimo + r,r):
    print('Termo ',x, '=' ,i)
    x+=1
