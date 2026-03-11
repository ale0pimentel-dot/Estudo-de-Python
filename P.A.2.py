num = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digte a razão da P.A: '))
décimo = num + (10 - 1) * r
for c in range(num, décimo + r, r):
    print(c , end='->')
print('Acabou')