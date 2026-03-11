from colorama import Fore
velocidade = float(input("Qual é a sua velocidade atual do carro?: "))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print(Fore.GREEN + 'Limite NÃO ultrapassado')
    print(Fore.GREEN + 'Tenha uma viagem!!')
else :
    print(Fore.RED + 'MULTADO!! VOCÊ ULTRAPASSOU O LIMITE DE VELOCIDADE PERMITIDO, QUE É 80KM/H')
    print(Fore.RED + f'VOCÊ DEVERÁ PAGAR UMA MULTA DE {multa}R$')
    print(Fore.YELLOW + 'TENHA UM BOM DIA! DIRIJA COM SEGURANÇA!')