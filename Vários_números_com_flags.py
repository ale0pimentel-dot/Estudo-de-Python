num = soma = contador = 0
while True:
    num = int(input('Digite um número inteiro [999 para parar] : '))
    if num == 999:
        break
    contador = contador + 1
    soma = soma + num
print(f'A quantidade números digitados foi {contador} ')
print(f'A soma dos números foi {soma}')
print('FIM')
