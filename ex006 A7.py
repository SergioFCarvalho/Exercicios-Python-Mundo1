# Ex06 Crie um algoritimo que leia um número e mostre seu dobro,triplo e raiz quadrada
n = int(input('Digite um número : '))
print(f'O número é {n}. \n O dobro \033[31m{n*2}.\033[m \n O triplo \033[32m{n*3}.\033[m \n A raiz quadrada é {n**(1/2):.2f}')
