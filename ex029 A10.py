                # Escreva um programa que leia a velocidade de um carro.
                # Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
                # A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual a velocidade do seu carro? '))
multa = (velocidade - 80) * 7
if velocidade == 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print(f'MULTADO! Você excedeu o limite de velocidade 80Km/h\nVocê deve pagar uma multa de R${multa:.2f}!')
    print('Tenha um bom dia! Dirija com segurança!')

# OU
# velocidade = float(input('Qual a velocidade do seu carro? '))
# if velocidade > 80:
#     multa = (velocidade - 80) * 7
#     print(f'MULTADO! Você excedeu o limite de velocidade 80Km/h\nVocê deve pagar uma multa de R${multa:.2f}!')
# print('Tenha um bom dia! Dirija com segurança!')
