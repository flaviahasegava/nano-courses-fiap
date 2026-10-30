# Crie um programa onde o professor digite notas de uma quantidade indeterminada de alunos. Quando ele terminar, exibir a média aritmética.

# Lista das notas
notas = []

# Loop while para verificar se o professor quer digitar a nota ou não
while input("Deseja inserir uma nota? S - Sim e N - Não: ").upper() != "N":
  # Pede para o professor inserir as notas
  notas.append(float(input("Nota: ")))

# Calcula a média com sum (soma) e len (tamanho da lista / quantidade)
media = sum(notas) / len(notas)

# Exibe a média
print(f"Para as notas digitadas, a média foi de {media:.2f}")