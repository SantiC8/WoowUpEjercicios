
public class Escalera {

    public int subir_escalera(int escalones) {

        //numeros invalidos
        if (Validaciones.validar(escalones))
        {
            return -1;
        }

        // recursividad hasta llegar a los casos bases
        if (escalones > 2)
        {
            return subir_escalera(escalones - 1) + subir_escalera(escalones - 2);
        }

        //casos bases
        else if (escalones == 2)
        {
            return 2;
        }

        else
        {
            return 1;
        }
    }
}
