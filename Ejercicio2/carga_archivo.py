from Ejercicio2.comparar import Comparar
from Ejercicio2.compra import Compra


class Carga:

    def __init__(self, compras_cliente):
        self.compras_cliente = compras_cliente
        self.cargar_datos()

    def cargar_datos(self):

        lista_compras = []

        comparar = Comparar()

        lista_clientes = self.compras_cliente.values()

        for cliente in lista_clientes:

            todas_las_compras = cliente.values()

            for una_compra in todas_las_compras:

                for valores_compra in una_compra:

                    lista_claves = list(valores_compra.items())

                    lista_compras.append(Compra(lista_claves[0][1], lista_claves[1][1], lista_claves[2][1]))

        comparar.comparar_compras(lista_compras)
