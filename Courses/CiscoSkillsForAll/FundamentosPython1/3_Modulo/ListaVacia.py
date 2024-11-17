# Creando una lista vacia y llenandola con append()
# Cada elemento se agregara al final de la lista
my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.append(i + 1)

print(my_list)

# Creando una lista vacia y llenandola con inert()
# Todos los valores se iran agregando en la posicion 0 y los demas elementos
# Se iran recorriendo de lugar
my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)

