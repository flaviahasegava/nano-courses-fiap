# LISTAS (RECURSOS)

# VALORES FORA DE ORDEM
valores = [1, 7, 7, 19, 3, 2, 11, 15, 6, 1, 5, 3.5]

# EXIBIÇÃO DA LISTA
print("A lista foi criada assim: {}".format(valores))

# CONTAGEM DE ELEMENTOS 1
contagem = valores.count(1) # Armazena em uma variável = Quantas vezes aparece o elemento "1"
print(f"A contagem de números 1 foi de {contagem}")

# INVERTENDO A LISTA
valores.reverse()
print(f"A lista invertida ficou assim: {valores}") # Coloca o nome da lista

# ORDENANDO A LISTA
valores.sort()
print(f"A lista em ordem crescente ficou assim: {valores}")

# ORDEM DECRESCENTE
valores.sort(reverse=True) # Ordene a lista na ordem crescente, mas coloque em ordem inversa, ordem decrescente
print(f"A lista em ordem decrescente ficou assim: {valores}")

# TAMANHO DA LISTA (CONTA QUANTOS ELEMENTOS TEM NA LISTA)
quantidade = len(valores) # len (length) - comprimento ou tamanho
print(f"A quantidade de elementos na lista é: {quantidade}")
# Ex: Carrinho de compras (quantos itens foram inseridos), controle de alimentação (tudo o que foi consumido ao longo do dia e ter como saber quantas refeições foram feitas), etc

# SOMA DOS ELEMENTOS
soma = sum(valores) # Soma todos os valores dentro da lista
print(f"A soma dos valores é: {soma}")