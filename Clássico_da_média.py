nota_1 = input('Digite a primeira nota: ')# recebimento do valor
nota_1 = nota_1.replace(',','.') # aceitando números com vírgulas
nota_1 = float(nota_1) # string convertido para float

nota_2 = input('Digite a segunda nota: ') # recebimento do valor
nota_2 = nota_2.replace(',','.') # aceitando números com vírgulas
nota_2 = float(nota_2) # string convertido para float

nota_3 = input('Digite a terceira nota: ') # recebimento do valor
nota_3 = nota_3.replace(',','.') # aceitando números com vírgulas
nota_3 = float(nota_3) # string convertido para float

nota_4 = input('Digite a quarta nota: ') # recebimento do valor
nota_4 = nota_4.replace(',','.') # aceitando números com vírgulas
nota_4 = float(nota_4) # string convertido para float

média_simples = (nota_1 + nota_2 + nota_3 + nota_4) / 4

if média_simples < 5:
    print(f'A sua nota foi {média_simples:.2f}')
    print('REPROVADO!')

elif média_simples >= 5 and média_simples < 7:
    print(f'A sua nota foi {média_simples:.2f}')
    print('RECUPERAÇÃO')
else :
    print(f'A sua nota foi {média_simples:.2f}')
    print('APROVADO')