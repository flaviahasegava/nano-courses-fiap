import os
os.system("cls")

# OPERADOR OR (OU) - Verifica se uma ou outra condição é verdadeira

# Exercício
'''
  Durante o aniversário da sua fundação, uma loja está presenteando clientes da seguinte forma:

  - Todas as compras de valor superior à R$1000, receberão um desconto de 10%.
  
  - Clientes selecionados receberam o cupom "FESTA", que também gera 10% de desconto na hora da compra (não importando o valor).

  - Os descontos não são cumulativos.

  Escreva um script em Python que receba um cupom e o valor de uma compra do usuário e informe o valor da compra.
'''

# Exibe a mensagem de boas-vindas
print("Bem-vindo(a) ao aniversário de fundação da nossa loja!")

# Pedir o nome do cliente, valor da compra e cupom de desconto
cliente = input("Por favor, digite o seu nome: ").strip() # .strip() - Remove os espaços invisíveis (ex: O usuário digita: " usuário " (com espaços) -> Saída: "usuário") 
valor_compra = float(input("Informe o valor da sua compra: R$"))
cupom = input("Insira um cupom de desconto válido: ").strip().lower()

# Verifica se a compra é maior que R$1000 ou se possui o cupom "festa"
if valor_compra >= 1000 or cupom == "festa":
  valor_compra = valor_compra * 0.90 # 10/100 = 0,10 (valor de desconto) -> 0,10 - 1 = 0,90 (valor final já descontado 10%)
  print("Você recebeu 10% de desconto!")

else:
  print("Você não tem direito ao desconto.")

# Exibe a mensagem final do valor da compra com ou sem desconto
print(f"{cliente}, o valor final da sua compra é de R${valor_compra:.2f}")
