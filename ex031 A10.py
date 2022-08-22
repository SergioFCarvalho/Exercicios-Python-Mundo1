# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = float(input('Qual é a distância da sua viagem? '))
print(f'Você esta preste a iniciar uma viagem de {km}km.')
if km <= 200:
    k1 = km * 0.50
    print(f'E o preço da sua passagem será de R${k1:.2f}')
else:
    k1 = km * 0.45
    print(f'E o preço da sua pasagem será de R${k1:.2f}')