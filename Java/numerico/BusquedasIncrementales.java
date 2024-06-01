import java.math.BigDecimal;
import java.util.ArrayList;

import com.ezylang.evalex.Expression;
import com.ezylang.evalex.data.EvaluationValue;

import co.com.quipux.qxgenericbean.QxGenericBean;

public class BusquedasIncrementales {

    public static QxGenericBean busquedasIncrementales(String funcion, BigDecimal x0, BigDecimal deltaX, int maxIter) throws Exception {
    
        QxGenericBean tabla = new QxGenericBean();

        BigDecimal x1;

        Expression func = new Expression(funcion);
        EvaluationValue fx0 = null;
        EvaluationValue fx1 = null;

        tabla.setValue("FILAS", new ArrayList<>());
        tabla.setValue("COLUMNAS", "ITERACION, XI, F(XI)");

        fx0 = func.with("x", x0).evaluate();

        QxGenericBean fila = new QxGenericBean();
        int iteracion = 0;
        fila = new QxGenericBean();
        fila.setValue("ITERACION", String.valueOf(0));
        fila.setValue("XI", x0.toString());
        fila.setValue("F(XI)", String.valueOf(fx0.getNumberValue().doubleValue()));
        tabla.getListQxBean("FILAS").add(fila);
        iteracion++;

        if (fx0.getNumberValue().compareTo(BigDecimal.ZERO) == 0){
            tabla.setValue("MENSAJE", "El valor " + x0.toString() + " es una raíz");
            return tabla;
        } else {
            x1 = x0.add(deltaX);
            fx1 = func.with("x", x1).evaluate();

            fila = new QxGenericBean();
            fila.setValue("ITERACION", String.valueOf(1));
            fila.setValue("XI", x1.toString());
            fila.setValue("F(XI)", String.valueOf(fx1.getNumberValue().doubleValue()));
            tabla.getListQxBean("FILAS").add(fila);

            iteracion++;
            
            do{
                fila = new QxGenericBean();

                x0 = x1;
                fx0 = fx1;
                x1 = x0.add(deltaX);
                fx1 = func.with("x", x1).evaluate();

                fila.setValue("ITERACION", String.valueOf(iteracion));
                fila.setValue("XI", x1.toString());
                fila.setValue("F(XI)", String.valueOf(fx1.getNumberValue().doubleValue()));
                tabla.getListQxBean("FILAS").add(fila);

                iteracion++;
            } while(fx0.getNumberValue().multiply(fx1.getNumberValue()).compareTo(BigDecimal.ZERO) > 0 && iteracion < maxIter);
            tabla.setValue("MAX_ITERACION", iteracion-1);
            if (fx1.getNumberValue().abs().compareTo(BigDecimal.ZERO) == 0) {
                tabla.setValue("MENSAJE", "El valor " + x1.toString() + " es una raíz");
                return tabla;
            } else if (fx0.getNumberValue().multiply(fx1.getNumberValue()).compareTo(BigDecimal.ZERO) < 0) {
                tabla.setValue("MENSAJE", "El intervalo [" + x0.toString() + ", " + x1.toString() + "] contiene al menos una raíz");
                return tabla;
            } else {
                tabla.setValue("MENSAJE", "La función falló en " + (iteracion-1) + " iteraciones");
                return tabla;
            }
        }
    }

    public static void main(String[] args) {
        try {
            Tabla.imprimir(busquedasIncrementales("(x^3)+x-6", new BigDecimal("0.00"), new BigDecimal("1.00"), 20));
        } catch (Exception e) {
            System.err.println(e);
        }
    }
}      