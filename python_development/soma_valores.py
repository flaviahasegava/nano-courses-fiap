import os
os.system("cls")

# Exibe a mensagem
print("Programa de soma de valores")

# Pedir os valores 1 e 2
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# Calcula a soma dos 2 valores
soma = valor1 + valor2

# Exibe a soma (Duas formas de fazer)
print(f"A soma é {soma}") # f-string (formatted string literal)
print("A soma é {}".format(soma)) # {} substituído pelo valor da variável (soma)