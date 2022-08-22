# Conversor de medidas (metros)
m = float(input('\033[43mDigite a medida: \033[m'))
cm = m * 100
mm = m * 1000
dm = m * 10
da = m / 10
hm = m / 100
km = m / 1000
print(f'A medida de {m}m corresponde a:')
print(f'{km:.3f}km')
print(f'{hm:.2f}hm')
print(f'{da:.1f}dam')
print(f'{dm:.0f}dm')
print(f'{cm:.0f}cm')
print(f'{mm:.0f}mm')
print('ok')

