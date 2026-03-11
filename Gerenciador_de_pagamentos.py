print('====================LOJAS ALEJANDRO====================')
total = input('Digite o valor total. :R$ ')
total = total.replace(',','.')
total = float(total)

print('''FORMAS DE PAGAMENTO :
[1] à vista dinheiro/ cheque

[2] à vista cartão

[3] 2x cartão

[4] 3x ou mais no cartão''')

opção = int(input('Escolha uma opção: '))

if opção == 1:
    desc_10 = total * 10 / 100
    print(f'Total a pagar com desconto de 10% é : {(total - desc_10):.2f}R$')

elif opção == 2:
    desc_5 = total * 5 / 100
    print(f'O total a ser pago com desconto de 5% é : {(total - desc_5):.2f}R$')

elif opção == 3:
    print(f'O total é : {total:.2f}R$ , sendo as duas parcelas de {(total / 2):.2f}R$')

elif opção == 4:
    parcelas = int(input('Quantas parcelas ? (Observação: o mínimo de parcelas é 3) : '))
    if parcelas >= 3 and parcelas <= 12:
        juros = total * 2 / 100
        juros_total = juros * parcelas
        total_final = total + juros_total
        total_parcela = total_final / parcelas
        print(f'O total a ser pago: {(total_final):.2f}, sendo {parcelas} parcelas de: {(total_parcela):.2f}R$')
    else :
        print('Esse não é o mínimo de parcelas em que trabalhamos')
      
else:
    print('Opção inválida! Tente novamente! ')
