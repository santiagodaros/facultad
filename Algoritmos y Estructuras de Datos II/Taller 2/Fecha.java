package aed;

public class Fecha {
    int dia;
    int mes;
    public Fecha(int dia, int mes) {
        this.dia = dia;
        this.mes = mes;
    }

    public Fecha(Fecha fecha) {
        // Implementar
    }

    public Integer dia() {
        return dia;
    }

    public Integer mes() {
        return mes;
    }

    public String toString() {
        return dia + "/" + mes;
    }

    @Override
    public boolean equals(Object otra) {
        boolean otroEsNull = (otra == null);
        boolean claseDistinta = otra.getClass() != this.getClass();
        
        if (otroEsNull || claseDistinta) {
            return false;
            }
        Fecha otroFecha = (Fecha) otra;
        return dia == otroFecha.dia && mes == otroFecha.mes;
    }

    public void incrementarDia() {
        if ((dia+1) > diasEnMes(mes)){
            if (mes == 12){
                mes = 1;
                dia = 1;
            }
            else{
                dia = 1;
                mes += 1;
            }
        }
        else{
            dia +=1;
        }
    }

    private int diasEnMes(int mes) {
        int dias[] = {
                // ene, feb, mar, abr, may, jun
                31, 28, 31, 30, 31, 30,
                // jul, ago, sep, oct, nov, dic
                31, 31, 30, 31, 30, 31
        };
        return dias[mes - 1];
    }

}
