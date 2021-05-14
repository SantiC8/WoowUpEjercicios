from Ejercicio2.articulo import Articulo
from Ejercicio2.compra import Compra


class Comparar:

    def comparar_compras(self, lista_compras):

        lista_articulos = []

        for x in lista_compras:
            lista_articulos.append(x.articulos)

        repetidos = self.comparar_articulos(lista_articulos)

        Compra.calcular_fecha_compra(self, lista_compras, repetidos)


    def comparar_articulos(self, lista_articulos):

        articulos_comprados = []
        #Creo lista de articulos
        for articulos in lista_articulos:
            for articulo in articulos:
                h = list(articulo.items())
                articulos_comprados.append(Articulo(h[0][1], h[1][1]))

        return self.articulos_repetidos(articulos_comprados)

    def articulos_repetidos(self, articulos_comprados):

        repetidos = []

        for i in range(len(articulos_comprados)):
            for j in range(len(articulos_comprados)):
                if i !=j:
                    if articulos_comprados[i] == articulos_comprados[j] and articulos_comprados[i] not in repetidos:
                        repetidos.append(articulos_comprados[i])

        return repetidos
