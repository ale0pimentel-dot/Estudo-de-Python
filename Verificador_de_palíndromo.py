frase = str(input('Digite uma frase: ')).strip().upper() #tratou a frase, tirando os espaços e tamanhos de palavra
palavra = frase.split() # transformou em listas, com isso tira os espaços internos
junto = ''.join(palavra) # juntou todas as palavras sem espaço
'''inverso = '' '''
inverso = junto[::-1]  #fatiamneto
'''for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]'''
print(junto,inverso)
if inverso == junto:
    print(f'O inverso de {junto} é {inverso}')
    print('É palíndromo')
else:
    print('Não é palíndromo')