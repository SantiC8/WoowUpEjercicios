import datetime


class Compra:

    def __init__(self, id_compra, fecha_compra, articulos):
        self.id_compra = id_compra
        self.fecha_compra = fecha_compra
        self.articulos = articulos


    def calcular_fecha_compra(self, lista_compras, repetidos):

        fechas_compras = []
        for compra in lista_compras:
            for articulos in compra.articulos:
                    h = list(articulos.items())
                    for i in repetidos:
                        if h[0][1] == i.sku:
                            fechas_compras.append((h[0][1], compra.fecha_compra))

        ##Busco los articulos con el mismo codigo y sumo sus fechas
        fechas_comparadas_iniciales = []
        diferecia_compras = []

        for i in range(len(fechas_compras)):
            for j in range(len(fechas_compras)):
                if i !=j:
                    if fechas_compras[i][0] == fechas_compras[j][0] and fechas_compras[i] not in fechas_comparadas_iniciales \
                          and  fechas_compras[j] not in fechas_comparadas_iniciales:

                        formato = '%Y-%m-%d'
                        fechas_comparadas_iniciales.append(fechas_compras[i])
                        fecha_compra_inicial = datetime.datetime.strptime(fechas_compras[i][1], formato)
                        fecha_compra_final = datetime.datetime.strptime(fechas_compras[j][1], formato)
                        diferencia = fecha_compra_final - fecha_compra_inicial

                        diferecia_compras.append((fechas_compras[i][0], diferencia.days, fechas_compras[j][1]))

        for x in diferecia_compras:
            print("El articulo con sku =", x[0], "posiblemente se comprara en", x[1], "dias a partir de", x[2], "\n")