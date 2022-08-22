# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip().title()
print(f'Seu nome é {nome}')
x = nome.split()
print(f'Seu primeiro nome é {x[0]}')
print(f'Seu último nome é {x[-1]}')



# Para acessar os elementos de uma lista utilizamos a notação de colchetes, colocando o índice do elemento

# Que sempre inicia com 0, ou seja, o primeiro elemento tem o índice zero

#Como geralmente não sabemos o tamanho de uma lista, para acessar o último item podemos utilizar o índice -1

# Desta forma, sempre vamos acessar o último elemento de uma lista, independente da quantidade de itens dentro dela