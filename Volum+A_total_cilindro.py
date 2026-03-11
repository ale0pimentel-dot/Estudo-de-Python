altura = float(input("Digite a altura: "))
raio = float(input("Digite o raio: "))
if altura <= 0 or raio <= 0:
        print("Valores inválidos")
        print("Digite aoenas valores positivos")
elif altura > 0 and raio > 0:
        A_circ = 3.14 * (raio **2)
        Volume_cili = A_circ * altura
        print(f"O volume é {Volume_cili: .2f}")
        A_lateral = 2 * 3.14 * raio * altura
        print(f"A área lateral é {A_lateral: .2f}")
        A_total = (2 * A_circ) + A_lateral
        print(f"A área total é {A_total: .2f}")
print("<<<<<FIM>>>>>")