número = input('Digite um número para saber sua tabuada: ')
número = número.replace(',','.')
número = float(número)
for c in range(1,11):
    resultado = número * c
    print(f'{número} x {c} = {resultado}')
