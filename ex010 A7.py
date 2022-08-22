# Converso de moedas  de (Real => Dólar) para <converter basta pega o real e dividir pela cotação do dólar>
import time
r = float(input('\033[33;40mDigite quanto você possui na carteira ? R$  \033[m'))
d = r / 5.30
print(f'Você tem R$ {r:.2f} reais')
time.sleep(1)
print(f' Com {r:.2f} você pode comprar US$ {d:.2f} ')
print('ok')