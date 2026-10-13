import os
os.system("cls")

# Exercício - Tabuada

# Pede ao usuário o número da tabuada
num_tabuada = int(input("Qual tabuada deseja ver? "))

# Laço de repetição
for multiplicador in range(1, 11):
  resultado = multiplicador * num_tabuada

  # Exibe a tabuada
  print(f"{num_tabuada} x {multiplicador} = {resultado}")