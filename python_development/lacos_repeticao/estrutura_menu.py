import os
os.system("cls")

# Exercício MENU

# Inicializador
opcao = 0 

# Laço condicional
while opcao != 4: # Enquanto a "opcao" for diferente de 4, continue rodando
  print("1 - Rodar funcionalidade 1")
  print("2 - Rodar funcionalidade 2")
  print("3 - Rodar funcionalidade 3")
  print("4 - Sair do sistema")

  # Pede ao usuário para selecionar a opção
  opcao = int(input("Informe a opção desejada: "))

  # Verifica qual opção foi escolhida
  if opcao == 1:
    print("Executando a funcionalidade 1")

  elif opcao == 2:
    print("Executando a funcionalidade 2")

  elif opcao == 3:
    print("Executando a funcionalidade 3")

  elif opcao == 4:
    print("Saindo do sistema...")
    
  else:
    print("Opção inválida!")