 # Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
 # se elas podem ou não formar um triângulo.
print('____' * 10)
print('Analisador de Triângulos')
a = float(input('Primeiro segmento : '))
b = float(input('Segundo segmento : '))
c = float(input('terceiro segmento : '))
if a + b > c and a + c > b and b + c > a:
    print('Os segmentos acima PODEM FORMA um triângulo !')
else:
    print('Os segmentos acima NÃO PODEM FORMA um triângulo !')
print('_____' * 10)
