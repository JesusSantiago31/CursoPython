#Mientras la palabra secreta no sea introducida, no se saldra del bucle
while True:
    secret_word = input("Ingresa una palabra: ")
    if secret_word == "chupacabra":
        break
    
print("Haz salido del bucle")

#Eliminar las vocales de una frase e imprimirlas en lineas distintas
# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.
user_word=input("Ingrese una palabra: ")
user_word = user_word.upper()

for letter in user_word:
    # Completa el cuerpo del bucle for.
    if letter in 'AEIOU':
        continue
    else:
        print(letter)
#Elimiar las vocales de una frase e imprimirlas en una sola linea

word_without_vowels = ""

# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.
user_word=input("Ingrese una palabra: ")
user_word = user_word.upper()


for letter in user_word:
    # Completa el cuerpo del bucle.
    if letter in 'AEIOU':
        continue
    else: 
        word_without_vowels += letter
        
print(word_without_vowels)
    
