# Bloco if - Avalia uma condição e só realiza caso a condição seja verdadeira

# Exercícios
'''
    Uma universidade realizará uma competição acadêmica. Para esta competição, só serão aceitos estudantes que sejam maiores de idade.
    Crie um programa que receba o RM e a idade de um aluno, e exiba uma mensagem confirmando o cadastro apenas caso o estudante seja maior de idade.
'''

# Pedir o RM do aluno
rm_aluno = input("Olá, aluno(a)! Por favor, digite o seu RM: ")

# Pedir a idade do aluno
idade = int(input("Digite sua idade: "))

# Exibe a confirmação do cadastro, caso o estudante seja maior de idade
if idade >= 18:
    print(f"{rm_aluno}, seu cadastro foi confirmado com sucesso!")

# Exibe ao usuário que não pode se cadastrar por ter menos de 18
else:
    print("Não é possível realizar o seu cadastro, você ainda é menor de 18 anos.")
