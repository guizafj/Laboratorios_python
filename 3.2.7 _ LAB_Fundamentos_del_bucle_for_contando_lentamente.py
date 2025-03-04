import time

# Escribe un bucle for que cuente hasta cinco.
for nl_conteo in range(1, 6):
    print(nl_conteo, "Mississippi")# Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
    # Cuerpo del bucle, emplea : time.sleep(1)
    time.sleep(1)

# Escribe una función print con el mensaje final.
print("Lista o no, aquí vengo!")

# 3.2.9   LAB   La sentencia break - atrapado en un bucle

ng_contador = 0 # se define una variable para guardar en la memoria los datos ingresados

while True:
    sg_usuario = input("ingresa una palabra: ")
    if sg_usuario == "chupacabra":
        break
    ng_contador += 1

print("Has dejado el bucle con éxito.")

for i in range(0, 11): # bucle de 0 a 10
    if i % 2 != 0: # identifica los impares y 
        print(i)   # los imprime en pantalla

ng_x = 1
while ng_x < 11: # se crea un bucle que cuenta hasta 10
    if ng_x % 2 != 0: # identifica los impares
        print(ng_x) # imprime los numeros identificados
    ng_x += 1 # almacena el nuevo valor en la variable declarada

for sl_ch in "john.smith@pythoninstitute.org": # se da una cadena predefinida
    if sl_ch == "@": # se condiciona la lectura de la cadena
        break # para cuando encuentra el signo o letra designado
    print(sl_ch, end="") # imprime el resultado hasta donde se ejecuta el programa

####

for nl_digit in "0165031806510": # definicion del bucle
    if nl_digit == "0": # se condiciona la ejecución del bucle
       print("x", end=" ") # se realiza la inclusion de la "x"
       continue # por medio de continue se evita el "0"
    print(nl_digit, end=" ") # imprime la nueva cadena que se encuentra en el bucle for

#####
        
ng_n = 3
while ng_n > 0:
    print(ng_n + 1)
    ng_n -= 1 # cuenta atras condicionada por la concatenación
else:
    print(ng_n)

####

ng_n = range(4) # se declara el range antes del bucle for
 
for nl_num in ng_n: # se invoca la variable que coniene el range
    print(nl_num - 1) # se imprime el valor incial dado a la variable de control
else:
    print(nl_num)  # se imprime el bucle hasta llegar al valor dado en la variable range