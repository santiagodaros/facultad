package aed;

public class Agenda {
    Fecha fechaHoy;
    ArregloRedimensionableDeRecordatorios recordatorios = new ArregloRedimensionableDeRecordatorios();

    public Agenda(Fecha fechaActual) {
        this.fechaHoy = new Fecha(fechaActual.dia(),fechaActual.mes()) ;
    }

    public void agregarRecordatorio(Recordatorio recordatorio) {
        recordatorios.agregarAtras(new Recordatorio(recordatorio.mensaje(),recordatorio.fecha(),recordatorio.horario()));
    }

    @Override
    public String toString() {
        String string = fechaHoy.toString() + "\n=====\n"; 
        for (int i = 0; i<recordatorios.longitud();i++){
            if ((recordatorios.obtener(i).fecha()).equals(fechaHoy)){
                string += recordatorios.obtener(i) + "\n"; 
            }
        }
        return string;
    }

    public void incrementarDia() {
        fechaHoy.incrementarDia();
    }

    public Fecha fechaActual() {    
        fechaHoy = new Fecha(this.fechaHoy.dia(), this.fechaHoy.mes());
        return fechaHoy;
    }

}
