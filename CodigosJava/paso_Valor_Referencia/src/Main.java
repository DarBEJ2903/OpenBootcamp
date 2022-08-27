public class Main {
    public static void main(String[] args) {
       // PASO POR VALOR
        int num1 = 10; // int 32 bits => 4 Bytes/
        sumaNumeros(num1); //Paso por Valor, asigna en otro espacio de memoria (a) el valor de num1,
                          // es decir, se duplica el espacio ocupado en memoria.

        System.out.println(num1);

        // PASO POR REFERENCIA
        Coche coche = new Coche();
        aumentarVel(coche); //Se pasa por referencia la clase coche que apunta al espacio de memoria con la
                           // variable velocidad, no se duplica el espacio en memoria
        System.out.println(coche.velocidad);
    }

    public  static void aumentarVel(Coche coche){
        coche.velocidad += 100;
        System.out.println(coche.velocidad);
    }

    public static void sumaNumeros(int a){
        System.out.println(a + 10);
    }
}

class Coche{
     public int velocidad;
}