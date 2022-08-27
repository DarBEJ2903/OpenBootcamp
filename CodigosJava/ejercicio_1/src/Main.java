public class Main {
    public static void main(String[] args) {
        double resultadoSuma = sumar(2.3,3.9,20); /// Parte 1 del ejercio

        Coche myCoche = new Coche(); //Segunda Parte
        myCoche.sumPuertas(); //Segunda Parte

    }
    public static double sumar(double num1,double num2,double num3){ //Parte 1 del ejercicio
        double result;
        result = num1 + num2 + num3;
        return result;
    }
}

class Coche {
    public int numPuertas = 0;
    public void sumPuertas(){
        this.numPuertas++;
        System.out.println(numPuertas);
    }
}