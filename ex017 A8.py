#Catetos e Hipotenusa
#programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co,ca)
print(f'A hipotenusa vai medir {hi:.2f}')
# 2 forma de fazer
'''from math import hypot
c1 = float(input('Cateto oposto: '))
c2 = float(input('Cateto adjacente: '))
h1 = hypot(c1 , c2)
print(f'A reposta é {h1:.2f}')'''