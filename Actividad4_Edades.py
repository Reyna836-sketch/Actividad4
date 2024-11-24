print("\n\nBienvenido a Reyna's System, te ayudaremos a calcular la edad de una persona...")

Year = 2024
Control = "si"

while Control.lower() == "si":
    Born = int(input("\nIngresa tu año de nacimiento a 4 dígitos: \n"))

    Control2 = len(str(Born))

    if Control2 != 4:
        print("Año de nacimiento no válido, por favor ingresa un número de 4 dígitos")
        Born = int(input())

    EdadActual = Year-Born

    print("\nLa edad es: ", EdadActual)
    
    Control = input("\nDesea calcular la edad de alguien más? [si, no]: \n")

    if Control.lower() not in ["si", "no"]:
        print("Entrada no valida, se tomará como un no. \n")

print("Gracias por utilizar Reyna's System, hasta luego.\n\n") 
