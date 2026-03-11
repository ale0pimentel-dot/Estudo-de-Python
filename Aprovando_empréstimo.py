casa = input('Qual é o valor da casa? R$: ')
casa = casa.replace('.','').replace(',','.')
casa = float(casa)
salário = input('Qual o o seu salário? R$: ')
salário = salário.replace('.','').replace(',','.')
salário = float(salário)
tempo = float(input('EM quantos anos pagará? : '))
prestação_mensal = casa / (tempo * 12)
print(f'A prestação a ser paga é R${prestação_mensal:.2f}')
if prestação_mensal > (30 / 100 * salário):
    print('Pretação NEGADA!')
else :
    print('Prestação APROVADA!')