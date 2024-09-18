# Como funcionan las listas
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

# El programa imprimira 2, debido a la forma de almacenar las variables ordinarias (escalares)
# -- el nombre de una variable ordinaria es el nombre de su contenido;
# -- el nombre de una lista es el nombre de una ubicación de memoria donde se almacena la lista.

#      SI MODIFICAMOS UNA LISTA, SE MODIFICARAN LAS DEMAS LISTAS QUE UTILICES LA LISTA MODIFICADA

# Rebanada
list_1 = [1]
list_2 = list_1[:] # Puede producri una lista completamente nueva
list_1[0] = 2
print(list_2)

# Formas mas generales de la rebanda
my_list[inicio:fin]

#Ejemplo


