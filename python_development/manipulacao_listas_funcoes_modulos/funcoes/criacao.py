# "def" - Indica a criação de uma função
# Após o "def" é o "nome da função"
def velocidade_media():

  distancia = float(input("Por favor, informe a distância percorrida: "))

  tempo = float(input("Por favor, informe o tempo utilizado na viagem: "))

  vm = distancia / tempo

  print(f"A velocidade média foi de {vm}")

# Chama a função
velocidade_media()