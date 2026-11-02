# DICIONÁRIOS (EXIBIÇÃO)
# Modos de exibição de um dicionário
dicionario = {
  "Yoda": "Mestre Jedi",
  "Mace Windu": "Mestre Jedi", 
  "Anakin Skywalker": "Cavaleiro Jedi", 
  "R2-D2": "Dróide", 
  "Dex": "Balconista"
}

# Exibe somente o valor associado a chave "Dex"
print(dicionario["Dex"])

# Outra forma é usando
print(dicionario.get("André")) # Previne erros quando está buscando alguma chave dentro de um dicionário

# Retorna uma lista contendo todas as chaves do dicionário
print(dicionario.keys())

# Loop para iterar (percorrer ou repetir um conjunto de passos sobre uma sequência de elementos, processando um item de cada vez) pela lista de chaves do dicionário e a cada volta da variável chave vai assumir cada um dos valores
for chave in dicionario:
  # Mostrar todas as chaves dentro de dicionário
  # print(chave)
  # Ou
  # Mostrar apenas os valores do dicionário
  print(dicionario[chave]) # Entre colchetes "[]" são os valores dentro

# Mostra os valores do dicionário em forma de lista, é possível verificar se dentro do dicionário existe um valor
print(dicionario.values())

# Mostra a quantidade de valores
print(len(dicionario.values()))

# Verifica se tem o valor/personagem dentro dos valores do dicionário (True ou False)
print("Mestre Jedi" in dicionario.values())

# Mostra os itens do dicionário em uma lista, uma tupla formada por chave e valor
print(dicionario.items())

# Mostra as tuplas de cada item
for item in dicionario.items():
  print(item)

# DESEMPACOTAR UM ITEM
# A cada volta do loop a variável "item" assume uma das tuplas, o nome vai para variável nome e a categoria vai para variável categoria
for item in dicionario.items():
  nome, categoria = item
  print(f"O personagem {nome} é um {categoria}")

# O loop for a cada volta navegando pela lista de tuplas (dicionario.items()) será desempacotado a chave para variável nome e o valor para a variável categoria
for nome, categoria in dicionario.items():
  print(f"O personagem {nome} é um {categoria}")