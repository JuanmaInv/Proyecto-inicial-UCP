#CONVERSOR DE MONEDAS EN PYTHON
#REPOSITORIO DE GITHUB


print("--- Conversor de Monedas ---")

# Tasas de Cambio Fijas
tasasCambio = {
    'USD': {'EUR': 0.88, 'ARS': 1200, 'REA':5.69},
    'EUR': {'USD': 1.14, 'ARS': 1327, 'BRL':5.50},
    'ARS': {'USD': 0.0011, 'EUR': 0.00105, 'BRL':0.0058},
    'BRL': {'USD': 0.196, 'EUR': 0.182, 'ARS':172},
}

# Lista para almacenar el historial de conversiones
historial = []

# Función para guardar el historial
def guardar_historial(cantidad, moneda_origen, resultado, moneda_destino):
    historial.append(f"{cantidad} {moneda_origen} a {resultado} {moneda_destino}")

# Función para mostrar y borrar historial
def gestionar_historial():
    if opcion==5:
        print("\n--- Historial de Conversiones ---")
        for entrada in historial:
            print(entrada)
        borrar = input("¿Desea borrar el historial? (s/n): ").lower()
        if borrar == "s":
            historial.clear()
            print("Historial borrado correctamente.")
    else:
        print("El historial está vacío.")


def cambioUSD():
    print("""--- Conversion desde USD ---
          1. USD a ARS
          2. USD a EUR
          3. USD a BRS""")

    Moneda2 = int(input("Seleccione la moneda destino (1-3): "))
    USD = float(input("Ingrese la cantidad de USD que desea convertir: "))

    if Moneda2 == 1:  # USD a ARS
        tasa = 1200  # 1 USD = 1200 ARS
        resultado = USD * tasa
        print(f"{USD} USD equivalen a {resultado} ARS")
        guardar_historial(USD, "USD", resultado, "ARS")

    elif Moneda2 == 2:  # USD a EUR
        tasa = 0.88  # 1 USD = 0.88 EUR
        resultado = USD * tasa
        print(f"{USD} USD equivalen a {resultado} EUR")
        guardar_historial(USD, "USD", resultado, "EUR")

    elif Moneda2 == 3:  # USD a BRS
        tasa = 5.69  # 1 USD = 5.69 BRS
        resultado = USD * tasa
        print(f"{USD} USD equivalen a {resultado} BRS")
        guardar_historial(USD, "USD", resultado, "BRS")

    else:
        print("Opcion no valida.")


def cambioARS():
    print("--- Conversión desde ARS ---")
    print("1. ARS a USD")
    print("2. ARS a EUR")
    print("3. ARS a BRL")

    Moneda2 = int(input("Seleccione la moneda destino (1-3): "))
    ARS = float(input("Ingrese la cantidad de ARS que desea convertir: "))

    if Moneda2 == 1:  # ARS a USD
        tasa = 0.0011
        resultado = ARS * tasa
        print(f"{ARS} ARS equivalen a {resultado} USD")
        guardar_historial(ARS, "ARS", resultado, "USD")
        
    elif Moneda2 == 2:  # ARS a EUR
        tasa = 0.00105
        resultado = ARS * tasa
        print(f"{ARS} ARS equivalen a {resultado} EUR")
        guardar_historial(ARS, "ARS", resultado, "EUR")

    elif Moneda2 == 3:  # ARS a BRL
        tasa = 0.0058
        resultado = ARS * tasa
        print(f"{ARS} ARS equivalen a {resultado} BRL")
        guardar_historial(ARS, "ARS", resultado, "BRL")

    else:
        print("Opción no válida.")

def cambioEUR():
    print("--- Conversión desde EUR ---")
    print("1. EUR a USD")
    print("2. EUR a ARS")
    print("3. EUR a BRL")

    Moneda2 = int(input("Seleccione la moneda destino (1-3): "))
    EUR = float(input("Ingrese la cantidad de EUR que desea convertir: "))

    if Moneda2 == 1:  # EUR a USD
        tasa = 1.14
        resultado = EUR * tasa
        print(f"{EUR} EUR equivalen a {resultado} USD")
        guardar_historial(EUR, "EUR", resultado, "USD")

    elif Moneda2 == 2:  # EUR a ARS
        tasa = 1327
        resultado = EUR * tasa
        print(f"{EUR} EUR equivalen a {resultado} ARS")
        guardar_historial(EUR, "EUR", resultado, "ARS")

    elif Moneda2 == 3:  # EUR a BRL
        tasa = 5.50
        resultado = EUR * tasa
        print(f"{EUR} EUR equivalen a {resultado} BRL")
        guardar_historial(EUR, "EUR", resultado, "BRL")

    else:
        print("Opción no válida.")


def cambioBRL():
    print("--- Conversión desde BRL ---")
    print("1. BRL a USD")
    print("2. BRL a EUR")
    print("3. BRL a ARS")

    Moneda2 = int(input("Seleccione la moneda destino (1-3): "))
    BRL = float(input("Ingrese la cantidad de BRL que desea convertir: "))

    if Moneda2 == 1:  # BRL a USD
        tasa = 0.196
        resultado = BRL * tasa
        print(f"{BRL} BRL equivalen a {resultado} USD")
        guardar_historial(BRL, "BRL", resultado, "USD")

    elif Moneda2 == 2:  # BRL a EUR
        tasa = 0.182
        resultado = BRL * tasa
        print(f"{BRL} BRL equivalen a {resultado} EUR")
        guardar_historial(BRL, "BRL", resultado, "EUR")

    elif Moneda2 == 3:  # BRL a ARS
        tasa = 172
        resultado = BRL * tasa
        print(f"{BRL} BRL equivalen a {resultado} ARS")
        guardar_historial(BRL, "BRL", resultado, "ARS")

    else:
        print("Opción no válida.")


opcion = ""  # Se inicia la variable como cadena vacía

while opcion != "6":  # El bucle seguirá mientras la opción no sea 5
    print("\n--- Conversor de Monedas ---")
    print("1. Convertir desde USD")
    print("2. Convertir desde EUR")
    print("3. Convertir desde ARS")
    print("4. Convertir desde BRL")
    print("5. Mostrar historial")
    print("6. Salir")
    
    opcion = input("Seleccione una opción (1-6): ")  # Aquí se le pide al usuario una opción

    if opcion == "1":
        cambioUSD()
    elif opcion == "2":
        cambioEUR()
    elif opcion == "3":
        cambioARS()
    elif opcion == "4":
        cambioBRL()
    elif opcion == "5":
        gestionar_historial()
    elif opcion == "6":
        print("¡Hasta luego!")
    else:
        print("Opción inválida.")