num = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digte a razão da P.A: '))
for c in range(0,10):
    pa = num + c * r
    print(pa, end=' -> ')
print('Acabou')