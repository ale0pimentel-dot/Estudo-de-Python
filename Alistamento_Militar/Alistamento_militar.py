from datetime import date
nascimento = int(input('Qual o ano de nascimento?: '))
data_atual = int(input('ANO ATUAL -> digite zero: '))
data_atual = date.today().year
idade = data_atual - nascimento
print(f'O ano ATUAL é: {data_atual}')
if idade < 18:
    saldo_1 = 18 - idade
    print(f'Você tem {idade} anos')
    print('Você ainda vai ser alistar!')
    print(f'O tempo que ainda falta para se alistar é {saldo_1} anos')
    print(f'O teu alistamento vai ser no : {data_atual + saldo_1} ')
elif idade == 18:
    print('Hora de se alistar!')
elif idade > 18:
    saldo_2 = idade - 18
    print(f'Você possui {idade} anos, passou {saldo_2} anos do alistamento, que deveria ter sido feito, com 18 anos. ')
    print(f'O ano que você teria que ter se alistado é {data_atual - saldo_2 }')
