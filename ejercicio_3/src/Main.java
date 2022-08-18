/// CLASE DE ENCAPSULAMIENTO

public class Main {
    public static void main(String[] args) {

        Persona persona1 = new Persona();
        persona1.setEdad(24);
        persona1.setNombre("ANDRES DANIEL");
        persona1.setTelefono(3214276);

        System.out.println(persona1.getEdad());
        System.out.println(persona1.getNombre());
        System.out.println(persona1.getTelefono());
    }
}
class Persona{
    private int Edad;
    private String nombre;
    private int telefono;

    public void setEdad(int edad) {
        this.Edad = edad;
    }

    public int getEdad() {
        return this.Edad;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }

    public int getTelefono() {
        return this.telefono;
    }
}