from random import randint
from time import sleep
computador = randint(0,5)
print('-=-' * 20)
print('vou pensar em um número entre 0 e 5. TEM ADIVINHAR.......')
print('-=-' * 20)
print('PROCESSANDO.....')
print('-=-' * 20)
sleep(2)
print('PENSEI')
print('-=-' * 20)
jogador = int(input('Escolha um número entre 0 e 5: '))
print('-=-' * 20)
if jogador == computador:
    print('VOCê VENCEU!!!!')
    print('-=-' * 20)
    print(f'Você pensou no {jogador} e eu TAMBÉM!!')
else :
    print('VOCÊ PERDEU HAHAHAHAHAHAH')
    print(f'VOCÊ pensou no {jogador} e eu no {computador}')
    print('TENTE OUTRA VEZ!!!')