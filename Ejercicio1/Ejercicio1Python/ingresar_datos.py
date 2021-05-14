from validaciones import validar_escalones
from subir_escalera import subir_escalera


def ingresar_escalones():

    while True:
        try:
            opcion_ingresada = int(input("Ingrese un numero de escalones mayor a 0: "))
            while validar_escalones(opcion_ingresada):
                opcion_ingresada = int(input("Reingrese una opción válida: "))
            break
        except ValueError:
            print("Ingresó datos inválidos")

    print("Las posibles formas de subir una escalera de", opcion_ingresada, "son", subir_escalera(opcion_ingresada),
          "formas.")


ingresar_escalones()
