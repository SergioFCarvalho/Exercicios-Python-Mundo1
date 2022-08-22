# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Qual seu salário ? R$ '))
if salario > 1250:
    novo = salario + (salario * 0.1 ) # calculo de porcentagem 10%
if salario <= 1250:
    novo = salario + (salario * 0.15) # calculo de porcentagem 15%
print(f'Quem ganhava R${salario:.2f} pasas ganhar agora R${novo:.2f} agora.')
