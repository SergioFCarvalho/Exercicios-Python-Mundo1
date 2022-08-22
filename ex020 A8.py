#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. >também resolve com random.sample( x , 4(numero de individuos))
import random
n1 = input('Pirmeiro aluno : ')
n2 = input('Segundo aluno : ')
n3 = input('Terceiro aluno : ')
n4 = input('Quarto aluno : ')
alunos = [n1, n2, n3, n4]
random.shuffle(alunos)
print(f' A ordem de apresentação será\n {alunos}')