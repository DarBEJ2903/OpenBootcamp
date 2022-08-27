// La Recursividad son funciones que se crean y que se llaman a si mismas,
// Es necesario tener cuidado con este tipo de funciones para no crear Bucles infinitos

public class Main {
    public static void main(String[] args) {
        int resultado;
        resultado = factorial(8);
        System.out.println(resultado);
    }
    public static int factorial(int numero){
        int resultado = 1;
        if (numero == 1){
            return resultado;
        }
        resultado = factorial(numero-1)*numero;
        return resultado;
    }
}