secret_number = 777
usuario = int(input(
    """
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
ingresa tu opción aqui: """)
)
#cuando coincide el numero ingresado por el definido detiene el programa
while usuario != 777: # se usa != para obtener una respuesta false 
    if usuario != secret_number: # si no coincide imprime y solicita un nuevo numero
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    usuario = int(input("intentalo de nuevo: ")) # si al ingresar un numero coincide con el predeterminado
                                                # detiene salta el bucle y ejecuta la siguiente orden

print("¡Bien hecho, muggle! Eres libre ahora.")
