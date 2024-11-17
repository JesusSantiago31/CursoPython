#EL desplazamient de bits es como multiplicar y dividir
# 1234 * 10 12340  Dessplazamiento a la Izquierda
# 12340 / 10 = 1234   Desplazamiento a la Derecha
# En Python es multiplicar y dividir por 2

# Simbolos de desplazamiento en Python 
#  valor << bits
#  valor >> bits 
var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)

# 17 >> 1 → 17 // 2 (17 dividido entre 2 a la potencia de 1) → 8 (desplazarse hacia la derecha en un bit equivale a la división entera entre dos)
# 17 << 2 → 17 * 4 (17 multiplicado por 2 a la potencia de 2) → 68 (desplazarse hacia la izquierda dos bits es lo mismo que multiplicar números enteros por cuatro)
