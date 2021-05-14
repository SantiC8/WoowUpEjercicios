from validaciones import validar_escalones


def subir_escalera(n):

    if validar_escalones(n):
        print("Escalones invalidos")
        return -1

    # recursividad hasta llegar a los casos bases
    elif n > 2:
        return subir_escalera(n - 1) + subir_escalera(n - 2)

    #casos bases
    elif n == 2:
        return 2

    else:
        return 1
