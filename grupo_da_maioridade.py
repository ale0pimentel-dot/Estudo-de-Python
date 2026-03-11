from datetime import date
atual = date.today().year
total_maior = 0
total_menor = 0
for pess in range(1,8):
    nasc = int(input(f'Em que ano a {pess}° pessoa nasceu? : '))
    idade = atual - nasc
    if idade >= 18:
        total_maior = total_maior + 1
    else:
        total_menor = total_menor +1
print(f'Ao total tem {total_maior} maiores de idade ')
print(f'E também tem {total_menor} menores de idade')
