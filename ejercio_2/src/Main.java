import javax.management.loading.MLetContent;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
       /// PRIMERA PARTE DEL EJERCICIO
        Scanner entrada = new Scanner(System.in);
        double numeroIf = entrada.nextDouble();
        if (numeroIf<0){
            System.out.println(("numeroIf es negativo"));
        }
        else if (numeroIf>0){
            System.out.println("numeroIf es positivo");
        }
        else {
            System.out.println("numeroIf es cero");
        }
        ///Segunda Parte while

        int numeroWhile = 0;
        while (numeroWhile<3){
            numeroWhile++;
            System.out.println(numeroWhile);
        }
        // Tercera parte do while
        do{
            numeroWhile ++ ;
            System.out.println(numeroWhile);
        } while(numeroWhile != numeroWhile);

        //Cuarta Parte bucle for

        for (int numeroFor = 0; numeroFor <= 3; numeroFor++){
            System.out.println(numeroFor);
        }

        String Estacion = "verano";
        switch (Estacion){
            case "verano":
                System.out.println("Es verano");
                break;
            case "invierno":
                System.out.println("Es invierno");
                break;
            case "otoño":
                System.out.println("Es otoño");
                break;
            case "primavera":
                System.out.println("Es primavera");
                break;
            default:
                System.out.println("No es una estacion del año");
        }


    }
}
