import os
os.system("cls")

'''
  Uma lanchonete trabalha com diversos combos de lanches, conforme a tabela abaixo:

  COMBO 1 - Hambúrguer | R$ 12,50
  COMBO 2 - Cheeseburguer | R$ 15,00
  COMBO 3 - X-Bacon | R$ 17,50

  Crie um programa que receba o número de um combo e exiba o nome do lanche e o preço correspondente.
'''

# MATCH CASE 
# Usado para avaliar valores possíveis para uma variável ou um objeto (intervalo de valores bem definidos)
# Exemplo: dias da semana, números de combos, finais das placas de carros, etc.

# Exibe mensagem de boas-vindas e pede o número do combo
print("Bem-vindo(a)!")
numero_combo = int(input("Escolha o número do seu COMBO: "))

# Escolha do combo
match numero_combo:
  case 1: # Se o conteúdo da variável for "1", faça
    nome_prato = "Hambúrguer"
    valor_prato = 12.50
  case 2:
    nome_prato = "Cheeseburguer"
    valor_prato = 15.00
  case 3:
    nome_prato = "X-Bacon"
    valor_prato = 17.50
  case _: # Caso o usuário digite outra coisa
    nome_prato = None

# Verifica se o prato é válido e imprime o resultado 
if nome_prato: # Verifica o valor booleano que nome do prato recebe None, então se existe o prato = True, mas se não existir(None) = False
  print(f'''
    VOCÊ ESCOLHEU
    COMBO {numero_combo}: {nome_prato:^15} | R$ {valor_prato:8.2f}
  ''') # "^" Centraliza a palavra e ">" antes do número espaça do lado esquerdo

else:
  print("Essa opção não existe. Por favor, escolha um combo de 1 a 3.")