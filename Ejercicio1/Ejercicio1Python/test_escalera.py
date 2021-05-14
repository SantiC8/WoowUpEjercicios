import unittest
from subir_escalera import subir_escalera


class TestEjercicio2(unittest.TestCase):

    def test_subir_escalera_de_un_escalon(self):
        result = subir_escalera(1)
        self.assertEqual(result, 1)

    def test_subir_escalera_de_dos_escalones(self):
        result = subir_escalera(2)
        self.assertEqual(result, 2)

    def test_subir_escalera_de_tres_escalones(self):
        result = subir_escalera(3)
        self.assertEqual(result, 3)

    def test_subir_escalera_de_ocho_escalones(self):
        result = subir_escalera(8)
        self.assertEqual(result, 34)

    #Casos Criticos
    def test_subir_escalera_de_cero_escalones(self):
        result = subir_escalera(0)
        self.assertEqual(result, -1)

    def test_subir_escalera_de_escalones_negativos(self):
        result = subir_escalera(-8)
        self.assertEqual(result, -1)
