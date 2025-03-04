# Indicar al usuario que ingrese una palabra
sg_usuario = input("ingresa una palabra: ")
sg_word_without_vowels = "" # uso de una cadena vacia para asignarle las letras no devoradas por el programa
# y asignarlo a la variable user_word.
sg_user_word = sg_usuario
sg_user_word = sg_user_word.upper()

for sl_letter in sg_user_word:  
# Completa el cuerpo del bucle for.
    if sl_letter == "A": # lee la cadena y si encuenta una A no la tiene en cuenta
        continue
    elif sl_letter == "E":
        continue
    elif sl_letter == "U":
        continue
    elif sl_letter == "O":
        continue
    elif sl_letter == "I":
        continue
          
    else:     
        sg_word_without_vowels += sl_letter # se asignan las letras no consumidas en el ciclo for a la variable
                                        # se usa la operación de concatenación
        print(sl_letter) # imprime las letras que no son vocales en cada linea

print("Palabra sin vocales: ", sg_word_without_vowels) # imprime las letras recogidas en la variable vacia
        
        
