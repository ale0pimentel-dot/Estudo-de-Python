from datetime import date
ano = int(input('Qual ano deseja analisar? Coloque 0 (zero) para saber o ano atual: '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) :
    print(f'O {ano} é ano bissexto')
else:
    print(f'O {ano} não é ano bissexto')