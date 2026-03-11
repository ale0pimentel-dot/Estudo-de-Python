import random
opções = [ 'pedra','papel','tesoura']
computador = random.choice(opções)
usuário = input('''Escolha entre:
[pedra]
[papel]
[tesoura]
Digite sua escolha: ''')
if computador == 'pedra' and usuário == 'papel':
    print(f'computador escolheu: {computador} e você escolheu {usuário}')
    print('Você venceu!')
elif computador == 'pedra' and usuário == 'tesoura':
    print(f'computador escolheu: {computador} e você escolheu {usuário}')
    print('O computador venceu!')
elif computador == 'pedra' and usuário == 'pedra':
    print(f'computador escolheu: {computador} e você escolheu {usuário}')
    print('Empate')

elif computador == 'papel' and usuário == 'tesoura':
    print(f'computador escolheu: {computador} e você escolheu {usuário}')
    print('Você venceu!')
elif computador == 'papel' and usuário == 'pedra':
    print(f'computador escolheu: {computador} e você escolheu {usuário}')
    print('O computador venceu!')
elif computador == 'papel' and usuário == 'papel':
    print(f'computador escolheu: {computador} e você escolheu {usuário}')
    print('Empate')

elif computador == 'tesoura' and usuário == 'pedra':
    print(f'computador escolheu: {computador} e você escolheu {usuário}')
    print('Você venceu!')
elif computador == 'tesoura' and usuário == 'papel':
    print(f'computador escolheu: {computador} e você escolheu {usuário}')
    print('O computador venceu!')
elif computador == 'tesoura' and usuário == 'tesoura':
    print(f'computador escolheu: {computador} e você escolheu {usuário}')
    print('Empate')
else:
    print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')