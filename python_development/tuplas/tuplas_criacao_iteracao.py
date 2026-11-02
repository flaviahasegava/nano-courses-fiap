# TUPLAS CRIAÇÃO
# Uma tupla nunca é criada vazia, é inserida com dados
categorias = ("Youngling", "Padawan", "Jedi", "Mestre")

print(categorias[-1]) # Exibe o último item da tupla
print(len(categorias)) # Mostra o tamanho da tupla, quantos elementos possui
# Ou
print(categorias.count("Jedi")) # Contar quantas vezes a palavra "Jedi" aparece na tupla

# Não é possível usar "append" (adicionar valor) nas tuplas

# Iterar
# Faz um loop que mostra todos os valores dentro da tupla
for categoria in categorias:
  print(categoria)

categorias = ("A", "B", "C", "D", "E") # Ao criar uma nova tupla, a anterior é destruída e usada esses novos valores

categoria = input("Insira a categoria da sua CNH: ")

# Verifica se existe na "categoria" digitada nas "categorias", ou seja, na tupla (o valor que o usuário digitou é um dos itens da minha tupla?)
if categoria in categorias:
  print("Categoria existente!")

else:
  print("Categoria inexistente!")