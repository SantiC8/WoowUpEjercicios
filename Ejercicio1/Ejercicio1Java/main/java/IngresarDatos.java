import java.util.Scanner;

public class IngresarDatos {


    public void ingresarEscalones() {

        Escalera escalera = new Escalera();
        Scanner entrada = new Scanner(System.in);

        int escalones = 0;

        while (Validaciones.validar(escalones)){
            System.out.println("Ingrese un numero de escalones mayor a 0: ");
            escalones = entrada.nextInt();
        }

        System.out.println("Una escalera de " + escalones + " escalones se puede subir de " +
                escalera.subir_escalera(escalones) + " formas.");

    }
}
