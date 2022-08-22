# Jogo da Adivinhação v.1.0
# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint              # importação do randomizador para sorteio de números
from time import sleep                  # importação de tempo para o programa esperar alguns segundos
computer = randint(0, 5)                # Faz o computador sortea números predefinidos
print('----' * 30 )
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('----' * 30 )
player = int(input('Em que número eu pensei? ')) # jogador escolhe número
print('PROCESSANDO.....')
sleep(3)
if player == computer:
    print('PARABÉNS! Você conseguiu me vencer!!!')
else:
    print(f'GANHEI! Eu pensei no número {computer} e não no número {player}!')
print('>>> Fim de jogo <<<')
