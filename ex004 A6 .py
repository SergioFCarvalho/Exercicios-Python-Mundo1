 # Faça um programa que leia algo pelo teclado e mostre na tela
 # o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input('\033[2;45mDigite algo: \033[m')
print('Qual o tipo primitivo desse valor :', type(n))
print('Só tem espaços?', n.isspace())
print("É número?", n.isnumeric())
print('É alfabético?', n.isalpha())

