# TUPLAS CENÁRIO
# Uma lista e dentro com tuplas (coordernadas (x e y))
inimigos = [(10, 5), (30, 3), (1, 50)] # É possível remover os elementos de dentro da lista, cada coordenada são os inimigos (tupla)

# Enquanto o tamanho dos meus inimigos for maior que 0 (Enquanto ainda tiver inimigos dentro da lista, o usuário continuará digitando um par de valores X e Y, quando o usuário acertar a tupla será removida da lista)
while len(inimigos) > 0:

  # Pede a coordenada X e Y para o usuário
  x = int(input("Informe um valor para o eixo X: "))
  y = int(input("Informe um valor para o eixo Y: "))

  # Verifica se a tupla "(x, y)" estão dentro de itens da lista inimigos
  if (x, y) in inimigos:
    print("Você acertou um inimigo!")
    inimigos.remove((x, y)) # Remove a tupla

  else:
    print("Você errou!")

  # Exibe quantos inimigos "len" faltam para concluir o jogo
  print (f"Ainda restam {len(inimigos)} inimigos no mapa")