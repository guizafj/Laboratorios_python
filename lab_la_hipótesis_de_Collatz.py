# Solicita el ingreso de un numero
c0 = int(input("ingresa un numero: "))
pasos = 0 # se declara una variable de conteo

while c0 != 0:   # se da inicio al bucle
    if c0 <= 0: # se condiciona el inicio del bucle o se detiene
        break   
    elif (c0 % 2) == 0:    # se verifica si es par
       print(c0, " es par")
       c0 = int(c0 // 2)
       pasos += 1
    elif c0 <= 1:
        break     

    elif (c0 % 2) == 1:  # se verifica si es impar
        print(c0, " es impar")
        c0 = int(3 * c0 + 1)  
        pasos += 1
    elif c0 <= 1:
        break          
       
print("pasos = ", pasos)
    