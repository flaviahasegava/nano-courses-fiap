# DICIONÁRIOS
# Um dicionário é uma estrutura com base na lógica de chave e valor / Uma estrutura que associa um dado a outro dado
# A chave é algo único e o valor é o conteúdo associado a essa chave
# É usado chaves para dicionarios
# Os valores do dicionário podem ser valores numéricos, de texto, lógicos e listas ou tuplas como valores do dicionário
# Exemplo: dicionário de produtos indicando os fornecedores do produto

# Criando as duas listas
personagens = []
categorias = []

# Executa um loop 10 vezes
for x in range(10):
  # Pede ao usuário que informe um nome e coloca na lista de personagens
  personagens.append(input("Informe o nome do personagem: "))

  # Pede ao usuário que informe a categoria e coloca na lista de categorias
  categorias.append(input("Informe a categoria do personagem: "))

# Executa um loop 10 vezes
for indice in range(10):
  # Exibe a cada volta o que está contido em um índice de personagens e categorias
  print("O personagem {} é um(a) {}".format(personagens[indice], categorias[indice]))