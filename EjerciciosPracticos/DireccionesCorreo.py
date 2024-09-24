"""
GENERAR X CANTIDAD DE CORREOS NUMERADOS CON TU NOMBRE
"""
nombre = input("Introduce tu nombre: ")
cantidad = int(input("Cuantos correos electronicos necesitas:" ))



for i in range(cantidad):
      print(f"{nombre}{i}@gmail.com")
                     
