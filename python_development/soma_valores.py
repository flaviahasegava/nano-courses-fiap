print("Programa de soma de valores")

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

soma = valor1 + valor2

# Duas formas
print(f"A soma é {soma}") # f-string (formatted string literal)
print("A soma é {}".format(soma)) # {} substituído pelo valor da variável (soma)