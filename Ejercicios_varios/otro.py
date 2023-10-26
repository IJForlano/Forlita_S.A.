def tabla_multiplicar():
    f = open("tabla-n.txt", "w")
    n = float(input("Ingrese un numero para obtener su tabla de multiplicacion."))
    print(f"Su numero inicial es {n}.")

    for i in range(1, 11):
        multiplicacion = n * i
        print(f"{i}* {n} = {multiplicacion}")
        f.write(f"{i}* {n} = {multiplicacion}\n")
    f.write(("\n"))
    return

tabla_multiplicar()
