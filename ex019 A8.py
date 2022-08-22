#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido. > Sorteando um item na lista
'''import random
n1 = input('Primeiro aluno : ')
n2 = input('Segundo aluno : ')
n3 = input('terceiro aluno : ')
n4 = input('Quarto aluno : ')
lista = [n1 , n2 , n3 , n4]
escolhido = random.choice(lista)
print(f'O escolhido foi {escolhido}!')'''
from random import choice
n1 = input('Primeiro : ')
n2 = input('Segundo : ')
n3 = input('Terceiro : ')
n4 = input('Quarto : ')
n5 = input(' Quinto : ')
lista =[n1, n2, n3, n4, n5]
print(f'\nO sorteado foi \033[1m{choice(lista)}!')
