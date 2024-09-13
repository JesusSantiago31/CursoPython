## ¿Que imprime el siguiente fragmento de codigo?
lst = [1, 2, 3, 4, 5] # Lista
lst.insert(1, 6) # Se agrega el numero 6 en la posicion 1 de lst
del lst[0] # Elimina el elemento 0 de lst
lst.append(1) # Agrega el numero 1, al final de la lista

print(lst) # Imprime la lista
# [6, 2, 3, 4, 5, 1]

## ¿Que imprime el siguiente fragmento de codigo?
lst = [1, 2, 3, 4, 5] # Lista
lst_2 = [] # Lista 2
add = 0 # Variable

for number in lst:  # Ciclo for que tomara los numero de lst
    add += number # Suma los numeros que tiene lst 
    lst_2.append(add) # Coloca la suma al final de la lista

print(lst_2) # Imprime lst2
# ¿Cuál es el resultado del siguiente fragmento de código?
lst = [] # Lista
del lst # Eliminacion de lst
print(lst) #Imprimir lst (Ya no existe en los registros)
# NameError: name 'lst' is not defined

# ¿Cuál es el resultado del siguiente fragmento de código?
lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))



