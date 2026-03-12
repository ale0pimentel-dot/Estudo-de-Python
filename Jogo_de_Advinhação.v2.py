from random import randint
from time import sleep
tentativas = 0
computador = randint(0,10)
print('Olá! Sou seu computador!')
sleep(2)
print('Vamos jogar um jogo de advinhação? Eu penso em um número entre 0 e 10')
sleep(3)
print('E você tenta até acertar!! É divertido!!')
sleep(2)
print('Vamos ??')
pergunta = str(input('Sim ou Não? : ')).strip().upper()
if pergunta == 'SIM':
    tent = int(input('Qual foi o número que o computador escolheu?: '))
    while tent != computador:
        tentativas = tentativas + 1
        tent = int(input('Tente novamente: '))
    print(f'Você acertou!!')
    print(f'Seu número de erros foi = {tentativas} ')
else:
    print('Ok, até mais tarde!!')
