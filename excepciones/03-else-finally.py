try:
    n1 = int(input("Ingresa primer numero: "))
except Exception as ex:
    print("Ocurrió un error")
else:
    print("No ocurrió ningun error")
finally:
    print("Se ejecuta siempre")
