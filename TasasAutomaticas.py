from urllib.request import urlopen #Para abrir una URL y leer su contenido
import json #Para trabajar con datos en formato JSON

# Funcion para obtener tasas de cambio desde una API
def obtener_tasas():
    try:
        # Obtener tasas de cambio desde la API
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        # Abre la URL y obtiene la respuesta
        respuesta = urlopen(url)
        # Convierte la respuesta JSON a un diccionario de Python
        datos = json.loads(respuesta.read())
        # Retorna solo las tasas de cambio
        return datos['rates']
    except:
        # En caso de error, retorna None
        return None

# Funcion para hacer los cambios o conversiones entre monedas
def cambiosMonedas(cantidad, monedaOrigen, monedaDestino):
    # Obtiene las tasas de cambio actuales
    tasas = obtener_tasas()

    # Si las tasas se obtuvieron correctamente, realiza la conversion
    if tasas:

        # Si la moneda origen es USD, simplemente multiplica por la tasa de la moneda destino
        if monedaOrigen == "USD":
            resultado = cantidad * tasas[monedaDestino]

        else:
            # Si la moneda destino es USD, divide por la tasa de la moneda origen
            resultado = cantidad * (tasas[monedaDestino] / tasas[monedaOrigen])

        return resultado # Retorna el resultado de la conversion
    
    # Si no se pudieron obtener las tasas por un error, retorna None
    return None

# Menu principal
while True:
    print("\n=== Conversor de Monedas ===")
    print("1. Convertir moneda (origen y destino)")
    print("2. Salir")
    
    opcion = input("Seleccione una opcion valida: ")
    #OPCION 1: Convertir moneda
    if opcion == "1":
        # Lista de monedas disponibles
        monedasDisponibles = ["USD", "EUR", "ARS", "BRL", "PYG"]
        print ("\n Monedas disponibles:", " --- ".join(monedasDisponibles)) # .join es para unir una cadena, muestra las monedas separadas por " --- "...ocupa el siguiente formato:
                                                                            # "Monedas disponibles:" + (monedas definidas anteriormente) + separadas por " --- "
        
        monedaOrigen = input("Ingrese moneda origen: ").upper()    #Convierte un string en mayusculas,
                                                                   # si ingreso por ejemplo "usd o USD"... se convierte a USD
        monedaDestino = input("Ingrese moneda destino: ").upper()

        if monedaOrigen in monedasDisponibles and monedaDestino in monedasDisponibles: #1ero verifica que la moneda origen este en la lista de monedas y luego verifica que la moneda destino tambien este en la lista de monedas
            try:                                                                       #Si ambas monedas (operador AND) estan en la lista, entonces pide la cantidad a convertir. Si los dos son true, devuelve true.
                # Solicitar cantidad a convertir
                cantidad = float(input(f"Cantidad de {monedaOrigen}: "))
                # Realiza la conversion
                resultado = cambiosMonedas(cantidad, monedaOrigen, monedaDestino)
                
                if resultado:
                    # Muestra el resultado con 2 decimales
                    print(f"Perfecto, {cantidad}  {monedaOrigen} es igual a {resultado:.2f} {monedaDestino}")
                    print("Gracias por usar el conversor de monedas")
                else:
                    print("Error al obtener tasas de cambio")

            except ValueError: # Si el usuario no ingresa un numero valido
                print("Por favor ingrese un numero valido")
        else: #Si alguna de las monedas no esta en la lista, muestra el siguiente mensaje
            print("Moneda no valida")
    # OPCION 2: Salir del programa      
    elif opcion == "2": # Opcion para salir del programa
        print("Chau")
        break
    # Si la opcion no es valida
    #ULTIMA OPCION, no valida
    else:
        print("Opcion no valida")