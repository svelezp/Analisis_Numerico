package numerico.src.main.java.com.numerico.app;

import java.util.ArrayList;
import java.util.HashMap;

public class Tabla {

    public void crearColumnas(String nombreColumnas){
        for (String columna : nombreColumnas.split(",")){
            Valor valor = new Valor("NNOMBRE_COLUMNA", columna);
            columnas.add(valor);
        }
    }

}
