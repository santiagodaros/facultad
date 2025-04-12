package aed;

public class Recordatorio {
    String mensaje;
    Fecha fecha;
    Horario horario;
    public Recordatorio(String mensaje, Fecha fecha, Horario horario) {
        this.mensaje = mensaje;
        this.fecha = new Fecha(fecha.dia(),fecha.mes());
        this.horario = new Horario(horario.hora(),horario.minutos()); 
    }

    public Horario horario() {
        Horario horario = new Horario(this.horario.hora(), this.horario.minutos());
        return horario;
    }

    public Fecha fecha() {
        Fecha fecha = new Fecha(this.fecha.dia(),this.fecha.mes());
        return fecha;
    }

    public String mensaje() {
        return mensaje;
    }

    @Override
    public String toString() {
        return mensaje + " " + "@" + " " + fecha + " " + horario;
    }

    @Override
    public boolean equals(Object otro) {
        boolean otroEsNull = (otro == null);
        boolean claseDistinta = otro.getClass() != this.getClass();
        
        if (otroEsNull || claseDistinta) {
            return false;
            }
        Recordatorio otroRecordatorio = (Recordatorio) otro;
        return horario.equals(otroRecordatorio.horario)&& fecha.equals(otroRecordatorio.fecha) && mensaje.equals(otroRecordatorio.mensaje);
    }

}
