quarto = int(input('insira o qaurto termo de uma PA: '))
razao = int(input('insira a razao da PA: '))
n = int(input('insira o tamanho da PA: '))
ultimo = quarto + n * razao
soma=(quarto + ultimo)*n % 2
print(f'{soma}')