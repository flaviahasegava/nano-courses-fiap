import os
os.system("cls")

# CONDIÇÃO IF ENCADEADO - Um if dentro de outro if

# Exercício
'''
  Uma universidade realizará uma competição acadêmica. Para esta competição, só serão aceitos estudantes que sejam maiores de idade.
  
  Crie um programa que receba o RM e a idade de um aluno, e exiba uma mensagem confirmando o cadastro apenas caso o estudante seja maior de idade. 
  
  Caso um aluno seja menor e informe ter autorização dos pais, o cadastro deve ser realizado e o email deve ser enviado para os responsáveis. 
  
  Caso contrário, o cadastro não será feito.
'''

# Pedir o RM do aluno(a)
rm_aluno = input("Olá, aluno(a)! Por favor, insira o seu RM: ")

# Pedir a idade do aluno(a)
idade = int(input("Por favor, insira sua idade: "))

# Verifica se o aluno(a) é maior de idade
if idade >= 18:
  print(f"RM{rm_aluno}, seu cadastro foi realizado com sucesso!")
  print("Mais informações serão enviadas para o seu e-mail cadastrado.")

else:
# Pedir a autorização de um responsável
  autorizacao = input("Você tem autorização de um responsável? (S/N) ")

  # Verifica se o aluno(a) tem a autorização de um responsável
  if autorizacao == "S":
    print(f"RM{rm_aluno}, seu cadastro foi realizado com sucesso!")
    print("Mais informações serão enviadas para o e-mail do responsável.")

# Exibe ao aluno(a) que não pode se cadastrar por ter menos de 18 anos e não possui autorização de um responsável
  else:
    print(f"RM{rm_aluno}, não é possível realizar o cadastro, pois você ainda é menor de idade e não tem autorização de um responsável.")