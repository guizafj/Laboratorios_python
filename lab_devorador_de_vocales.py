# Indicar al usuario que ingrese una palabra
usuario = input("ingresa una palabra: ")
word_without_vowels = "" # uso de una cadena vacia para asignarle las letras no devoradas por el programa
# y asignarlo a la variable user_word.
user_word = usuario
user_word = user_word.upper()

for letter in user_word:  
# Completa el cuerpo del bucle for.
    if letter == "A": # lee la cadena y si encuenta una A no la tiene en cuenta
        continue
    elif letter == "E":
        continue
    elif letter == "U":
        continue
    elif letter == "O":
        continue
    elif letter == "I":
        continue
          
    else:     
        word_without_vowels += letter # se asignan las letras no consumidas en el ciclo for a la variable
                                        # se usa la operación de concatenación
        print(letter) # imprime las letras que no son vocales en cada linea

print("Palabra sin vocales: ", word_without_vowels) # imprime las letras recogidas en la variable vacia
        
        
