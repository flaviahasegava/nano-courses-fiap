import os
os.system("cls")

# Exercício - Identificar as vogais na frase

# Pede ao usuário uma frase e deixa tudo em minúsculo (lower)
frase = input("Introduza uma frase: ").lower()

# Inicializador
total_vogais = 0

# O laço "for" percorre cada caractere da frase, um por um
for letra in frase:
    # Verifica se a letra atual está dentro do grupo de vogais
    if letra in "aeiou":
        # Se for vogal, adiciona 1 ao contador
        total_vogais += 1

# Exibe o resultado final (número total de vogais)
print(f"A frase contém {total_vogais} vogais.")