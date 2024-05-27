package com.numerico.app;

import java.math.BigDecimal;
import java.util.ArrayList;

import com.ezylang.evalex.Expression;
import com.ezylang.evalex.data.EvaluationValue;

import co.com.quipux.qxgenericbean.QxGenericBean;

public class Biseccion {

    public static QxGenericBean biseccion(String funcion, BigDecimal x0, BigDecimal x1, BigDecimal tol) throws Exception {
        
        QxGenericBean tabla = new QxGenericBean();

        Expression func = new Expression(funcion);
        EvaluationValue fx0 = null;
        EvaluationValue fx1 = null;
        EvaluationValue fxm = null;
        BigDecimal xm = null;
        BigDecimal xma = null;
        BigDecimal xf = null;
        BigDecimal error = null;
        tabla.setValue("FILAS", new ArrayList<>());
        tabla.setValue("COLUMNAS", "ITERACION, XI, XS, XM, F(XM), ERROR");

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
                xm = x0.add(x1);
                xm = xm.divide(new BigDecimal("2.00"));
                fxm = func.with("x", xm).evaluate();
                xf = xm;
                error = fxm.getNumberValue().subtract(func.with("x", xma).evaluate().getNumberValue()).abs();

                fila.setValue("ITERACION", String.valueOf(iteracion));
                fila.setValue("XI", x0.toString());
                fila.setValue("XS", x1.toString());
                fila.setValue("XM", xm.toString());
                fila.setValue("F(XM)", String.valueOf(fxm.getNumberValue().doubleValue()));
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
            Tabla.imprimir(Biseccion.biseccion("(e^(7-4x))-(x^2)+10", new BigDecimal("3.00"), new BigDecimal("4.00"),
                new BigDecimal("0.00005")));
        } catch (Exception e) {
            System.err.println(e);
        }
    }
}

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
