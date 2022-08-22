# Programa que converta uma temperatura digitando em graus Celsius para graus Fahrenheit.
celsius = float(input('Informe a temperatura em ºC : '))
f = celsius * 1.8 + 32
# f = (9*c/5)+32
print(f' A temperatura de \033[1;31m{celsius}\033[m ºC  corresponde a \033[1;31m{f}\033[m ºF!')