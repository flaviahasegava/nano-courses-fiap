# DICIONÁRIOS (CRIAÇÃO E ESTRUTURA)
# Para criar um dicionário é utilizado colchetes "{}" e dentro dele a chave, dois pontos : e o valor, cada um separado por vírgula
dicionario = {
  # As chaves estão entre "", pois são strings
  # Chave    Valor (separados por vírgula no final)
  "Yoda": "Mestre Jedi",
  "Obi-Wan": "Mestre Jedi", 
  "Anakin": "Cavaleiro Jedi", 
  "Grogu": "Youngling", 
}

print(type(dicionario)) # Mostra o tipo da variável

# Mostra a estrutura completa do dicionário com chave e valor
print(dicionario) 

produto = {
  "nome": "Cafeteira",
  "preco": 100.00,
  "fornecedores": ["Fornecedor Supimpa", "Fornecedor Maneiro", "Fornecedor legal"]
}

print(produto)