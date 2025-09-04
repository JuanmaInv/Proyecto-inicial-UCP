#Como es mi primera vez usando Try Except, hice un ejemplo sencillo para entender su funcionamiento.

# Manejo de errores con try y except
while True:
        try:
            print("Division de dos numeros\n")
            print("Si introduces un valor que no sea numerico, se generara un ValueError.")
            print("Si introduces un cero como divisor, se generara un ZeroDivisionError.\n")
            print("Introduce dos numeros para realizar una division (numerador/denominador):\n")

            num1 = int(input("Introduce el primer numero(numerador):"))
            num2 = int(input("\nIntroduce el segundo numero(divisor):"))

            resultado = num1 / num2

            print(f"\nEl resultado es: {resultado}")
            break # Para salir del bucle, si no hay errores

        except ValueError: #Si se genera un ValueError, se ejecuta este bloque

            print("\nError: Debes introducir numeros validos.")
            if input("\n¿Quieres reintentar? (s/n): ").lower() != 's':
                break # Si no quiere reintentar, salimos
        except ZeroDivisionError: #Si se genera un ZeroDivisionError, se ejecuta este bloque
            print("\nError: No se puede dividir por cero.")
            if input("\n¿Quieres reintentar? (s/n): ").lower() != 's':
                break

# try contiene la operación 10 / 0. Como esto genera un ZeroDivisionError,
# la ejecucion salta a la sección except ZeroDivisionError:, que imprime el mensaje de error,
# y luego el programa continua con la línea "Programa terminado.".

