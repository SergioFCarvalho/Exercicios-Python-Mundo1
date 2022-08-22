  # Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
print('_-_' * 15)
print('Descubra se o número é  PAR ou ÍMPAR :)')
print('_-_' * 15)
num = int(input('Digite um número inteiro: '))
r = num % 2         # Para saber se o número é par ou ímpar basta dividir ele por 2 e se o resto da operação é 0 zero.
if r == 0:
    print(f'O número {num} é PAR.')
else:
    print(f'O número {num} é ÍMPAR.')
