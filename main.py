from datetime import datetime


def consultar_nac():
    fecha_nac_str = input("Ingrese su fecha de nacimiento (dd/mm/yyyy): ")
    fecha_nac = datetime.strptime(fecha_nac_str, "%d/%m/%Y")
    return fecha_nac


def calcular_edad(nacimiento):
    presente = datetime.now()
    edad_usuario = presente.year - nacimiento.year - (
                (presente.month, presente.day) < (nacimiento.month, nacimiento.day))
    return edad_usuario


def segs_para_prox_cumple(fecha_nac):
    presente = datetime.now()
    prox_cumple = fecha_nac.replace(year=presente.year)

    if prox_cumple < presente:
        prox_cumple = prox_cumple.replace(year=presente.year + 1)

    tiempo_restante = prox_cumple - presente
    segundos_faltantes = tiempo_restante.total_seconds()
    return segundos_faltantes


fecha_nac = consultar_nac()
edad = calcular_edad(fecha_nac)
segundos_faltantes = segs_para_prox_cumple(fecha_nac)

print(f"Tu edad es {edad} años.")
print(f"Faltan {segundos_faltantes} segundos para tu próximo cumpleaños.")
