 

import java.util.ArrayList;
import java.util.HashMap;
import com.ezylang.evalex.Expression;
import com.ezylang.evalex.data.EvaluationValue;
import java.math.BigDecimal;

import co.com.quipux.qxgenericbean.QxGenericBean;

public class Matriz {

    public static BigDecimal[][] leerMatriz(String matriz){

        int n = matriz.split("\n ").length;
        BigDecimal[][] A = new BigDecimal[n][n];

        int i = 0;
        for (String fila : matriz.split("\n ")) {
            int j = 0;
            for (String columna : fila.split(", ")) { 
                A[i][j] = new BigDecimal(columna);
                j++;
            }
            i++;
        }
        return A;

    }

    public static BigDecimal[] leerVector(String vector){

        int n = vector.split("\n ").length;
        BigDecimal[] A = new BigDecimal[n];

        int i = 0;
        for (String fila : vector.split("\n ")) {
            A[i] = new BigDecimal(fila);
            i++;
        }
        return A;

    }

    public static void imprimirMatriz(BigDecimal[][] A, BigDecimal b[]){

        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < A.length; j++) { 
                System.out.print(A[i][j].doubleValue() + " ");
            }
            System.out.println("| " + b[i].doubleValue());
            System.out.println();
        }
    }
}
