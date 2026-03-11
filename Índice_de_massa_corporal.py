print('Vamos calcular o seu Índice de Massa Corporal')
peso = input('Digite o teu peso. Kg:')
peso = peso.replace(',','.')
peso = float(peso)

altura = input('Digite a tua altura em metros (ex: 160cm = 1.60m ) : ')
altura = altura.replace(',','.')
altura = float(altura)

IMC = peso / altura ** 2
print(f'O seu IMC é igual a {IMC:.2f}')

if IMC < 18.5:
    print('Abaixo do peso')
elif IMC >= 18.5 and IMC < 25:
    print('Peso ideal')
elif IMC >= 25 and IMC < 30:
    print('Sobrepeso')
elif IMC >= 30 and IMC < 40:
    print('Obesidade')
else :
    print('Obesidade mórbida')