def sumar(a, b):
    rtdo1 = a + b

    def dividir(c):
        rtdo2 = rtdo1 / c
        return rtdo2
    return dividir
mi_suma = sumar(2,3)
mi_div = mi_suma(2)
print(mi_div)