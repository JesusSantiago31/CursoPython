#    Las listas son un tipo de datos en Python  que se utiliza para almacenar multiples objetos
#    Es una coleccion ordenada y mutable de elementos separados por comas entre corchetes
my_list = [1, None, True, "Soy una cadena", 256, 0]

###          Indexar y Actualizar
my_list = [1, None, True, 'Soy una cadena', 256, 0]
print(my_list[3])  # output: Soy una cadena
print(my_list[-1])  # output: 0

my_list[1] = '?'
print(my_list)  # output: [1, '?', True, 'Soy una cadena', 256, 0]

my_list.insert(0, "primero")
my_list.append("último")
print(my_list)  # output: ['primero', 1, '?', True, 'Soy una cadena', 256, 0, 'último']

###         Las listas pueden estar anidads
my_list = [1, 'a', ["lista", 64, [0, 1], False]]

###         Eliminar elemento de lista y lista completa
my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list)  # output: [1, 2, 4]

del my_list  # borra la lista entera

###         Iteracion de lista con bucle for
my_list = ["blanco", "purpura", "azul", "amarillo", "verde"]

for color in my_list:
    print(color)

###         Verificar longitud de lista con len()
my_list = ["blanco", "purpura", "azul", "amarillo", "verde"]
print(len(my_list))  # output 5

del my_list[2]
print(len(my_list))  # output 4




