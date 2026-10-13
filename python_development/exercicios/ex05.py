import os
os.system("cls")

# Exercício 05
'''
  Você deve elaborar um algoritmo implementado em Python em que o usuário informe quantos alimentos consumiu naquele dia e depois possa informar o número de calorias de cada um dos alimentos.
  
  Como não foi estudado listas nesse capítulo você não deve se preocupar em armazenar todas as calorias digitadas, mas deve exibir o total de calorias no final.
'''

# Pede ao usuário a quantidade de alimentos consumidos
qtd_alimentos = int(input("Por favor, informe quantos alimentos você consumiu hoje: "))

# Inicializador
total_calorias = 0

# Laço de repetição
for alimento in range(1, qtd_alimentos + 1, 1):
  # Pede a quantidade de calorias consumidas do alimento
  caloria = int(input("Informe a quantidade de calorias do {} alimento: ".format(alimento)))

  # Calcula o total de calorias consumidas
  total_calorias = total_calorias + caloria

# Exibe o total de calorias consumidas
print("Foram consumidas {} calorias ao longo do dia".format(total_calorias))