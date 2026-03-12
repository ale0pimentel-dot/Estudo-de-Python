sexo = str(input('Digite o seu sexo , [M/F]: ')).strip().upper()[0]#fatiamento(uso de [0] + tratando entrada
if sexo =='M' or sexo == 'F':
    print('Sexo registrado com sucesso! ')
while sexo not in 'MnFm':
    sexo = str(input('Valores inválidos.Por favor, informe seu sexo! [M/F]: ')).strip().upper()[0]
    if sexo == 'M' or sexo == 'F':
        print('Sexo registrado com sucesso!')
        break