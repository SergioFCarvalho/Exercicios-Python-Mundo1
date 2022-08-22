# Faça um programa que leia uma frase pelo teclado e mostre quantas
# vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite a frase :')).strip().upper()
print(f'Na frase digitada a letra (A) aparece {frase.count("A")} vezes')
x = frase.find('A')+1
print(f'A primeira letra A aparece na posição {x}')
print(f'A ultima letra A apareceu na posição {frase.rfind("A")+1}')

