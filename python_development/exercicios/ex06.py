import os
os.system("cls")

# Exercício 06
'''
  Olhando para o mercado de educação infantil, você e sua equipe decidem criar um aplicativo onde as crianças aprendam a controlar os seus gastos.

  Como forma de validar um protótipo, foi solicitado que você crie um script simples, em que o usuário deve informar QUANTAS TRANSAÇÕES financeiras realizou ao longo de um dia e, na sequência, deve informar o VALOR DE CADA UMA das transações que realizou.

  Seu programa deverá exibir, ao final, o valor total gasto pelo usuário e também a média do valor de cada transação.
'''

# Pede ao usuário a quantidade de transações feitas no dia
qtd_transacoes = int(input("Quantidade de transações feitas: "))

# Inicialização do acumulador
valor_total = 0

# Laço de repetição que recebe as transações
for i in range(qtd_transacoes):
  valor = float(input(f"Transação {i + 1}: "))
  valor_total = valor_total + valor

# Calcula a média do valor total de transações
media = valor_total / qtd_transacoes

# Exibe o relatório final
print(f"""
Relatório:
Quantidade de transações...........: {qtd_transacoes}
Valor total gasto..................: R$ {valor_total:.2f}
Média..............................: R$ {media:.2f}
""")