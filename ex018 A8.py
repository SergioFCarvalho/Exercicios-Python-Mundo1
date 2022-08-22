#Faça um programa que leia um ângulo qualquer e mostre na tela o valor
# do seno, cosseno e tangente desse ângulo.
from math import radians ,sin , cos , tan
a = float(input('Qual ângulo : '))
sen = sin(radians(a))
print(f'O ângulo é {a} e tem SENO de {sen:.2f}')
cos = cos(radians(a))
print(f'O ângulo é {a} e tem o COSSENO de {cos:.2f}')
tang = tan(radians(a))
print(f'O ângulo é {a} e tem TANGENTE de {tang:.2f}')
