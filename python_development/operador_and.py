import os
os.system("cls")

# OPERADOR AND (E) - Verifica duas condições e retorna verdadeiro quando ambas as condições forem verdadeiras

# Exercício
'''
  Para acessar um sistema, o usuário deve digitar o username fulano_permitido e a senha 1138.

  Crie um script que receba e valide estas informações de acesso.
'''

# Pedir o username e a senha
username = input("Por favor, digite o seu nome de usuário: ")
senha = input("Por favor, digita a sua senha: ")

# Verifica se possui o username e senha permitidos para o acesso
if username.lower() == "fulano_permitido" and senha == "1138": # Função .lower() - Transforme o conteúdo da variável em letras minúsculas / O username digitado independente de estar com letras maiúsculas ou minúsculas será permitido o acesso (ex: Fulano_permitido, FULANO_PERMITIDO, etc)
  print("Acesso PERMITIDO. Login bem sucedido!")

# Exibe a mensagem de acesso negado
else:
  print("Acesso NEGADO! Login não autorizado.")
  print("Username ou senha incorretos.")