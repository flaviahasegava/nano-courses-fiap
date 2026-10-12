import os
os.system("cls")

# Exercício 01
'''
  Você deve elaborar um algoritmo implementado em Python em que o usuário informe quantos alimentos consumiu naquele dia e depois possa informar o número de calorias de cada um dos alimentos.
  
  Como não foi estudado listas nesse capítulo você não deve se preocupar em armazenar todas as calorias digitadas, mas deve exibir o total de calorias no final.
'''

qtd_alimentos = int(input("Por favor, informe quantos alimentos você consumiu hoje: "))

total_calorias = 0

for alimento in range(1, qtd_alimentos + 1, 1):
  caloria = int(input("Informe a quantidade de calorias do {} alimento: ".format(alimento)))
  total_calorias = total_calorias + caloria

print("Foram consumidas {} calorias ao longo do dia".format(total_calorias))