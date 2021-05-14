
class Articulo:

    def __init__(self, sku, nombre):
        self.sku = sku
        self.nombre = nombre

    def __eq__(self, otro):

        return self.sku == otro.sku
