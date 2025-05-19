pmr = int(input('insira o primeiro termo de uma PG: '))
razao = int(input('insira a razao da PG: '))
n = int(input('insira o tamanho da PG: '))
for c in range(n):
    rz = razao**(c-1)
    termos = pmr * rz
    print(f'{termos}')