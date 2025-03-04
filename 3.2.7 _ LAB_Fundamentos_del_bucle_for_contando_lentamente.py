import time

# Escribe un bucle for que cuente hasta cinco.
for conteo in range(1, 6):
    print(conteo, "Mississippi")# Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
    # Cuerpo del bucle, emplea : time.sleep(1)
    time.sleep(1)

# Escribe una función print con el mensaje final.
print("Lista o no, aquí vengo!")

# 3.2.9   LAB   La sentencia break - atrapado en un bucle

contador = 0 # se define una variable para guardar en la memoria los datos ingresados

while True:
    usuario = input("ingresa una palabra: ")
    if usuario == "chupacabra":
        break
    contador += 1

print("Has dejado el bucle con éxito.")

for i in range(0, 11): # bucle de 0 a 10
    if i % 2 != 0: # identifica los impares y 
        print(i)   # los imprime en pantalla

x = 1
while x < 11: # se crea un bucle que cuenta hasta 10
    if x % 2 != 0: # identifica los impares
        print(x) # imprime los numeros identificados
    x += 1 # almacena el nuevo valor en la variable declarada

for ch in "john.smith@pythoninstitute.org": # se da una cadena predefinida
    if ch == "@": # se condiciona la lectura de la cadena
        break # para cuando encuentra el signo o letra designado
    print(ch, end="") # imprime el resultado hasta donde se ejecuta el programa

####

for digit in "0165031806510": # definicion del bucle
    if digit == "0": # se condiciona la ejecución del bucle
       print("x", end=" ") # se realiza la inclusion de la "x"
       continue # por medio de continue se evita el "0"
    print(digit, end=" ") # imprime la nueva cadena que se encuentra en el bucle for

#####
        
n = 3
while n > 0:
    print(n + 1)
    n -= 1 # cuenta atras condicionada por la concatenación
else:
    print(n)

####

n = range(4) # se declara el range antes del bucle for
 
for num in n: # se invoca la variable que coniene el range
    print(num - 1) # se imprime el valor incial dado a la variable de control
else:
    print(num)  # se imprime el bucle hasta llegar al valor dado en la variable range