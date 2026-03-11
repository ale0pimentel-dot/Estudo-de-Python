from colorama import Fore
print('SEJA BEM VINDO(A)')
distância = float(input('Por favor , me informe qual é a distância, em KM, da viagem?: '))
preço_1 = distância * (0.50)
preço_2 = distância * (0.45)
print(Fore.LIGHTWHITE_EX + 'ATENÇÃO!')
print(Fore.RED +'Para viagens até 200KM, 0,50R$ por KM')
print(Fore.RED +'Para viagens maiores que 200KM, 0,45R$ por KM')
if distância <= 200:
    print(Fore.YELLOW + f'O preço da passagem é {preço_1:.2F}R$')
elif distância > 200:
    print(Fore.YELLOW + f'O preço da passagem é {preço_2:.2F}R$')