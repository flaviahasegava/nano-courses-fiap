# FUNÇÕES (MODULARIZAÇÃO)
# Chamar funções de outro arquivo

# "import" -> buscar recursos que não estão dentro desse arquivo que está aberto
import calculos

# Aqui está dizendo para o python que o arquivo "import calculos" é um arquivo externo e que ele procure uma função dentre dele chamada "somar()", passando dois valores
print(calculos.somar(1, 2))

# Outra forma de realizar a importação (importar direto as funções e não o arquivo inteiro)
from calculos import somar, subtrair, dividir, multiplicar # Dentro do arquivo "calculos", importa a função somar
print(somar(1, 2))
print(subtrair(6, 2))

# VANTAGENS DA MODULARIZAÇÃO
# - Poder de manutenção, caso queira mudar algum comportamento, basta que altere na função e não em cada uma das chamadas
# - Organização