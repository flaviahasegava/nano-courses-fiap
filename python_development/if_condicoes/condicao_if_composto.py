import os
os.system("cls")

# CONDIÇÃO IF COMPOSTO - if e else(se e senão), verifica um e caso não seja exibe o outro

# Exercício
'''
  Uma universidade realizará uma competição acadêmica. Para esta competição, só serão aceitos estudantes que sejam maiores de idade.
  
  Crie um programa que receba o RM e a idade de um aluno, e exiba uma mensagem confirmando o cadastro apenas caso o estudante seja maior de idade.
'''

# Pedir o RM do aluno(a)
rm_aluno = input("Olá, aluno(a)! Por favor, insira o seu RM: ")

# Pedir a idade do aluno(a)
idade = int(input("Por favor, insira sua idade: "))

# Verifica se o aluno(a) é maior de idade e confirma o cadastro
if idade >= 18:
  print(f"RM{rm_aluno}, seu cadastro foi confirmado com sucesso!")

# Exibe ao aluno(a) que não pode se cadastrar por ter menos de 18 anos
else:
  print("Seu cadastro não pode ser concluído, você ainda é menor de 18 anos.")