import os
os.system("cls")

# Exercício - Somador Condicional

# Inicializador
soma = 0

# Laço condicional
while True: # Enquanto for verdade
  numero = int(input("Digite um número: "))
  soma = soma + numero

# Verifica caso o número seja negativo ele termina o laço / para de pedir o número e exibe a soma total
  if numero < 0:
    print(f"Soma total: {soma}")
    break # Pausa o laço