i = 15
j = 22
# A representacion de 32 bits
# i: 00000000000000000000000000001111
# j: 00000000000000000000000000010110 

bit = i & j
# bit = 00000000000000000000000000000110

bitneg = ~i
# bitneg = 11111111111111111111111111110000

### Operadores bit a bit de forma abreviada
x &= y
x |= y
x ^= y
