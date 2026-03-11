ordem = [] #lista, vai receber os valores
for pessoa in range(1,6): #repetição dos inputs
    peso_pessoa = input(f'Digite o seu peso da {pessoa}° pessoa: ')
    peso_pessoa = float(peso_pessoa.replace(',', '.')) # recebendo num com vírgulas
    ordem.append(peso_pessoa) # colocando cs valores na lista 'ordem'
ordem.sort() # colocando em ordem crescente
peso_maior = max(ordem)
peso_menor = min(ordem)
print(f'Os pesos registrados foram {ordem}')
print(f'O maior peso registrado foi {peso_maior}KG , e o menor peso registrado foi {peso_menor}KG')
