lado_1 = input('Digite o primeiro lado do triângulo: ')
lado_1 = lado_1.replace(',','.')
lado_1 = float(lado_1)

lado_2 = input('Digite o segundo lado do triângulo: ')
lado_2 = lado_2.replace(',','.')
lado_2 = float(lado_2)

lado_3 = input('Digite o terceiro lado do triângulo: ')
lado_3 = lado_3.replace(',','.')
lado_3 = float(lado_3)

if lado_1 <= 0 or lado_2 <= 0 or lado_3 <= 0:
    print('VALORES INVÁLIDOS')

elif lado_1 < lado_2 + lado_3 and lado_2 <  lado_3 + lado_1 and lado_3 <  lado_2 + lado_1:
    print('O triãngulo é POSSÍVEL')
    if lado_1 == lado_2 == lado_3:
        print('TIPO: EQUILÁTERO')
    elif lado_1 != lado_2 and lado_3 != lado_1 and lado_3 != lado_2:
            print('TIPO: ESCALENO')
    else:
        print('TIPO: ISÓSCELES')
else:
    print('triãngulo não possível')
    print('Digite outros seguimentos')
