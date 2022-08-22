# Analisador de texto Exercício Python 022 curso em vídeo TIVE DIFICULDADE NAS DUAS ULTIMAS PARTES
nome = str(input('Digite seu nome completo :')).strip()
print(f'Seu nome em Maiúsculo é {nome.upper()}')
print(f'Seu nome em Minúsculo é {nome.lower()}')
print(f'Seu nome tem ao todo: {len(nome)- nome.count(" ")} letras')
separa = nome.split()
print(f'Seu primeiro {separa[0]} tem {len(separa[0])} letras')