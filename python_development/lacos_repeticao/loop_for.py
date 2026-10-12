import os 
os.system("cls")

# Exemplo de FOR

# for -> loop baseado em intervalos
# range -> intervalo de valores
# Pega uma variável e faz com que ela assuma valores dentro de um determinado intervalo
for variavel in range(1, 101, 2): # Começa do "1", termina no "100" e incrementa "2"
  print(variavel)

# Exemplo 02

# Assume cada valor a variável "dia"
for dia in ["segunda", "terça", "quarta", "quinta", "sexta"]:
  print(f"Hoje é {dia}")
  
  # Verifica se o dia é segunda, quarta ou sexta
  if dia == "segunda" or dia == "quarta" or dia == "sexta":
    print("É dia de colcoar o lixo para o coletor.")