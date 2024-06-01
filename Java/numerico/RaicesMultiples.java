import java.math.BigDecimal;
import java.util.ArrayList;

import com.ezylang.evalex.Expression;
import com.ezylang.evalex.data.EvaluationValue;

import co.com.quipux.qxgenericbean.QxGenericBean;

public class RaicesMultiples {

    public static QxGenericBean raicesMultiples(String funcion, String derivada, String segDeriv, BigDecimal x0, BigDecimal tol, int maxIter) throws Exception {
        
        QxGenericBean tabla = new QxGenericBean();

        Expression func = new Expression(funcion);
        Expression der = new Expression(derivada);
        Expression segDer = new Expression(segDeriv);
        EvaluationValue y0 = null;
        EvaluationValue d0 = null;
        EvaluationValue s0 = null;
        BigDecimal error = BigDecimal.ONE;
        BigDecimal x1;

        tabla.setValue("FILAS", new ArrayList<>());
        tabla.setValue("COLUMNAS", "ITERACION, XN, F(XN), F'(XN), F''(XN), ERROR");

        y0 = func.with("x", x0).evaluate();
        d0 = der.with("x", x0).evaluate();
        s0 = segDer.with("x", x0).evaluate();
        
        QxGenericBean fila = new QxGenericBean();

        fila.setValue("ITERACION", "0");
        fila.setValue("XN", String.valueOf(x0.doubleValue()));
        fila.setValue("F(XN)", String.valueOf(y0.getNumberValue().doubleValue()));
        fila.setValue("F'(XN)", String.valueOf(d0.getNumberValue().doubleValue()));
        fila.setValue("F''(XN)", String.valueOf(s0.getNumberValue().doubleValue()));
        fila.setValue("ERROR", "---");
        tabla.getListQxBean("FILAS").add(fila);

        Expression next = new Expression("x1 - ((y0*d0)/(d0^2-y0*s0))");
        
        int iteracion = 1;
        while(y0.getNumberValue().compareTo(BigDecimal.ZERO) != 0 && error.compareTo(tol) > 0 && iteracion < maxIter){
            fila = new QxGenericBean();

            x1 = x0;
            x0 = next.with("x1", x1).and("y0", y0).and("d0", d0).and("s0", s0).evaluate().getNumberValue();
            
            y0 = func.with("x", x0).evaluate();
            d0 = der.with("x", x0).evaluate();
            s0 = segDer.with("x", x0).evaluate();

            error = x0.subtract(x1).abs();

            fila.setValue("ITERACION", String.valueOf(iteracion));
            fila.setValue("XN", String.valueOf(x0.doubleValue()));
            fila.setValue("F(XN)", String.valueOf(y0.getNumberValue().doubleValue()));
            fila.setValue("F'(XN)", String.valueOf(d0.getNumberValue().doubleValue()));
            fila.setValue("F''(XN)", String.valueOf(s0.getNumberValue().doubleValue()));
            fila.setValue("ERROR", String.valueOf(error.doubleValue()));
            tabla.getListQxBean("FILAS").add(fila);
            System.out.println(iteracion);
            iteracion++;
        }
        tabla.setValue("MAX_ITERACION", iteracion-1);
        if (y0.getNumberValue().abs().compareTo(BigDecimal.ZERO) == 0) {
            tabla.setValue("MENSAJE", "El valor " + x0.toString() + " es una raíz");
            return tabla;
        } else if (error.abs().compareTo(tol) < 0) {
            tabla.setValue("MENSAJE", "No se ha logrado encontrar una raíz exacta dentro de la tolerancia seleccionada. El valor " + x0.toString() + " es el más aproximado");
            return tabla;
        } else {
            tabla.setValue("MENSAJE", "Se ha fallado en " + iteracion + " iteraciones");
            return tabla;
        }
    }

    public static void main(String[] args) {
        try {
            Tabla.imprimir(raicesMultiples("e^(2x)-(e^3)+3-e^(-1*x)", "2*e^(2x)+e^(-x)", "4*e^(2x)-e^(-x)", new BigDecimal("0.50"), new BigDecimal("0.00000000000000005"), 20));
        } catch (Exception e) {
            System.err.println(e);
        }
    }

}
