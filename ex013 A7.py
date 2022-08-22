# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input('Seu salário é? R$ '))
sn = s + (s * 15/100)
print(f'O salário do funcionário é \033[1mR${s}\033[m, com o aumento de 15%, seu salário agora será \033[1mR${sn:.2f}')
