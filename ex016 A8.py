#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira
import math
num = float(input('Digite um número :'))
print(f'Você digitou {num} e a sua porção inteira é {math.floor(num)}')
# 2 forma de fazer
nume = float(input('Digite um valor:'))
print(f'O valor que você digitou foi {nume} e a sua porção inteira é {math.trunc(nume)}')
# 3 forma de fazer
numer =float(input('Digite um número: '))
print(f'O número é {numer} e sua porção inteira é {int(numer)}')
