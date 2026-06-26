somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for i in range(1,5):
    print(f'---------- {i}° PESSOA ----------')
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F] : ')).strip().upper()
    if i == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    somaidade = somaidade + idade
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1
médiaidade = somaidade / 4
print(f'A média de idade do grupo é {médiaidade} anos')
print(f'O homem mais velho é {nomevelho} e ele tem {maioridadehomem} anos')
print(f'O total de mulheres com menos de 20 anos é {totmulher20} anos')
