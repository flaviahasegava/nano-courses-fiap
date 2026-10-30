# FUNÇÃO COM PARÂMETRO

# Antes da função começar a ser executada ela vai precisar conhecer a dist&ancia e o tempo
def velocidade_media(distancia, tempo):
  vm = distancia / tempo
  print(f"A velocidade média foi de {vm:.0f}km/h")

distancia = float(input("Por favor, informe a distância percorrida: "))

tempo = float(input("Por favor, informe o tempo utilizado na viagem: "))

# Poderia colocar velocidade_media(500, 3) que seria a distância e o tempo, ao invés do usuário digitar a distância e o tempo
velocidade_media(distancia, tempo)

# Ex: quando vai ao restaurante de fast food e faz um pedido no balcão "Quero o pedido número 3"