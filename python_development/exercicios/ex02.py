import os
os.system("cls")

# Exercício 02
'''
  Viajar é bom demais! Uma agência de viagens está propondo uma estratégia para alavancar as vendas após os impactos da pandemia do coronavírus.

  A empresa ofertará descontos progressivos na compra de pacotes, dependendo do número de viajantes que estão no mesmo grupo e moram na mesma residência.

  Para ajudar a tornar esse projeto real, você deve criar um algoritmo que receba o VALOR BRUTO do pacote, a CATEGORIA DOS ASSENTOS no vôo e a QUANTIDADE DE VIAJANTES que moram em uma mesma casa e calcule os descontos de acordo com a tabela abaixo:

  Categoria DESCONTOS
  - Econômica       2 viajantes -> 3%
                    3 viajantes -> 4%
                    4 viajantes ou mais -> 5%

  - Executiva       2 viajantes -> 5%
                    3 viajantes -> 7%
                    4 viajantes ou mais -> 8%

  - Primeira classe       2 viajantes -> 10%
                          3 viajantes -> 15%
                          4 viajantes ou mais -> 20%
                    
  O programa deverá exibir o valor BRUTO DA VIAGEM (o mesmo que foi digitado), o VALOR DE DESCONTO, o VALOR LÍQUIDO DA VIAGEM (valor bruto menos os descontos) e o VALOR MÉDIO POR VIAJANTE.
'''

# Exibe a mensagem de boas-vindas (\n -> pula para a próxima linha)
print("Bem-vindo(a) às promoções de pacotes da nossa agência!\n")

# Pede ao usuário o valor bruto, categoria e quantidade de passageiros
valor_bruto = float(input("Por favor, informe o valor da viagem: R$ "))
# upper() -> Muda o valor da variável para letras maiúsculas
categoria = input("Qual a categoria escolhida? (Econômica, Executiva ou Primeira classe) ").upper()
qtd_passageiros = int(input("Qual a quantidade de passageiros? "))

# Retira o desconto caso seja apenas 1 passageiro
valor_desconto = 0

# =======================================
# Categoria ECONÔMICA
# =======================================
if categoria == "ECONÔMICA":
  # Verifica quantidade de passageiros e calcula o desconto 
  if qtd_passageiros == 2:
    # Desconto 3%
    valor_desconto = valor_bruto * 0.97

  elif qtd_passageiros == 3:
    # Desconto 4%
    valor_desconto = valor_bruto * 0.96

  elif qtd_passageiros >= 4:
    # Desconto 5%
    valor_desconto = valor_bruto * 0.95

# =======================================
# Categoria EXECUTIVA
# =======================================
elif categoria == "EXECUTIVA":
  if qtd_passageiros == 2:
    # Desconto 5%
    valor_desconto = valor_bruto * 0.95

  elif qtd_passageiros == 3:
    # Desconto 7%
    valor_desconto = valor_bruto * 0.93

  elif qtd_passageiros >= 4:
    # Desconto 8%
    valor_desconto = valor_bruto * 0.92

# =======================================
# Categoria PRIMEIRA CLASSE
# =======================================
elif categoria == "PRIMEIRA CLASSE":
  if qtd_passageiros == 2:
    # Desconto 10%
    valor_desconto = valor_bruto * 0.90

  elif qtd_passageiros == 3:
    # Desconto 15%
    valor_desconto = valor_bruto * 0.85

  elif qtd_passageiros >= 4:
    # Desconto 20%
    valor_desconto = valor_bruto * 0.80

# Exibe a mensagem caso seja apenas 1 passageiro
else:
  print("Promoção inválida para a quantidade de passageiros.")

# Calcula o valor da passagem para cada passageiro
media_passageiro = valor_desconto / qtd_passageiros

# Verifica se é apenas 1 passageiro ou mais e exibe uma mensagem personalizada para a quantidade de passageiros 
# ========================
# 1 PASSAGEIRO
# ========================
if qtd_passageiros == 1:
  print(f'''
  Categoria:                     |  {categoria}
  -------------------------------------------------
  Passageiros:                   |  {qtd_passageiros}
  -------------------------------------------------
  VALOR DA VIAGEM
  Valor bruto:                   |  R$ {valor_bruto:.2f}
  ''')

# ========================
# MAIS DE 1 PASSAGEIRO
# ========================
else:
  print(f'''
  Categoria:                     |  {categoria}
  -------------------------------------------------
  Passageiros:                   |  {qtd_passageiros}
  -------------------------------------------------
  VALOR DA VIAGEM
  Valor bruto:                   |  R$ {valor_bruto:.2f}
  Valor líquido:                 |  R$ {valor_desconto:.2f}
  Valor médio por passageiro:    |  R$ {media_passageiro:.2f}
  ''')