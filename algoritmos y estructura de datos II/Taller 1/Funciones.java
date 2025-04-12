package aed;

import javax.swing.plaf.TreeUI;

class Funciones {
    int cuadrado(int x) {
        return x*x;
    }

    double distancia(double x, double y) {
        return Math.sqrt(x*x + y*y);
    }

    boolean divideA(int d, int n) {
        return (n % d == 0);

    }

    boolean esPar(int n) {
        if (n%2 == 0){
            return true;
        }
        return false;
    }

    boolean esBisiesto(int n) {
        if (divideA(4,n) && !divideA(100, n) || divideA(400, n)){
            return true;
        } 
        return false; 
    }

    int factorialIterativo(int n) {
        if (n == 0){
            return 1;
        }
        int h = 1;
        while (n > 0){
            h = h*n;
            n -= 1;
        }
        return h;
    }

    int factorialRecursivo(int n) {
        int x = 1;
        if (n == 0){
            return 1;
        }
        else {
            x = n * factorialRecursivo(n-1);
        }
        return x;
    }

    boolean primo(int n) {
        int k = 0;
        for (int i = 1; i<=n ;i++){
            if (divideA(i, n)){
                k += 1;
            }
        }
        if (k == 2){
            return true;
        }
        return false;
    }
    boolean esPrimo(int n) {
        int k = 0;
        for (int i = 1; i<=n ;i++){
            if (divideA(i, n)){
                k += 1;
            }
        }
        if (k == 2){
            return true;
        }
        return false;
    }
    

    int sumatoria(int[] numeros) {
        int k = 0;
        for (int i = 0;i<numeros.length;i++){
            k += numeros[i];
        }
        return k;
    }

    int busqueda(int[] numeros, int buscado) {
        for (int i = 0; i<numeros.length ; i++){
            if (numeros[i] == buscado){
                return i;
            }
        }
        return 0;
    }


    boolean tienePrimo(int[] numeros) {
        for (int i = 0;i<numeros.length;i++){
            if (esPrimo(numeros[i])){
                return true;
            }
        }
        return false;
    }

    boolean todosPares(int[] numeros) {
        for (int i = 0; i< numeros.length;i++){
            if (!esPar(numeros[i])){
                return false;
            }
        }
        return true;
    }

    boolean esPrefijo(String s1, String s2) {
        if (s2.length() < s1.length()){
            return false;
        }
        for (int i=0;i<s1.length();i++){
            if (s1.charAt(i) != s2.charAt(i)){
                return false;
            }
        }
        return true;
    }

    String invertir(String s1){
        String k = "";
        for (int i = s1.length()-1; i>=0;i--){
            k += s1.charAt(i);


        }
        return k;
    }

    boolean esSufijo(String s1, String s2) {
        if (s2.length() < s1.length()){
            return false;
        }
        return esPrefijo(invertir(s1), invertir(s2));
    }
}
