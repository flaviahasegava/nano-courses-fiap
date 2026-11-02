# LISTAS (INSERÇÃO DE DADOS)
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]

print(f"A lista original contém: \n {jedi}")

# INSERÇÃO NO FIM DA LISTA (APPEND)
jedi.append("Luminara") # Nome da lista . append e qual o valor que vai ser inserido na lista
# append é usado em listas e serve para adicionar um único elemento ao final de uma lista já existente alterando essa lista diretamente
print(f"Após a inserção a lista contém: \n {jedi}")
# Ex: fila de atendimento

# INSERÇÃO NO FIM DA LISTA COM INPUT
jedi.append(input("Insira o nome de um Jedi: ")) # O usuário adiciona o valor
print(f"Após a inserção a lista contém: \n {jedi}")

# INSERÇÃO EM POSIÇÃO ESPECÍFICA (INSERT)
jedi.insert(1, "Cebolinha") # Posição e o nome do valor que será preenchido
print(f"Após a inserção na posição indicada a lista contém: \n {jedi}")