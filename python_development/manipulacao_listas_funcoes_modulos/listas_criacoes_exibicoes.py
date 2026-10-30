# LISTAS (CRIAÇÃO E ITERAÇÃO)

# Geralmente é criado uma lista vazia quando o usuário precisa inserir os dados ao longo do funcionamento do programa ou ao extrair os dados de algum outro lugar (como um banco de dados, um arquivo de texto ou algo do tipo)

# CRIAÇÃO DE UMA LISTA VAZIA
lista = [] # Nome da lista e o símbolo de colchetes indica uma criação de lista
print(type(lista)) # A função "type" retorna o tipo de um objeto ou uma variável 

# CRIAÇÃO DE UMA LISTA COM OS JEDI YODA, LUKE, OBI-WAN E ANAKIN
# Índice   0       1        2         3
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]

# EXIBIÇÃO DE UMA LISTA COMPLETA
print(jedi)

# EXIBIÇÃO DE UMA POSIÇÃO ESPECÍFICA NA LISTA
print(jedi[0])

# ELEMENTO ÍNDICE
# É um número inteiro que identifica a posição de um determinado valor dentro de uma estrutura.

# EXIBIÇÃO DOS ÚLTIMOS ELEMENTOS
print(jedi[-1]) # O último elemento sempre é identificado como "-1"
# Índice    -4      -3        -2        -1
# jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
print(jedi[1:3]) # O ":" indica um intervalo de valores dentro de uma lista / Ele entende que quer começar a sublista pelo item de índice "1" e o ":" até qual elemento eu quero pegar.
# Pega o elemento do índice "1" até o elemento "2"
# Índice    0       1        2         3
# jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
# [inicio:fim] O limite final não é incluído (ele é exclusivo). Seria "comece no índice inicio e pare antes de chegar no índice fim".

# EXIBIÇÃO DE CADA ITEM DA LISTA
# O loop for vai usar como intrvalo a lista "jedi" (composta pelos 4 itens) e que a cada volta do loop for, a variável "nome" vai assumir um dos elementos do meu intervalo e a cada volta vai exibir o conteúdo da variável
for nome in jedi: 
  print(nome)

# Exemplo de onde poderia ser usado: E-commerce (lista com todos os produtos que quero exibir na tela e depois utilizar o loop for para percorrer a lista e exibir os produtos para o usuário)