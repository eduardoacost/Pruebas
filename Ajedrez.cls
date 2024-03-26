public class Ajedrez {
	//Definimos la variable
	private Integer n;
   	List<List<integer>>  tablero;
    public Integer i;
    public Integer j;
    //Constructor
    public Ajedrez(Integer n){
        this.n = n;
        tablero[n] = new List<integer>();
        
    }
    
    public Boolean Solu(){
        return soluAjedrez(0);
    }
    
    private Boolean soluAjedrez(Integer row){
        if(row >= n){
            System.debug('Se encontro una solucion');
            return true; // Significa que llego al final esto quiere decir que si consiguo un final
            
        }
        for (Integer col = 0; col < n; col++){
            if(es_seguro(row,col)){
                tablero[row][col] = 1;
                if(soluAjedrez(row + 1)){
                    return true;
                }
                
                tablero[row][col] = 0;
            }
        }
        
        
        return false;// si no se encontro una solucion
        
    }
    private Boolean es_seguro(Integer row, Integer col){
        for(Integer i = 0; i < row; i++){
            if(tablero[i][col] == 1){
               return false; 
            }            
        }
        for(Integer i = row; i >= 0; i--){
            for(Integer j = col; j >= 0; j--){
                 if(tablero[i][j] == 1){	//#Verifica si hay una reina en la esquina diagonal superior Izquierda
                return false; 
            }
           
            }
              
        }
         for(Integer i = row; i >= 0; i--){
            for(Integer j = col; j >= 0; j++){
                 if(tablero[i][j] == 1){	//#Verfica si hay una reina en la esquina superior derecha
                return false; 
            }
           
            }
              
        }
        return true;
    }
    public void impriAjedrez(){
        for(Integer i = 0; i < n; i++){
            String row = ''; //correccion creando con string vacio
                for(Integer j = 0; j < n; j++){
                    row += tablero[i][j] + ''; //concatena
                }
            System.debug(row);// imprime la fila del tablero
        }
    }
}