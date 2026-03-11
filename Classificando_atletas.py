from datetime import date
nascimento = int(input('Informe o ano de nascimento do atleta: '))
data_atual = date.today().year
idade = data_atual - nascimento
if idade <= 9:
    print(f'A idade do atleta é de {idade} anos.')
    print('A categoria do atleta: MIRIM')
elif idade > 9 and idade <= 14:
    print(f'A idade do atleta é de {idade} anos.')
    print('A categoria do atleta: INFANTIL')
elif idade > 14 and idade <= 19:
    print(f'A idade do atleta é de {idade} anos.')
    print('A categoria do atleta: JUNIOR')
elif idade > 19 and idade <= 25:
    print(f'A idade do atleta é de {idade} anos.')
    print('A categoria do atleta: SÊNIOR')
else :
    print(f'A idade do atleta é de {idade} anos.')
    print('A categoria do atleta: MASTER')