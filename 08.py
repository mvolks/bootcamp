fib = int(input('insira até onde a sequencia de febonacci deve ir: '))
n1 = 0
n2 = 1
n3 = n2 + n1
print('A sequência ficaria: 1', end=' ')
for c in range(0, fib - 1):
    print(f'{n3}', end=' ')
    n1 = n2
    n2 = n3
    n3 = n2 + n1