import os
os.system("cls")

# Exercício 04
'''
  Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver um trabalho em parceria: um serviço em que as pessoas possam usar um estúdio profissional para gravar seus vídeos para o YouTube com máxima qualidade. O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus calculado por uma porcentagem sobre o faturamento que o canal do cliente obteve ao longo do ano.

  Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele e que calcula e exiba qual o valor do bônus que o cliente deve pagar a vocês. A tabela abaixo mostra a porcentagem de acordo com cada nível de assinatura:

  NÍVEL               PORCENTAGEM SOBRE O FATURAMENTO
  Basic               30%
  Silver              20%
  Gold                10%
  Platinum            5%
'''

# Exibe a mensagem de boas-vindas
print(f'''
+-------------------------------------------------------+
|         BEM-VINDO(A) AO ESTÚDIO PROFISSIONAL          |
|              Sistema de Cálculo de Bônus              |
+-------------------------------------------------------+
''')

# Pede o faturamento anual do canal
faturamento_anual = float(input("Por favor, informe o seu faturamento anual: R$ "))

# Exibe os níveis de assinatura e pede o tipo de assinatura
print("NÍVEIS DE ASSINATURA: Basic, Silver, Gold e Platinum")
tipo_assinatura = input("Qual o seu nível de assinatura? ").upper() 

# Variáveis de bônus iniciam zeradas e serão alteradas de acordo com a assinatura
percentual_bonus = 0
bonus = "0%"

# Verifica o tipo de assinatura e adiciona o bônus
# =================================
# Assinatura BASIC
# =================================
if tipo_assinatura == "BASIC":
  percentual_bonus = 0.30
  bonus = "30%"

# =================================
# Assinatura SILVER
# =================================
elif tipo_assinatura == "SILVER":
  percentual_bonus = 0.20
  bonus = "20%"

# =================================
# Assinatura GOLD
# =================================
elif tipo_assinatura == "GOLD":
  percentual_bonus = 0.10
  bonus = "10%"

# =================================
# Assinatura PLATINUM
# =================================
elif tipo_assinatura == "PLATINUM":
  percentual_bonus = 0.05
  bonus = "5%"

# Calcula o valor de bônus e o total do faturamento anual
valor_bonus = faturamento_anual * percentual_bonus
total = valor_bonus + faturamento_anual

# Verifica se o cliente digitou uma assinatura diferente das existentes
if tipo_assinatura != "BASIC" and tipo_assinatura != "SILVER" and tipo_assinatura != "GOLD" and tipo_assinatura != "PLATINUM":
  print(f"Assinatura não identificada. Tente novamente ou entre em contato com o nosso suporte. \nTotal: R$ {total:.2f}")

# Exibe a assinatura, faturamento anual, bônus e o total caso o cliente digite a assinatura correta
else:
  print(f'''
  Assinatura:             {tipo_assinatura}
  ---------------------------------------------------------
  Faturamento Anual:      R$ {faturamento_anual:.2f}
  Bônus:                  R$ {valor_bonus:.2f} | {bonus}
  Total:                  R$ {total:.2f}
  ''')