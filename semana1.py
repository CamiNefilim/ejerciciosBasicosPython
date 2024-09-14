import time

while True:
    time.sleep(2)
    print("Menú de hoy")
    print("""
        1. Imprimir un mensaje
        2. Sumar dos números
        3. Número par o impar
        4. Área de un triángulo
        5. Intercambio de valores
        6. Conversión de temperatura
        7. Números consecutivos
        8. Suma de una lista
        9. Número mayor
        10. Invertir una cadena
        11. Contador de vocales
        12. Adivina el número
        13. Factorial
        14. Números pares en una lista
        15. Tablas de multiplicar
        16. Conversión de horas a segundos
        17. Suma de dígitos
        18. Verificar palíndromo
        19. Imprimir números impares
        20. Contador de palabras
        0. Salir""")

    # Captura opción seleccionada
    opcion = input("\nIngresa el número de la acción que deseas ejecutar: ")

    # Evalúa las opciones
    match opcion:
        case "1":
            # Si se selecciona 1. Imprimir un mensaje
            print("Hola, Python")
        case "2":
            # Si se selecciona 2. Sumar dos números
            while True:
                try:
                    # Solicita números
                    valorA = float(input("Ingresa el primer número: "))
                    valorB = float(input("Ingresa el segundo número: "))
                    # Realiza la suma
                    suma = valorA + valorB
                    # Imprime resultado
                    print(f"La suma es: {suma}")
                    break  # Se sale del bucle si se ingresa número
                except ValueError:
                    # Imprime error
                    print("Para poder sumar se requiere ingresar números.")
        case "3":
            # Si se selecciona 3. Número par o impar
            while True:
                try:
                    # Solicita número
                    numero = int(input("Ingresa un número: "))
                    # Verifica si es par o inpar
                    if numero % 2 == 0:
                        print(f"El número ingresado: {numero} es par.")
                    else:
                        print(f"El número ingresado: {numero} es inpar.")
                    break  # Se sale del bucle si se ingresa número
                except ValueError:
                    # Imprime error
                    print("Por favor ingresa un número entero.")
        case "4":
            # Si se selecciona 4. Área de un triángulo
            while True:
                # Solicita base y altura
                try:
                    base = float(input("Ingresa la base del triángulo: "))
                    altura = float(input("Ingresa la altura del triángulo: "))
                    # Calcula área
                    area = (base * altura)/2
                    # Imprime resultado
                    print(f"El área del triángulo es: {area}")
                    break  # Se sale del bucle si se ingresa número
                except ValueError:
                    # Imprime error
                    print("Para poder calcular se requieren números.")
        case "5":
            # Si se selecciona 5. Intercambio de valores
            valorA = input("Ingresa el valor de a: ")
            valorB = input("Ingresa el valor de b: ")
            # Intercambia valores con variable temporal
            temp = valorA
            valorA = valorB
            valorB = temp
            # Imprime resultados
            print(f"Después del intercambio, el valor de a es: {valorA}")
            print(f"Después del intercambio, el valor de b es: {valorB}")
        case "6":
            # Si se selecciona 6. Conversión de temperatura
            while True:
                try:
                    # Solicita grados Celsius
                    celsius = float(input("Ingresa los Grados Celsius: "))
                    # Calcula grados Fahrenheit
                    fahrenheit = (1.8 * celsius) + 32
                    # Imprime resultado
                    print(f"{celsius}° Celsius son {fahrenheit}° Fahrenheit.")
                    break  # Se sale del bucle si se ingresa número
                except ValueError:
                    # Imprime error
                    print("Para realizar la conversión se requieren números.")
        case "7":
            # Si se selecciona 7. Números consecutivos
            for i in range(1, 11):
                print(i)
        case "8":
            # Si se selecciona 8. Suma de una lista
            import random
            listaNumeros = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
            print(f"La suma de: {listaNumeros} es: {sum(listaNumeros)}")
        case "9":
            # Si se selecciona 9. Número mayor
            while True:
                try:
                    # Solicita números
                    valorA = float(input("Ingresa el primer número: "))
                    valorB = float(input("Ingresa el segundo número: "))
                    valorC = float(input("Ingresa el tercer número: "))
                    # Verifica cual es el más grande
                    mayor = max(valorA, valorB, valorC)
                    # Imprime resultado
                    print(f"De los números ingresados el mayor es: {mayor}.")
                    break  # Se sale del bucle si se ingresa número
                except ValueError:
                    # Imprime error
                    print("Para poder calcular se requieren números.")
        case "10":
            # Si se selecciona 10. Invertir una cadena
            texto = input("Ingresa un texto: ")
            textoInvertido = ""
            for letra in texto:
                textoInvertido += letra
            print(f"El texto invertido es: {textoInvertido}.")
        case "11":
            # Si se selecciona 11. Contador de vocales
            texto = input("Ingresa un texto: ")
            vocales = "aeiou"
            contador = 0
            for letra in texto:
                if letra.lower() in vocales:
                    contador += 1
            print(f"El texto tiene: {contador} vocal(es).")
        case "12":
            # Si se selecciona 12. Adivina el número
            while True:
                try:
                    # Genera número aleatorio entre 1 y 10
                    import random
                    numero = random.randint(1, 10)
                    # Solicita número
                    valorA = int(input("Adivina un número entre el 1 y 10: "))
                    # Imprime resultado
                    if numero == valorA:
                        print(f"Adivinaste, estoy pensando en el: {numero}.")
                    else:
                        print(f"No adivinaste, estoy pensando en el: {numero}.")
                    # Imprime resultado
                    break  # Se sale del bucle si se ingresa número
                except ValueError:
                    # Imprime error
                    print("Para poder calcular se requieren números.")
        case "13":
            # Si se selecciona 13. Factorial
            while True:
                try:
                    # Solicita número
                    numero = int(input("Ingresa un número: "))
                    # Calcula factorial
                    factorial = 1
                    for i in range(1, numero + 1):
                        factorial *= i
                    print(f"La factorial de: {numero} es: {factorial}.")
                    # Imprime resultado
                    break  # Se sale del bucle si se ingresa número
                except ValueError:
                    # Imprime error
                    print("Para poder calcular se requieren números.")
        case "14":
            # Si se selecciona 14. Números pares en una lista
            import random
            listaNumeros = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
            listaNumerosPares = []
            for numero in listaNumeros:
                if numero % 2 == 0:
                    listaNumerosPares.append(numero)
            print(f"Los numeros pares de: {listaNumeros} son: {listaNumerosPares}")
        case "15":
            # Si se selecciona 15. Tablas de multiplicar
            while True:
                try:
                    # Solicita número
                    numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
                    # Calcula tabla de multiplicar
                    for i in range(1, 11):
                        # Imprime resultado
                        print(f"{numero}x{i} = {numero*i}.")
                    break  # Se sale del bucle si se ingresa número
                except ValueError:
                    # Imprime error
                    print("Para poder calcular se requieren números.")
        case "16":
            # Si se selecciona 16. Conversión de horas a segundos
            while True:
                try:
                    # Solicita horas
                    horas = int(input("Ingresa hora para convertir a segundos: "))
                    # Imprime resultado
                    print(f"{horas} hora(s) son {horas*3600} segundo(s).")
                    break  # Se sale del bucle si se ingresa número
                except ValueError:
                    # Imprime error
                    print("Para poder calcular se requieren números.")
        case "17":
            # Si se selecciona 17. Suma de dígitos
            while True:
                try:
                    # Solicita numero
                    numero = int(input("Ingresa un número: "))
                    suma = 0
                    for digito in str(numero):
                        suma += int(digito)
                    # Imprime resultado
                    print(f"La suma de los digitos de {numero} es: {suma}.")
                    break  # Se sale del bucle si se ingresa número
                except ValueError:
                    # Imprime error
                    print("Para poder calcular se requieren números.")
        case "18":
            # Si se selecciona 18. Verificar palíndromo
            texto = input("Ingresa un texto para verificar si es palíndromo: ")
            # Imprime resultado
            if texto.lower() == texto.lower()[::-1]:
                print("El texto es palíndromo.")
            else:
                print("El texto no es palíndromo.")
        case "19":
            # Si se selecciona 19. Imprimir números impares
            print("Los números impares entre 1 y 20 son:")
            for i in range(1, 21):
                if i % 2 != 0:
                    print(i)
        case "20":
            # Si se selecciona 20. Contador de palabras
            texto = input("Ingresa un texto para contar sus palabras: ")
            palabras = texto.split()
            # Imprime resultado
            print(f"El texto ingresado tiene {len(palabras)} palabra(s).")
        case "0":
            print("Muchas gracias por participar.")
            break
        case _:
            print("No existe la opción ingresada")
            