from f_retenciones import *

#OBTENER DATOS DE ENTRADA 
sueldo = float(input("sueldo: "))
situacion = input("Situacion (1/2/3): ")
num_hijos = int(input("numero de hijos:"))

#OBTENER EXENCION 

exencion = obtener_exencion(situacion, num_hijos)
sueldo_a_retener = sueldo - exencion
porcentaje = obtener_retencion(sueldo_a_retener)

#OBTENER RETENCION


monto_anual = sueldo_a_retener * porcentaje / 100
monto_mensual = monto_anual / 12

# MOSTRAR RESULTADOS
print("Sueldo anual: \t", sueldo)
print("situacion:\t", situacion)
print("Base a retener:", sueldo_a_retener)
print("Total anual:\t", monto_anual)
print()
print("Retencion mensual:", monto_mensual)

 