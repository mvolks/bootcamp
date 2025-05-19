pmr = int(input('insira o primeiro termo de uma PA: '))
razao = int(input('insira a razao da PA: '))
n = int(input('insira o tamanho da PA: '))
for c in range (n):
    termo = pmr + c * razao
    print(f'{termo}')