import os
os.system("cls")

# CONDIÇÃO ELIF - Abreviação de elif if ou "senão se", serve para testar múltiplas condições em sequência (elifs)

# Exercício
'''
  Uma empresa de telefonia está realizando uma promoção, onde os clientes podem receber alguns bônus para navegação na internet com base em uma pontuação. 

  1000 pontos -> 3GB de bônus
  500 pontos -> 1,5GB de bônus
  200 pontos -> 530MB de bônus

  Crie um programa que recebe o número de pontos e informe ao cliente quanto de bônus ele receberá
'''

# Pedir o nome do cliente
print("Seja bem-vindo(a) a nossa PROMOÇÃO de BÔNUS DE INTERNET. ")
nome_cliente = input("Por favor, qual o seu nome? ")

# Pedir o número de pontos do cliente
print(f"Olá, {nome_cliente}!")
pontos = int(input("Quantos pontos você possui? (200, 500 ou 1000) "))


# Verifica se o cliente digitou o número certo
if pontos < 0:
  print("OPS! Pontuação não identificada.")
  print("Verifique se você digitou o número certo de pontos. Por favor, digite novamente sua pontuação.")
  print("Quantidade mínima de pontos = 200 pontos")
  print("Quantidade máxima de pontos = 1000 pontos")

# Verifica se o cliente ultrapassou 1000 pontos
elif pontos > 1000:
  print("Pontuação ultrapassada!")
  print("Você possui mais de 1000 pontos. Digite novamente até 1000 pontos, por favor!")

# Verifica se o cliente tem 200 pontos
elif pontos == 200:
  print(f"Você possui {pontos} pontos.")
  print(f"PARABÉNS, {nome_cliente}! Você receberá 530MB de BÔNUS!")
  print("Aproveite!")

# Verifica se o cliente tem 500 pontos
elif pontos == 500:
  print(f"Você possui {pontos} pontos.")
  print(f"PARABÉNS, {nome_cliente}! Você receberá 1,5GB de BÔNUS!")
  print("Aproveite!")

# Verifica se o cliente tem 1000 pontos
elif pontos == 1000:
  print(f"Você possui {pontos} pontos.")
  print(f"PARABÉNS, {nome_cliente}! Você atingiu o máximo de pontos e receberá 3GB de BÔNUS!")
  print("Aproveite!")

# Verifica se o cliente não possui pontos
else:
  print(f"{nome_cliente}, você tem {pontos} pontos.")
  print("Você precisa de no mínimo 200 pontos ou máximo de 1000 pontos para resgatar o seu bônus de internet.")
  print("Por favor, digite novamente o número de pontos correto (200, 500 ou 1000).")