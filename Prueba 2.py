#Definicion Funcion Mochila
def Mochila(elementos, capacidad):
    #definicion de las variables
    n = len(elementos)
    #se inicializa una matriz para almacenar los valores maximos y donde dp representa el valor maximo
    dp = [[0] * (capacidad + 1) for _ in range(n+1)]
    print("dp1", dp)
    
    #se realiza el llamado a la matriz
    for i in range(1, n + 1):
        for j in range(1, capacidad + 1):
            # si el elemento actual excede la capacidad maxima no se incluira el 
            #elemento en la mochila
            if elementos[i- 1][0] > j:
                dp[i][j] = dp[i-1][j]
            else:
                #se consideran ambos casos el de agregarlo o no agregarlo a la mochila
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-elementos[i-1][0]] + elementos[i-1][1])
    
    #Construcion de los elementos seleccionados
    items_seleccionados=[]
    i = n
    j = capacidad
    while i > 0 and j > 0:
        if dp[i][j] != dp[i-1][j]:
            items_seleccionados.append(elementos[i-1])
            j = elementos[i-1][0]
        i -= 1
        #retorna valor maximo y los elementos seleccionados
    print("capacidad",dp)
    print("items", items_seleccionados)
    return dp[n][capacidad], items_seleccionados # retorna la capacidad junto a los valores maximos y la mejor combinacion segun los elementos
    #seleccionados

#ejemplo de uso
elementos= [(2,3),(3,4),(4,5),(5,6)] #elemntos o combinaciones
capacidad= 8 # capacidad de la mochila
valores_maximos, items_seleccionados = Mochila(elementos, capacidad)
print("valores maximos",valores_maximos)
print("combinacion seleccionada",items_seleccionados)



