num1 = input('Digite o primeiro valor: ')
num1 = num1.replace(',', '.')
num1 = float(num1)

num2 = input('Digite o segundo valor: ')
num2 = num2.replace(',', '.')
num2 = float(num2)

opção = 0

while opção != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA''')

    opção = int(input('Qual é a sua opção? : '))

    if opção == 1:
        soma = num1 + num2
        print(f'A soma entre {num1} + {num2} é igual a {soma}')

    elif opção == 2:
        multiplicação = num1 * num2
        print(f'A multiplicação entre {num1} x {num2} é igual a {multiplicação}')

    elif opção == 3:
        if num1 > num2:
            maior = num1
            print(f'O maior é {maior}')

        else:
            maior = num2
            print(f'O maior é {maior}')

    elif opção == 4:
        print('Informe os números novamente')
        num1 = input('Digite o primeiro valor: ')
        num1 = num1.replace(',', '.')
        num1 = float(num1)

        num2 = input('Digite o segundo valor: ')
        num2 = num2.replace(',', '.')
        num2 = float(num2)

    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção invalida!')
    print('=-=' * 10)
print('Fim do programa!')