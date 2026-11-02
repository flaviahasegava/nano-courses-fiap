# TUPLAS
# Tupla é o mesmo que lista, porém são imutáveis, diferente das listas que são mutáveis (flexível, adicionar, remover ou alterar)
# É usado "()" e não "[]"
# As listas consomem mais memória e são mais lentas, já as tuplas são rápidas e consomem menos memória 
# Usados em: registos estáticos, coordenadas, dados protegidos ou retornos múltiplos de funções. Quando não é preciso modificar nada

# MEDIR A QUANTIDADE DE MEMÓRIA OCUPADA POR UM OBJETO EM PYTHON (TAMANHO EM BYTES)
import sys # Importa a biblioteca sys

# Medir tipos primitivos
print(sys.getsizeof(0))          # 28 bytes
print(sys.getsizeof(100))        # 28 bytes
print(sys.getsizeof("Olá"))      # 54 bytes

# Comparar Lista vs Tupla com os mesmos elementos
lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)

print(sys.getsizeof(lista))      # ~104 bytes (reserva espaço extra para expansão)
print(sys.getsizeof(tupla))      # ~80 bytes (é imutável, por isso usa menos memória)