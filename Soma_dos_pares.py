soma = 0
count = 0
for c in range(1,7):
    num = int(input(f'Digite {c} valor inteiro: '))
    if num % 2 == 0:
        soma = soma + num
        count = count +1
print(f'A soma dos {count} números pares é : {soma}')
