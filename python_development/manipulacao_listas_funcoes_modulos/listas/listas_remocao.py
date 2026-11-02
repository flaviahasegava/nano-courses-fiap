# LISTAS REMOÇÃO
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]

# REMOÇÃO DO ÚLTIMO VALOR (POP)
jedi.pop()
print(jedi)

# REMOÇÃO DE UM VALOR EM POSIÇÃO ESPECÍFICA
jedi.pop(1) # Posição do qual deseja remover o elemento
print(jedi)

# REMOÇÃO DE UM ITEM ESPECÍFICO
jedi.remove("Yoda") # Remove o elemento pelo valor/nome
print(jedi)

# REMOÇÃO CASO NÃO EXISTA O ELEMENTO
# jedi.remove("Yoda") Retorna um erro caso o elemento não exista na lista
# print(jedi)

# APAGAR A LISTA TODA
jedi.clear()
print(jedi)