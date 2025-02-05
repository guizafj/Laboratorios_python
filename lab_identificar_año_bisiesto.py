## Calcular si es año bisiesto o no 

year = int(input("Introduce un año: "))

if year < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:      
    if year % 4 != 0: # Se divide en 4 y se usa el != para evitar que el resultado sea 0.
         print(year, "es un año común")
    elif year % 100 !=0: # En caso de que el resultado sea 0 el programa se detiene.
         print(year, "es un año bisiesto")
    elif year % 400 != 0:
        print(year, " es un año común")
    else:
         print(year, "es un año bisiesto")


    
