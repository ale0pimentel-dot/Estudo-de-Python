soma = 0
count = 0
for c in range(3,501,3):
    if c % 3 == 0 and c % 2 != 0:
        soma = soma + c
        count = count + 1
print(f'A soma de todos os {count} valores solicitados é {soma}')