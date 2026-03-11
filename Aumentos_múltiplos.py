salário = float(input('Digite o salário atual do funcionário. R$:'))
if salário <= 1.250:
    a = salário * (15 / 100) + salário
    print(f'O novo salário é de R${a:.2f}, antes ganhava R${salário:.2f}')
else:
    b = salário * (10 / 100) + salário
    print(f'O novo salário é R${b}, antes ganhava R${salário:.2f}')