terceiro = int(input('insira o terceiro termo de uma PG: '))
razao = int(input('insira a razao da PG: '))
n = int(input('insira o tamanho da PG: '))
while True:
    if n < 3:
        print('por favor, insira um numero maior que 3')
    else:
        break
for c in range(n)