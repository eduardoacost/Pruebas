#Definicion de la clase ajedrez
class Ajedrez:
    #Constructor de la clase
    def __init__ (self, n):
        #Variables Inicializada
        self.n = n #tamaño del tablero 
        self.tablero = [[0]*n for _ in range(n)] #Inicializar una matriz en 0 para el tableros
    
    def es_seguro( self, row ,col):
        #es_seguro es un metodo para verficar si hay una reina en diferentes posiciones

        for i in range(row):
            if self.tablero[i][col] == 1: #es para verficiar si hay una reina en la columna
                return False
            
        for i, j in zip(range(row , -1 , -1),range(col ,-1 ,-1)):
            if self.tablero[i][j] == 1: #Verifica si hay una reina en la esquina diagonal superior Izquierda
                return False 

        for i ,j  in zip(range(row, -1,-1), range(col,self.n)): 
            if self.tablero[i][j] == 1: #Verfica si hay una reina en la esquina superior derecha
                return False
        print("se han verificado las posiciones de las reinas")
        return True
    
                    
    def reinas(self, row):
        #metodo para resolver el problema de las reinas
        if row >= self.n: #caso para saber si hay reinas en el tablero 
            return True
        
        #iterar todas las columnas en las filas actuales
        for col in range(self.n):
            if self.es_seguro(col, row):
                #si es seguro se coloca una reina en esa posicion como un 1
                self.tablero[row][col] = 1
                if self.reinas(row + 1):#para llamar a la siguiente reina 
                    print("se verifico si hay reynas se colocara en esta posicion")
                    return True
                
                self.tablero[row][col] = 0 #si verifica que no es seguro lo que realiza es colocar a la reina en esta posicion
            print("nose pudo colocar ninguna reina")
        return False #si no se puede colocar ninguna reina esto retornoara false
    
    def solu_ajedrez(self):
        #imprime la solucion del tablero que se define
        for row in (self.tablero):
            
            print("".join(map(str, row)))#Se imprime cada fila del tablero



def ajedrez_fin():
    print("iniciando")
    #funcion Principal
    n=(int(input("Colocar el tamaño del tablero")))
    n_ajedrez = Ajedrez(n) #se cra una instancia 
    if n_ajedrez.reinas(0):
        #si se encuentra una solucion imprime el tablero de la solucion
        print("Solucion encontrada")
        n_ajedrez.solu_ajedrez()
    else:
        print("nose encontro una solucion")



ajedrez_fin() # se llama la funcion






 
                    

             