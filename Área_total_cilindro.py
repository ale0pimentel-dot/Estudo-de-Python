altura = float(input("Digite a altura do cilindro: "))
raio = float(input("Digite o raio do cilindro: "))
A_circ = 3.14 * (raio * raio)
A_lat = 2 * 3.14 * raio * altura
A_total = (2 * A_circ) + A_lat
print(f"Área total do cilindro é : {A_total}")