valor = int(input("Digite seu número de 0 até 9999: "))
print(f"Seu número é {valor}")
unidades = valor // 1 % 10
dezenas = valor // 10 % 10
centenas = valor // 100 % 10
milhares = valor // 1000 % 10
print(f"Unidades {unidades}")
print(f"Dezenas {dezenas}")
print(f"Centenas {centenas}")
print(f"Milhares {milhares}")