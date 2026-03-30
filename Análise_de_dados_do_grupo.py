contador_idade = contador_masculino = contador_feminino = 0
while True :
    idade = int(input('Informe sua idade: '))
    if idade > 18:
        contador_idade = contador_idade +1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe seu sexo: [M/F] : ')).strip().upper()[0]
        if sexo == 'M':
            contador_masculino = contador_masculino + 1
        if sexo == 'F' and idade < 20:
            contador_feminino = contador_feminino + 1

    decisão = ' '
    while decisão not in 'SN':
        decisão = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if decisão == 'N':
            print('Programa finalizado com sucesso!')
            print(f'Foram cadastrados {contador_idade} pessoas maiores de 18 anos')
            print(f'Foram cadastrados {contador_masculino} homens')
            print(f'Foram cadastrados {contador_feminino} mulheres com menos de 20 anos')
            break

    else:
        print('Vamos continuar...')

print('FIM DO PROGRAMA!!! Volte sempre!')