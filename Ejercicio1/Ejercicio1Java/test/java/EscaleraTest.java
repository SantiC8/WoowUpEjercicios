import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class EscaleraTest {

    @Test
    public void seSubeUnaEscaleraDeUnEscalonYTieneUnaUnicaPosibilidadDeSubirse()
    {
        Escalera escalera = new Escalera();

        assertEquals(1 , escalera.subir_escalera(1));
    }

    @Test
    public void seSubeUnaEscaleraDeDosEscalonesYTieneDosFormasDeSubirse()
    {
        Escalera escalera = new Escalera();

        assertEquals(2 , escalera.subir_escalera(2));
    }

    @Test
    public void seSubeUnaEscaleraDeTresEscalonesYTieneTresFormasDeSubirse()
    {
        Escalera escalera = new Escalera();

        assertEquals(3 , escalera.subir_escalera(3));
    }

    @Test
    public void seSubeUnaEscaleraDeOchoEscalonesYTieneTreintaYCuatroFormasDeSubirse()
    {
        Escalera escalera = new Escalera();

        assertEquals(34 , escalera.subir_escalera(8));
    }

    //Casos criticos
    @Test
    public void seSubeUnaEscaleraDeCeroEscalonesYNoTieneFormasDeSubirse()
    {
        Escalera escalera = new Escalera();

        assertEquals(-1 , escalera.subir_escalera(0));
    }

    @Test
    public void seSubeUnaEscaleraDeEscalonesNegativosYNoTieneFormasDeSubirse()
    {
        Escalera escalera = new Escalera();

        assertEquals(-1 , escalera.subir_escalera(-8));
    }

}
