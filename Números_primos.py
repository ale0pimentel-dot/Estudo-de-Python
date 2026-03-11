num = int(input('Digite um número: '))
tot = 0
for c in range(1,num +1):
    if num % c == 0:
        print('\033[34m', end=' ')
        tot = tot +1

    else:
        print('\033[m', end=' ')
    print(f'{c}' , end=' ')
print(f'\n O número {num} foi divisível {tot} vezes')
if tot == 2:
    print(f'O {num} é primo')
else:
    print(f'O {num} não é primo')