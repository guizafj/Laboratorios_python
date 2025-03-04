# Solicita el ingreso de un numero
ng_c0 = int(input("ingresa un numero: "))
ng_pasos = 0 # se declara una variable de conteo

while ng_c0 != 0:   # se da inicio al bucle
    if ng_c0 <= 0: # se condiciona el inicio del bucle o se detiene
        break   
    elif (ng_c0 % 2) == 0:    # se verifica si es par
       print(ng_c0, " es par")
       ng_c0 = int(ng_c0 // 2)
       ng_pasos += 1
    elif ng_c0 <= 1:
        break     

    elif (ng_c0 % 2) == 1:  # se verifica si es impar
        print(ng_c0, " es impar")
        ng_c0 = int(3 * ng_c0 + 1)  
        ng_pasos += 1
    elif ng_c0 <= 1:
        break          
       
print("pasos = ", ng_pasos)
    