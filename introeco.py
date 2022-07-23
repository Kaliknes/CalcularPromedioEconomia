print('Bienvenido para calcular su promedio ingrese sus notas')

cert = [int(input('Certamen 1: ')), int(input('Certamen 2: '))]
ctrl = [int(input('Control 1: ')), int(input('Control 2: ')), int(input('Control 3: ')), int(input('Control 4: '))]
ne = float(input('Nota ensayo: '))
pc = 0.0
pq = 0.0

for c in cert:
    if c >= 55:
        for cr in cert:
            pc += cr
        pc /= 2
        pc *= 0.6
        print('Calculando promedio certamenes...')
        break
for q in ctrl:
    pq += q
pq /= 4
pq *= 0.25
ne *= 0.15
print('Calculando promedio controles...')
ns = pc + pq + ne
print('Calculando promedio semestral...')

if pc == 0.0:
    print(f'Reprobado por que no tiene ningun certamen arriba de 55.')
elif ns < 55:
    print(f'Reprobado con {ns}.')
elif ns >= 55:
    print(f'Aprobado con {ns}.')
