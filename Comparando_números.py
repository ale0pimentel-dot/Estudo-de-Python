n1 = input('Digite o primeiro número: ')

if ',' in n1 and '.' in n1:

    # assume padrão brasileiro

    n1 = n1.replace('.','').replace(',','.')


elif ',' in n1:

 # se tiver só ponto, assume que já está correto

    n1 = n1.replace(',','.')

n1 = float(n1)

n2 = input('Digite o segundo número: ')

if ',' in n2 and '.' in n2:

    # assume padrão brasileiro

    n2 = n2.replace('.','').replace(',','.')


elif ',' in n2:

# e tiver só ponto, assume que já está correto

    n2 = n2.replace(',','.')

n2 = float(n2)

print(f'O primeiro número é {n1}')
print(f'O segundo número é {n2}')
if n1 > n2:
    print('O PRIMEIRO VALOR é MAIOR')
elif n2 > n1:
    print('O SEGUNDO VALOR é MAIOR')
elif n1 == n2:
    print('OS DOIS VALORES SÃO IGUAIS')
else:
    print('TENTE NOVAMENTE!!!')