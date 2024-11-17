#Sintaxis de un bucle WHILE
while conditional==True:
  instruccion

#Ejemplo de un bucle infinito
while True:
    print("Estoy atrapado dentro de un bucle.")

#Ejemplo para salir de un bucle
counter = 5
while counter != 0:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)

#Sintaxis de un bucle FOR
for i in range(100):
    # do_something()
    pass
  
for i in range(10):
    print("El valor de i es", i)
        
#La funcion range puede tener dos argumentos
for i in range(2, 8):
    print("El valor de i es", i)

#Con tres argumentos, el tercer argumento es el incremento
for i in range(2, 8, 3):
    print("El valor de i es", i)
#El bucle no tendra Output
for i in range(1, 1):
    print("El valor de i es", i)



