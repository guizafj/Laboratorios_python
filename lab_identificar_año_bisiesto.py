## Calcular si es año bisiesto o no 

sg_year = int(input("Introduce un año: "))

if sg_year < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:      
    if sg_year % 4 != 0: # Se divide en 4 y se usa el != para evitar que el resultado sea 0.
         print(sg_year, "es un año común")
    elif sg_year % 100 !=0: # En caso de que el resultado sea 0 el programa se detiene.
         print(sg_year, "es un año bisiesto")
    elif sg_year % 400 != 0:
        print(sg_year, " es un año común")
    else:
         print(sg_year, "es un año bisiesto")


    
