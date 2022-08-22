# Ex 07 Crie programa que leia duas notas de um aluno e depois calcule e mostre sua média
# Usei int() porém é float() corrigido o float usa números flutuantes as notas podem sugir com decimais
import statistics
n1 = float(input('Digite a primeira nota :'))
n2 = float(input('Digite a segunda nota: '))
#m = (n1+n2)/2
notas = [n1 , n2]
statistics.mean(notas)
#print(f'Suas notas são {n1} e {n2} \nsua média é {m:.1f}')
print(statistics.mean(notas))
