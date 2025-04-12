package aed;

public class Horario {
    int hora;
    int minutos;
    public Horario(int hora, int minutos) {
        this.hora = hora;
        this.minutos = minutos;
    }

    public int hora() {
        return hora;
    }

    public int minutos() {
        return minutos;
    }

    @Override
    public String toString() {
        return hora + ":" + minutos;
    }

    @Override
    public boolean equals(Object otro) {
        boolean otroEsNull = (otro == null);
        boolean claseDistinta = otro.getClass() != this.getClass();
        
        if (otroEsNull || claseDistinta) {
            return false;
            }
        Horario otroHorario = (Horario) otro;
        return hora == otroHorario.hora && minutos == otroHorario.minutos;
        
    }

}
