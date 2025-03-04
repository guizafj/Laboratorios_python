ng_blocks = int(input("Ingresa el número de bloques: "))
ng_height = 0

for i in range(ng_blocks):
    if ng_blocks <= 0:
        break       
    elif ng_blocks != 0: # Si consideramos la pirámide como una progresión aritmética, y el total de bloques como la
         # suma de la progresión, a partir de la expresión de la suma de los términos de la progresión: Sn = n(a1+an)/2
        ng_height = int(((1 + 8 * ng_blocks) ** .5 -1 ) // 2)  # haciendo a1 = 1 y an = n, despejando n se obtien la expresion del inicio 
else:
    print("La altura de la pirámide: ", ng_height)

