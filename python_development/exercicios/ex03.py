import os
os.system("cls")

# Exercício 03
'''
  Hora de decidir! Os colaboradores da sua equipe foram sorteados para ganharem um console de última geração cada um por conta do bom desempenho que tiveram nos último projetos. Por uma questão de logística, porém, a empresa pede que toodos os 5 membros da equipe recebam o mesmo aparelho.

  Crie um algoritmo que o usuário possa digitar o voto de cada um dos 5 membros da equipe e, ao final, exiba qual foi o console escolhido e com quantos votos.

  As opções são:
  - PLAYSTATION
  - XBOX
  - NINTENDO
'''

# Exibe os consoles disponíveis para a votação
print(f'''
PREMIAÇÃO DE CONSOLE:
--------------------------------------
- PLAYSTATION
- XBOX
- NINTENDO
''')

# Pede os votos de cada colaborador
print("ESCOLHA APENAS 1. VOTE PARA O SEU CONSOLE!\n")
voto1 = input("Voto 1: ").upper()
voto2 = input("Voto 2: ").upper()
voto3 = input("Voto 3: ").upper()
voto4 = input("Voto 4: ").upper()
voto5 = input("Voto 5: ").upper()

# No começo contabiliza os votos em 0 para cada console
playstation = 0 
xbox = 0 
nintendo = 0 

# Adiciona as votações para cada console
# ============================
# VOTO 1
# ============================
if voto1 == "PLAYSTATION":
  playstation = playstation + 1

elif voto1 == "XBOX":
  xbox = xbox + 1

elif voto1 == "NINTENDO":
  nintendo = nintendo + 1

else:
  print("O colaborador 1 digitou um console inexistente e seu voto será desconsiderado.")

# ============================
# VOTO 2
# ============================
if voto2 == "PLAYSTATION":
  playstation = playstation + 1

elif voto2 == "XBOX":
  xbox = xbox + 1

elif voto2 == "NINTENDO":
  nintendo = nintendo + 1

else:
  print("O colaborador 2 digitou um console inexistente e seu voto será desconsiderado.")

# ============================
# VOTO 3
# ============================  
if voto3 == "PLAYSTATION":
  playstation = playstation + 1

elif voto3 == "XBOX":
  xbox = xbox + 1

elif voto3 == "NINTENDO":
  nintendo = nintendo + 1

else:
  print("O colaborador 3 digitou um console inexistente e seu voto será desconsiderado.")

# ============================
# VOTO 4
# ============================
if voto4 == "PLAYSTATION":
  playstation = playstation + 1

elif voto4 == "XBOX":
  xbox = xbox + 1

elif voto4 == "NINTENDO":
  nintendo = nintendo + 1

else:
  print("O colaborador 4 digitou um console inexistente e seu voto será desconsiderado.")

# ============================
# VOTO 5
# ============================  
if voto5 == "PLAYSTATION":
  playstation = playstation + 1

elif voto5 == "XBOX":
  xbox = xbox + 1

elif voto5 == "NINTENDO":
  nintendo = nintendo + 1

else:
  print("O colaborador 5 digitou um console inexistente e seu voto será desconsiderado.")

# Verifica qual console foi mais votado e se houve empate
if playstation > xbox and playstation > nintendo:
  print("O console escolhido foi: PLAYSTATION!")

elif xbox > playstation and xbox > nintendo:
  print("O console escolhido foi: XBOX!")

elif nintendo > playstation and nintendo > xbox:
  print("O console escolhido foi: NINTENDO!")

else:
  print("Houve empate, favor entrar em contato com a direção.")