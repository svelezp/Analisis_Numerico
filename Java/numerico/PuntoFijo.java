 

import java.math.BigDecimal;
import java.util.ArrayList;

import com.ezylang.evalex.Expression;
import com.ezylang.evalex.data.EvaluationValue;

import co.com.quipux.qxgenericbean.QxGenericBean;

public class PuntoFijo {

    public static QxGenericBean puntoFijo(String funcion, String funcionG, BigDecimal x0, BigDecimal tol, int maxIter) throws Exception {
        
        QxGenericBean tabla = new QxGenericBean();

        Expression func = new Expression(funcion);
        Expression funcG = new Expression(funcionG);
        EvaluationValue fx0 = null;
        EvaluationValue gx0 = null;
        BigDecimal xm = BigDecimal.ZERO;
        BigDecimal error = tol.add(BigDecimal.ONE);
        tabla.setValue("FILAS", new ArrayList<>());
        tabla.setValue("COLUMNAS", "ITERACION, G(X), F(G(X)), ERROR");

        fx0 = func.with("x", x0).evaluate();
        int iteracion = 0;
        while(fx0.getNumberValue().compareTo(BigDecimal.ZERO) != 0 && error.compareTo(tol) > 0 && iteracion < maxIter){
            QxGenericBean fila = new QxGenericBean();
            xm = funcG.with("x", x0).evaluate().getNumberValue();
            fx0 = func.with("x", xm).evaluate();
            
            error = xm.subtract(func.with("x", x0).evaluate().getNumberValue()).abs();

            fila.setValue("ITERACION", String.valueOf(iteracion));
            fila.setValue("G(X)", String.valueOf(xm.doubleValue()));
            fila.setValue("F(G(X))", String.valueOf(fx0.getNumberValue().doubleValue()));
            fila.setValue("ERROR", String.valueOf(error.doubleValue()));
            tabla.getListQxBean("FILAS").add(fila);

            x0 = xm;

            iteracion++;
        }
        tabla.setValue("MAX_ITERACION", iteracion-1);
        if (fx0.getNumberValue().abs().compareTo(BigDecimal.ZERO) == 0) {
            tabla.setValue("MENSAJE", "El valor " + xm.toString() + " es una raíz");
            return tabla;
        } else if (error.abs().compareTo(tol) < 0) {
            tabla.setValue("MENSAJE", "No se ha logrado encontrar una raíz exacta dentro de la tolerancia seleccionada. El valor " + fx0 + " es el más aproximado");
            return tabla;
        } else {
            tabla.setValue("MENSAJE", "Se ha fallado en " + iteracion + " iteraciones");
            return tabla;
        }
    }

    public static void main(String[] args) {
        try {
            Tabla.imprimir(puntoFijo("e^(x-10)+sin(x)", "e^(x-10)++sin(x)-x", BigDecimal.ZERO, new BigDecimal("0.00000000000005"), 30));
        } catch (Exception e) {
            System.err.println(e);
        }
    }
}