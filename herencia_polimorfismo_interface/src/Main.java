public class Main {
    public static void main(String[] args) {
        // PRIMERA PARTE
        Cliente cliente = new Cliente();

        cliente.nombre = "Andres Daniel";
        cliente.edad = 24;
        cliente.telefono = 321427613;
        cliente.setCredito(2158);

        System.out.println("Nombre Cliente: "+ cliente.nombre);
        System.out.println("Edad: "+ cliente.edad);
        System.out.println("Telefono:"+cliente.telefono);
        System.out.println("Credito No: "+ cliente.getCredito());

        // SEGUNDA PARTE

        Trabajador trabajador = new Trabajador();

        trabajador.nombre = "Natalia Rojas";
        trabajador.edad = 33;
        trabajador.telefono = 314525342;
        trabajador.setSalario(1200000);

        System.out.println("Nombre Trabajador: "+trabajador.nombre);
        System.out.println("Edad: "+ trabajador.edad );
        System.out.println("Telefono: "+trabajador.telefono);
        System.out.println("Salario: "+trabajador.getSalario());



    }
}
class Persona{
    int edad;
    String nombre;
    long telefono;
}

//Herencia

class Cliente extends Persona {
    private int credito;

    public void setCredito(int credito) {
        this.credito = credito;
    }

    public int getCredito() {
        return credito;
    }

}

class Trabajador extends Persona{
    private long salario;

    public void setSalario(long salario) {
        this.salario = salario;
    }

    public long getSalario() {
        return salario;
    }
}
