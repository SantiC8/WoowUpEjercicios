import json
from carga_archivo import Carga

try:
    with open('purchases.json', 'r') as my_file:
        data = my_file.read()
        Carga(json.loads(data))

except FileNotFoundError:
    print("Nombre del archivo invalido")


