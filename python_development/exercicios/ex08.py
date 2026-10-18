import os
os.system("cls")

# Exercício 08
'''
  Um grande cliente seu sofreu um ataque hacker: o servidor foi sequestrado por um software malicioso que criptografou todos os discos e pede a digitação de uma senha para a liberação da máquina. E é claro que os criminosos exigem um pagamento para informar a senha.

  Ao analisar o código do programa deles, porém, você descobre que a senha é composta pela palavra "LIBERDADE" seguida do fatorial dos minutos que a máquina estiver marcando no momento da digitação da senha (se a máquina estiver marcando 5 minutos, a senha será LIBERDADE120).

  Crie um programa que receba do usuário os minutos atuais e exiba na tela a senha necessária para desbloqueio.

  ATENÇÃO: seu programa não pode utilizar funções prontas para o cálculo do fatorial. Ele deve obrigatoriamente utilizar loop.
'''

# Pede ao usuário o tempo em minutos
minutos = int(input("Informe o número dos minutos do horário atual: "))

# Guarda o valor dos minutos na variável fatorial
fatorial = minutos

# Laço de repetição
for numero in range(1, minutos):
  # Calcula o fatorial
  fatorial = fatorial * numero

# Exibe a senha de acordo com os minutos
print(f"A senha é LIBERDADE{fatorial}")