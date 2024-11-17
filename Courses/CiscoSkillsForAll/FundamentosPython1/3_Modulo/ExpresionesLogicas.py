var=1
# Ejemplo 1:
print(var > 0)
print(not (var <= 0))


# Ejemplo 2:
print(var != 0)
print(not (var == 0))

#Leyes de De Morgan. Dicen que:
#La negación de una conjunción es la separación de las negaciones.
#La negación de una disyunción es la conjunción de las negaciones.
not (p and q) == (not p) or (not q)
not (p or q) == (not p) and (not q)

