#  Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
#  e a quantidade de tinta necessária para pintá-la,
#  sabendo que cada litro de tinta pinta uma área de 2 m².
larg = float(input('Largura da parede : '))
alt = float(input('Altura da parede : '))
a = larg * alt
print(f'Sua parede tem a dimensão de {larg} x {alt} e sua área é de {a}m²')
t = a / 2
print(f'Para pintar essa parede você vai precisar de {t}l de tinta.')