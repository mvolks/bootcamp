while True:
    num = int(input('insira um numero inteiro positivo: '))
    if num < 0:
        print('por favor, insira um numero positivo')
    else:
        num2 = int(input('insira outro numero inteiro positivo: '))
        break
//mdc
num3 = num
num4 = num2
if num3 == num4:
    print(f'o mdc é = {num3}')
elif num3 < num4:
    num3 = num4
    temp = num4
    num4 = num3
rest = num3 % num4
while rest !=0:
    num3 = num4
    num4 = rest
    rest = num3 % num4
//mdc
if num > num2:
    maior = num
else:
    maior = num2
while True:
    if maior% num == 0 and maior % num2 == 0:
        mmc = maior
        break
    maior += 1
print(f'o mmc é {mmc} e o mdc é {num4}') 