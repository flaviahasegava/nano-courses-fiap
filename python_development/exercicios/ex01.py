import os
os.system("cls")

'''
  Verificar se os batimentos cardíacos por minuto se encontram na faixa adequada.

  Para isso, você deve solicitar que o usuário informe o seu número de BATIMENTOS POR MINUTO (BPM) e a IDADE.

  A partir disso o script deve verificar e exibir uma mensagem informando se os batimentos do usuário encontram-se DENTRO da faixa adequada, ACIMA da faixa adequada ou ABAIXO da faixa adequada, de acordo com o site "Tua Saúde" (https://www.tuasaude.com/frequencia-cardiaca/#:~:text=At%C3%A9%202%20anos%20de%20idade,idosos%3A%2050%20a%2060%20bpm](https://www.tuasaude.com/frequencia-cardiaca/#:~:text=At%C3%A9%202%20anos%20de%20idade,idosos%3A%2050%20a%2060%20bpm):

  IDADE                     BPM
  - Até 2 anos              120 a 140
  - De 8 anos até 17 anos   80 a 100
  - Adulto sedentário       70 a 80
  - Idosos                  50 a 60
'''

print("VERIFICADOR DE FREQUÊNCIAS CARDÍACAS")

# Pedir a idade e o BPM do paciente
idade = int(input("Por favor, informe a sua idade: "))
bpm = int(input("Por favor, informe o seu BPM: "))

# Verificar qual a faixa adequada do paciente

# ========================================
# Crianças até 2 anos
# ========================================
if idade <= 2 and bpm >= 120 and bpm <= 140:
  print("Batimentos NORMAIS para a idade fornecida.")

elif idade <= 2 and bpm < 120:
  print("Batimentos ABAIXO dos indicados para a idade.")

elif idade <= 2 and bpm > 140:
  print("Batimentos ACIMA dos indicados para a idade.")

# ========================================
# Jovens de 8 a 17 anos
# ========================================
elif idade >= 8 and idade <= 17 and bpm >= 80 and bpm <= 100:
  print("Batimentos NORMAIS para a idade fornecida.")

elif idade >= 8 and idade <= 17 and bpm < 80:
  print("Batimentos ABAIXO dos indicados para a idade.")

elif idade >= 8 and idade <= 17 and bpm > 100:
  print("Batimentos ACIMA dos indicados para a idade.")

# ========================================
# Adultos de 18 a 60 anos
# ========================================
elif idade >= 18 and idade <= 60 and bpm >= 70 and bpm <= 80:
  print("Batimentos NORMAIS para a idade fornecida.")

elif idade >= 18 and idade <= 60 and bpm < 70:
  print("Batimentos ABAIXO dos indicados para a idade.")

elif idade >= 18 and idade <= 60 and bpm > 80:
  print("Batimentos ACIMA dos indicados para a idade.")

# Exibe a mensagem de inválido caso a idade nào esteja dentro da faixa
else:
  print("Não existem dados para a idade indicada.")