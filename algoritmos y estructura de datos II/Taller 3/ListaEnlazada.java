package aed;

import java.util.*;

public class ListaEnlazada<T> implements Secuencia<T> {
    private Nodo primero;
    private Nodo ultimo;

    private class Nodo {
        private Nodo sig;
        private Nodo ant;   
        private T valor;
        Nodo(T v) { valor = v; }
    }

    public ListaEnlazada() {
        primero = null;
        ultimo = null;
    }

    public int longitud() {
        int contador = 0;
        Nodo actual = primero;
        while (actual!=null){
            contador += 1;
            actual = actual.sig;
        }
        return contador;
    }

    public void agregarAdelante(T elem) {
        Nodo nuevo_Nodo = new Nodo (elem);
        if (longitud()>0){
        primero.ant = nuevo_Nodo;
        nuevo_Nodo.sig = primero;
        primero = nuevo_Nodo;
        }
        else{
            primero = nuevo_Nodo;
            ultimo= nuevo_Nodo;
        }
    }

    public void agregarAtras(T elem) {
        Nodo nuevo_Nodo = new Nodo(elem);
        if (longitud()>0){
        ultimo.sig = nuevo_Nodo;
        nuevo_Nodo.ant = ultimo;
        ultimo = nuevo_Nodo;
        }
        else{
            primero = nuevo_Nodo;
            ultimo = nuevo_Nodo;
        }
    }

    public T obtener(int i) {
        Nodo actual=primero;
        for (int j = 0; j<i;j++){
            actual= actual.sig;
        }
        return actual.valor;
    }

    public void eliminar(int i) {
        Nodo actual = primero;
        Nodo prev = primero;
        if (longitud() == 1){
            primero = null;
            ultimo = null;
        }
        else{
        for (int j = 0; j < i; j++) {
            prev = actual;
            actual = actual.sig;
            }
            if (i == 0) {
            primero = actual.sig;
            primero.ant = null;
            } 
            else {
                if (i==longitud()-1){
                    ultimo = prev;
                    ultimo.sig = null;
                }
                else{
                    prev.sig = actual.sig;
                    actual.sig.ant=prev;
                }
        }
    }
    }

    public void modificarPosicion(int indice, T elem) {
        Nodo actual = primero;
        for (int j = 0; j < indice; j++) {
            actual = actual.sig;
            }
        actual.valor=elem;
    }

    public ListaEnlazada(ListaEnlazada<T> lista) {
        Nodo actual = lista.primero;
        while (actual != null) {
            this.agregarAtras(actual.valor);
        actual = actual.sig;
        }
    }
    
    @Override
    public String toString() {
        throw new UnsupportedOperationException("No implementada aun");
    }

    private class ListaIterador implements Iterador<T> {
    	// Completar atributos privados

        public boolean haySiguiente() {
	        throw new UnsupportedOperationException("No implementada aun");
        }
        
        public boolean hayAnterior() {
	        throw new UnsupportedOperationException("No implementada aun");
        }

        public T siguiente() {
	        throw new UnsupportedOperationException("No implementada aun");
        }
        

        public T anterior() {
	        throw new UnsupportedOperationException("No implementada aun");
        }
    }

    public Iterador<T> iterador() {
	    throw new UnsupportedOperationException("No implementada aun");
    }

}
