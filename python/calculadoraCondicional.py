print("==========================")
print("      MI CALCULADORA")
print("==========================")

while True:
    print("")
    print("¿Qué operación deseas realizar?")
    print("1. Multiplicar")
    print("2. Dividir")
    print("3. Salir")
    print("-------------------------------")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        num1 = input("Ingresa el primer número: ")
        num1 = int(num1)
        num2 = input("Ingresa el segundo número: ")
        num2 = int(num2)
        print("El resultado de la multiplicación es", num1*num2)

    elif opcion == "2":