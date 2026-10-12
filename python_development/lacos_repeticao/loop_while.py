import os 
os.system("cls")

# Exemplo de WHILE

# Declarar as variáveis na memória
resposta = ""
tentativas = 0

# O loop WHILE para de executar quando a condição deixar de ser verdadeira (quando o usuário digitar o "42")
while resposta != "42":
  resposta = input("Qual a resposta da vida, do universo e tudo mais? ")
  # Conta o número de tentativas do usuário (a variável "tentativas" conta como 0 e vai somando 1)
  tentativas = tentativas + 1

# Essa linha de código só será executada quando o loop while parar de ser executado
print("Parabéns! Você acertou!\nNão esqueça a sua toalha!")
print(f"Você precisou de {tentativas} tentativas")

# Exemplo 02

tentativas1 = 0

while True: # Loop infinito (roda de qualquer jeito) / Enquanto for verdadeiro
    resposta = input("Qual a resposta da vida, do universo e tudo mais? ")
    # Atalho que significa "tentativas1 = tentativas1 + 1" ou "some + 1"
    tentativas1 += 1

    # Se a resposta for igual a "42" termina a condição while True
    if resposta == "42":
        break # O break "quebra"/para o loop e o programa continua na linha de baixo

print(f"Você precisou de {tentativas1} tentativas")

# Exemplo 03

numero = 1

# Repete enquanto a variável "numero" for menor ou igual a "20"
while numero <= 20:
   print(numero)
   # Incrementa a variável "numero" de 1 em 1
   numero = numero + 1