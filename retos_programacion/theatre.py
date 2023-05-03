"""Theatre Square en la ciudad capital de Berland tiene una forma rectangular con el tamaño n  ×  m metros.
 Con motivo del aniversario de la ciudad, se decidió pavimentar la Plaza con losas cuadradas de granito. 
 Cada losa tiene el tamaño a  ×  a .

¿Cuál es el menor número de losas necesarias para pavimentar la plaza?
Se permite cubrir una superficie más grande que la Plaza del Teatro,
pero la Plaza tiene que ser cubierta. No está permitido romper las losas.
Los lados de las losas deben ser paralelos a los lados del Cuadrado."""

#  auhtor: wil_aldana
#  created: 29/03/23 00:43:56
#  complexity: O()
n, m, a = map(int, input().split())

# Calcular el número de losas necesarias en cada dimensión
num_tiles_n = -(-n // a)  # división entera redondeando hacia arriba
num_tiles_m = -(-m // a)

# Calcular el número total de losas necesarias
num_tiles = num_tiles_n * num_tiles_m

print(num_tiles)
