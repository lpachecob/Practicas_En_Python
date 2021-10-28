def Piramide(lineas):
    """
        Dibuja Una Piramide vertical \n
        return: void()
    """
    filas = 0
    print("Piramide\n--------")
    for inea in range(lineas):
        filas += 1
        print(" " * (lineas - filas), end="")
        print("*" * filas, end="")
        print("*" * (filas-1), end=" ")
        print("")

Piramide(5)