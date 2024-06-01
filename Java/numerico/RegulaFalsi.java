 

import java.math.BigDecimal;
import java.util.ArrayList;

import com.ezylang.evalex.Expression;
import com.ezylang.evalex.data.EvaluationValue;

import co.com.quipux.qxgenericbean.QxGenericBean;

public class RegulaFalsi {

    public static QxGenericBean regulaFalsi(String funcion, BigDecimal x0, BigDecimal x1, BigDecimal tol) throws Exception {
        
        QxGenericBean tabla = new QxGenericBean();

        Expression func = new Expression(funcion);
        Expression next = new Expression("x0 - ((y0 * (x0 - x1)) / (y0 - y1))");
        EvaluationValue fx0 = null;
        EvaluationValue fx1 = null;
        EvaluationValue fxm = null;
        BigDecimal xm = null;
        BigDecimal xma = null;
        BigDecimal xf = null;
        BigDecimal error = null;
        tabla.setValue("FILAS", new ArrayList<>());
        tabla.setValue("COLUMNAS", "ITERACION, XI, XU, XR, F(XR), ERROR");

        fx0 = func.with("x", x0).evaluate();
        fx1 = func.with("x", x1).evaluate();

        if (fx0.getNumberValue().multiply(fx1.getNumberValue())
                .compareTo(BigDecimal.ZERO) > 0) {
            tabla.setValue("MENSAJE", "Rango invalido, no cruza el eje x");
            return tabla;
        } else if (fx0.getNumberValue().compareTo(BigDecimal.ZERO) == 0){
            tabla.setValue("MENSAJE", "El valor " + x0.toString() + " es una raíz");
            return tabla;
        } else if (fx1.getNumberValue().compareTo(BigDecimal.ZERO) == 0){
            tabla.setValue("MENSAJE", "El valor " + x1.toString() + " es una raíz");
            return tabla;
        } else {
            xm = x0;
            fxm = func.with("x", xm).evaluate();
            int iteracion = 0;
            while(fxm.getNumberValue().abs().compareTo(tol) > 0 && fxm.getNumberValue().compareTo(BigDecimal.ZERO) != 0){
                QxGenericBean fila = new QxGenericBean();
                xma = xm;

                xm = next.with("x0", x0).and("x1", x1).and("y0", fx0).and("y1", fx1).evaluate().getNumberValue();
                fxm = func.with("x", xm).evaluate();

                xf = xm;
                error = fxm.getNumberValue().subtract(func.with("x", xma).evaluate().getNumberValue()).abs();

                fila.setValue("ITERACION", String.valueOf(iteracion));
                fila.setValue("XI", String.valueOf(x0.doubleValue()));
                fila.setValue("XU", String.valueOf(x1.doubleValue()));
                fila.setValue("XR", String.valueOf(xm.doubleValue()));
                fila.setValue("F(XR)", String.valueOf(fxm.getNumberValue().doubleValue()));
                fila.setValue("ERROR", String.valueOf(error.doubleValue()));
                tabla.getListQxBean("FILAS").add(fila);

                if (fx0.getNumberValue().multiply(fxm.getNumberValue()).compareTo(BigDecimal.ZERO) < 0){
                    x1 = xm;
                } else {
                    x0 = xm;
                }

                iteracion++;
            }
            tabla.setValue("MAX_ITERACION", iteracion-1);
            if (fxm.getNumberValue().abs().compareTo(BigDecimal.ZERO) == 0) {
                tabla.setValue("MENSAJE", "El valor " + xm.toString() + " es una raíz");
                return tabla;
            } else if (fxm.getNumberValue().abs().compareTo(tol) < 0) {
                tabla.setValue("MENSAJE", "No se ha logrado encontrar una raíz exacta dentro de la tolerancia seleccionada. El valor " + xf + " es el más aproximado");
                return tabla;
            } else {
                tabla.setValue("MENSAJE", "Otro");
                return tabla;
            }
        }
    }

    public static void main(String[] args) {
        try {
            Tabla.imprimir(regulaFalsi("(x^3)+(4x^2)-10", new BigDecimal("1.00"), new BigDecimal("2.00"),
                new BigDecimal("0.00005")));
        } catch (Exception e) {
            System.err.println(e);
        }
    }
}
