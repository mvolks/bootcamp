pmr = int(input('insira o primeiro termo de uma PA: '))
razao = int(input('insira a razao da PA: '))
while True:
    n = int(input('insira o tamanho da PA(maior que 3): '))
    if n < 3:
        print('por favor, insira um numero maior que 3')
    else:
        break
for c in range (n):
    termo = pmr + c * razao
    print(f'{termo}')