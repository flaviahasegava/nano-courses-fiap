# FUNÇÕES (RETORNO)

# A função recebe dados através de parâmetros
def velocidade_media(distancia, tempo):
  vm = distancia / tempo

  # Retorna valores
  return vm # Variável que vai ser retornada "vm"
  # "return" -> é a instrução de uma função, encerra uma função
  # Quando não possui uma instrução "return" a linguagem devolve um valor nulo padrão (None)

# Ao usar "return vm" é preciso dar uma finalidade para essa instrução (exibir o resultado)
# Uma forma mais longa: print(f"A velocidade média é de {velocidade_media(500, 3):.2f}")

# Outra forma
variavel = velocidade_media(500, 3)

# Com a função, pode ser feito outros cálculos / ou armazenar em algum banco de dados
variavel = variavel * -1

# Pode ser feito a exibição do resultado
print(f"A velocidade média foi de {variavel:.2f}")


velocidades_medias = []
# Loop de repetição que passa por todos os dias da semana
for dia in ["segunda", "terça", "quarta", "quinta", "sexta"]:

  dist = float(input(f"Insira a distância percorrida na {dia}: "))

  temp = float(input(f"Insira o tempo da viagem da {dia}: "))

  velocidades_medias.append(velocidade_media(dist,temp))

print(f"As velocidades médias da semana foram {velocidades_medias}")

# Nem toda função precisa ter return e nem toda função precisa ter um print
# Quando uma função terminar, preciso que ela devolva um valor para alguém? Se sim, é usado o "return", caso ao completar a tarefa e ela pode ser encerrada, não é preciso usar o "return"