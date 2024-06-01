import java.math.BigDecimal;
import java.math.MathContext;
import java.math.RoundingMode;
import java.util.ArrayList;

import javax.xml.namespace.QName;

import com.ezylang.evalex.Expression;
import com.ezylang.evalex.data.EvaluationValue;

import co.com.quipux.qxgenericbean.QxGenericBean;

public class GaussSimple {

    public static QxGenericBean gaussSimple(BigDecimal[][] A, BigDecimal[] b) throws Exception {

        QxGenericBean tabla = new QxGenericBean();
        tabla.setValue("ITERACIONES", new ArrayList<>());
        QxGenericBean iteracion;
        BigDecimal pivote = null;
        BigDecimal mult = null;
        BigDecimal sum = BigDecimal.ZERO;
        StringBuilder result = new StringBuilder();
        MathContext math = new MathContext(150, RoundingMode.HALF_DOWN);

        int n = b.length-1;
        BigDecimal[] x = new BigDecimal[n+1];
        int etapa = 0;
        for (int i = 0; i <= n; i++){
            pivote = A[i][i];
            System.out.println(String.valueOf(pivote.doubleValue()));
            if (pivote.compareTo(BigDecimal.ZERO) != 0){
                for(int j = i+1; j <= n; j++){
                    mult = A[j][i].divide(pivote, math);
                    for (int a = 0; a <= n; a++){
                        A[j][a] = A[j][a].subtract(mult.multiply(A[i][a], math), math);
                    }
                    b[j] = b[j].subtract(mult.multiply(b[i], math), math);
                    iteracion = new QxGenericBean();
                    iteracion.setValue("A", A);
                    iteracion.setValue("b", b);
                    iteracion.setValue("NRO_ETAPA", etapa);
                    tabla.getListQxBean("ITERACIONES").add(iteracion);    
                    etapa++;                
                }
            } else {
                return null;
            }
        }

        x[n] = b[n].divide(A[n][n], math);

        for (int i = n; i >= 0; i--){
            sum = BigDecimal.ZERO;
            for (int j = i+1; i > n; i++){
                sum = A[i][j].multiply(x[j], math);
            }
            x[i]=(b[i].subtract(sum, math).divide(A[i][i], math));
            result.append("x"+(i+1)+": "+x[i].toString() + " ");
        }
        tabla.setValue("RESULTADOS", result.toString());
        return tabla;
    }

    public static void main(String[] args) {
        try {
            Tabla.imprimirMatriz((gaussSimple(Matriz.leerMatriz("25, -3, 4, -7\n 6, 42, -7, 9\n 5, 12, -73, 8\n 2, -7, 13, -95"), Matriz.leerVector("8\n 21\n 19\n -25"))));
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
