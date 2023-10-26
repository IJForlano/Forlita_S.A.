# Modulo que calcula tu edad en base a tu nac y cuando falta para tu prox cumple en segs.
from datetime import datetime


def consultar_nac():
    fecha_nac_str = input("ingrese su fecha de nacimiento.(dd/mm/yyyy)")
    fecha_nac = datetime.strptime(fecha_nac_str, "%d/%m/%Y")
    return fecha_nac


nacimiento = consultar_nac()


# func. que consulta edad y transforma ese str en un datetime

def calcular_edad(nacimiento):
    presente = datetime.now()
    edad_usuario = presente.year - nacimiento.year - ((presente.month, presente.day) < (nacimiento.month, nacimiento.day))
    return edad_usuario


edad = calcular_edad()
print(edad)

# func. que calcula edad.
segundos_faltantes = 0


def segs_para_prox_cumple(fecha_nac=None):
    global segundos_faltantes

    presente = datetime.now()
    if presente.month >= nacimiento.month:
        if presente.day >= nacimiento.day:
            diferencia = presente - nacimiento
            segundos_faltantes = diferencia.total_seconds()
            return segundos_faltantes
        elif presente.day <= nacimiento.day:
            diferencia = presente - nacimiento
            segundos_faltantes = diferencia.total_seconds()
            return segundos_faltantes


    elif presente.month <= nacimiento.month:
        diferencia = presente - nacimiento
        segundos_faltantes = diferencia.total_seconds()
        return segundos_faltantes
    else:
        print("Ingrese un input valido.")


segs_para_prox_cumple()
