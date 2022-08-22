# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.> usando in que é um operador do python
nome = str(input('Qual seu nome completo ?')).strip()
n1 = 'silva' in nome.lower()
print(f'Seu nome tem SILVA ? {n1}')