package aed;

class ArregloRedimensionableDeRecordatorios {
    Recordatorio[] array = new Recordatorio[0];

    public ArregloRedimensionableDeRecordatorios() {
        
    }

    public ArregloRedimensionableDeRecordatorios(ArregloRedimensionableDeRecordatorios vector) {
        for (int i = 0 ; i<vector.longitud() ; i++){
            agregarAtras(vector.obtener(i));    
        }
    }

    public int longitud() {
        return array.length;
    }

    public void agregarAtras(Recordatorio i) {
        Recordatorio[] array_nuevo = new Recordatorio[this.array.length + 1];
        for (int f = 0; f < array.length ; f++){
            array_nuevo[f] = this.array[f];
        }
        array_nuevo[array_nuevo.length -1] = i;

        this.array = array_nuevo;
    }

    public Recordatorio obtener(int i) {
        return new Recordatorio(array[i].mensaje(),array[i].fecha(),array[i].horario());
    }

    public void quitarAtras() {
        Recordatorio[] array_nuevo = new Recordatorio[this.array.length -1];
        for (int f = 0; f < array_nuevo.length ; f++){
            array_nuevo[f] = this.array[f];   
        }
        this.array = array_nuevo;
    }

    public void modificarPosicion(int indice, Recordatorio valor) {
        this.array[indice] = valor;
    }



    public ArregloRedimensionableDeRecordatorios copiar() {
        // Implementar
        return new ArregloRedimensionableDeRecordatorios(this);
    }
}
