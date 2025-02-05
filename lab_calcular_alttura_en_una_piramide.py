blocks = int(input("Ingresa el número de bloques: "))
height = 0

for i in range(blocks):
    if blocks <= 0:
        break       
    elif blocks != 0: # Si consideramos la pirámide como una progresión aritmética, y el total de bloques como la
         # suma de la progresión, a partir de la expresión de la suma de los términos de la progresión: Sn = n(a1+an)/2
        height = int(((1 + 8 * blocks) ** .5 -1 ) // 2)  # haciendo a1 = 1 y an = n, despejando n se obtien la expresion del inicio 
else:
    print("La altura de la pirámide: ", height)

