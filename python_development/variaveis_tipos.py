# Tipo de dados
# str (string) - Textos/caracteres (ex: "Nome", "123")
# int (integer) - Números inteiros (ex: 4, -7, 0)
# float (floating point) - Números decimais (ex: 3.61, -9.21)
# bool (boolean) - Valores lógicos (True ou False)
# Função type() - Exibe o tipo de dado de uma variável ou valor (str, int, float ou bool)

nome = "Flávia"
idade = 20
altura = 1.75
online = True
teste = "123"

print(type(nome))
print(type(idade))
print(type(altura))
print(type(online))
print(type(teste))
print(int(teste)) # Convertido o texto da variável "teste" para um número int (inteiro)
print(float(teste)) # Convertido o texto da variável "teste" para um número float (decimal)

# Transformar textos e números para um tipo lógico (bool)
# Qualquer número diferente de 0 = True
# O número 0 = False
# Um texto vazio = False (ex: " ")
# Texto com caracteres = True

print(bool(0))
print(bool(1994))
print(bool(""))
print(bool("Flávia"))