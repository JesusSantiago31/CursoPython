"""
GENERAR X CANTIDAD DE CORREOS NUMERADOS CON TU NOMBRE
"""
nombre = input("Introduce tu nombre: ")
cantidad = int(input("Cuantos correos electronicos necesitas:" ))
correos = ""
for i in range(cantidad):
  correos += f"{nombre}{i}@gmail.com \n"
  archivo = open("correos.txt","a")
  archivo.write(correos)
  archivo.close()
        
                     
