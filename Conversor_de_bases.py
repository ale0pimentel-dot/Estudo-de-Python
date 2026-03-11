num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] CONVERTER PARA BINÁRIO
[ 2 ] CONVERTER PARA PARA OCTAL
[ 3 ] CONVERTER PARA HEXADECIMAL''')
opção = int(input('Escolha sua opção : '))
if opção == 1:
    print(f'{num} convertido para binário é {bin(num)[2:]}')
elif opção == 2:
    print(f'{num} convertido para octal é {oct(num)[2:]}')
elif opção == 3:
    print(f'{num} convertido para hrxadecimal é {hex(num)[2:]}')
else:
    print('OPÇÃO INVÁLIDA!!! TENTE NOVAMNTE!!!')