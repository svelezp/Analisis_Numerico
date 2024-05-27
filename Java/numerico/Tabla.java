package numerico.src.main.java.com.numerico.app;

import java.util.ArrayList;
import java.util.HashMap;
import com.ezylang.evalex.Expression;
import com.ezylang.evalex.data.EvaluationValue;
import java.math.BigDecimal;

import co.com.quipux.qxgenericbean.QxGenericBean;

public class Tabla {

    public static void imprimir(QxGenericBean tabla){
        
        String[] columnas = tabla.getString("COLUMNAS").split(", ");
        StringBuilder formatoImpresion = new StringBuilder();
        QxGenericBean lastFila = tabla.getListQxBean("FILAS").get(tabla.getInt("MAX_ITERACION"));
        
        formatoImpresion.append("\n");
        for (String columna : columnas){
            if (lastFila.getString(columna).length() < columna.length()) {
                formatoImpresion.append(" | %" + columna.length() + "s" );
            } else {
                formatoImpresion.append(" | %" + (lastFila.getString(columna).length()+4+ "s" ));
            }
        }
        formatoImpresion.append("\n");

        System.out.printf(formatoImpresion.toString(), (Object[]) columnas);
        String[] valores = new String[columnas.length];
        for (QxGenericBean fila : tabla.getListQxBean("FILAS")) {
            int i = 0;
            while (i < columnas.length){
                valores[i] = fila.getString(columnas[i]);
                i++;
            }
            System.out.printf(formatoImpresion.toString(), (Object[]) valores);
        }
        System.out.println(tabla.getString("MENSAJE"));
    }

}
