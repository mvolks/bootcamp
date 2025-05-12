
n1 = int(input('insira um numero inteiro  para ser a base: '))
n2 = int(input('insira um segundo numero inteiro positivo para ser o expoente: '))
if base <= 0 or expoente <= 0:
    print("Por favor, digite apenas números inteiros positivos.")
else:
    contador = 0
    resultado = 1
    while contador < n2 :
        resultado = resultado * n1
        contador = contador + 1
print(f'{n1} elevado a {n2} = {resultado}')