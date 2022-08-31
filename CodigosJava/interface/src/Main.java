public class Main {

    public static void main(String[] args) {
        Coche coche = new Coche();
        Moto moto = new  Moto();

        ejecutarAcelerar(coche);
        ejecutarAcelerar(moto);
    }
    public static void ejecutarAcelerar (Vehiculo vehiculo){
        // Se ejecuta la funcion acelerar vehiculo de la clase que implementa la interfaz
        // que se recibe como parametro
        vehiculo.acelerarVehiculo(32);
    }

}

//Creacion de la interface

interface Vehiculo{
   void acelerarVehiculo(double velocidadVehiculo);
   void frenarVehiculo(double velocidadVehiculo);
}

// Implementaciòn de la interface

class Coche implements Vehiculo{

    public void acelerarVehiculo(double velocidadVehiculo){
          System.out.println("Acelerando Coche()"+velocidadVehiculo);
    }
    public void frenarVehiculo(double velocidadVehiculo){
        System.out.println("Frenar Coche");
    }
}

class Moto implements Vehiculo{

    public void acelerarVehiculo(double velocidadVehiculo){
        System.out.println("Acelerando moto()");
    }
    public void frenarVehiculo(double velocidadVehiculo){
        System.out.println("Frenando moto");
    }
}