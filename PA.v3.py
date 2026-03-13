primeiro = int(input('Digite o primeiro termo da Pa: ')) # peço o primeiro termo
razão = int(input('Digite o valor da razão da Pa: ')) # peço a razão
termo = primeiro # termos da PA
contador = 0 # contador acumulativo, vai contar os termos
mais = 10
total = 0
while mais != 0:
    total= total + mais
    while contador <= total: # enquanto 'mais' diferente de zero
        print(f'{termo} -> ', end='') # termo sem acumulador -> acumulador -> contador = 0
        termo = termo + razão
        contador = contador + 1
    print('Pausa')
    mais = int(input('Quantos termos vocé quer a mais ? : '))
print(f'Progressão finalizada com {total} termos registrados')
