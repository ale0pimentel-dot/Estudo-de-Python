num = input('Digite um número para tabuada: ')
num = num.replace(',','.')
num = float(num)
for c in range(1,11):
    print(f'{num} x {c} = {num * c}')