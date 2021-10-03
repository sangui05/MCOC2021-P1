
# -*- coding: utf-8 -*-

from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from constantes import *
from math import sqrt
from secciones import SeccionICHA

import sys


ret = Reticulado()


# nombre_archivo = "g06_4063_1540840_Grupo_06.h5"
#nombre_archivo = "g07_2725_1540552_05_ejemplo_chequear_diseño.h5"
# nombre_archivo = "Bonus_G8.h5"
# nombre_archivo = "g00_704_1544595_Puente Grupo 0 bonus-2.h5" #PESO_TOTAL = 50090.6566633671 kg
# nombre_archivo = "g05_2103_1544554_05_ejemplo_chequear_diseño.h5" #PESO_TOTAL = 667456.2596066704 kg
# nombre_archivo = "g07_2725_1544495_05_ejemplo_chequear_diseño-2.h5" #PESO_TOTAL = 416646.9566412371 kg
nombre_archivo = "g10_LATE_129_1544669_05_ejemplo_chequear_diseño.h5" #PESO_TOTAL = 101973.82745843157 kg



if len(sys.argv) > 1:
	nombre_archivo = sys.argv[1]


print(f"Abriendo: {nombre_archivo}" )

ret.abrir(nombre_archivo)



opciones_nodos = {
	"ver_cargas": True,
	"ver_numeros_de_nodos": False,
}

#Visualizar y comprobar las secciones
opciones_barras = {
	# "ver_secciones_en_barras": True,
	"color_barras_por_seccion": True,
	"ver_numeros_de_barras" : False,
}
ver_reticulado_3d(ret,opciones_nodos=opciones_nodos,opciones_barras=opciones_barras)




#Resolver el problema peso_propio
ret.ensamblar_sistema(factor_peso_propio=[0.,0.,-1.], factor_cargas=0.0)
ret.resolver_sistema()
f_D = ret.obtener_fuerzas()


#Resolver el problema carga viva
ret.ensamblar_sistema(factor_peso_propio=[0.,0.,0], factor_cargas=1.0)
ret.resolver_sistema()
f_L = ret.obtener_fuerzas()



#Calcular carga ultima (con factores de mayoracion)
FU_caso1 = 1.4*f_D
FU_caso2 = 1.2*f_D + 1.6*f_L




cumple_caso1 = ret.chequear_diseño(FU_caso1, ϕ=0.9)
cumple_caso2 = ret.chequear_diseño(FU_caso2, ϕ=0.9)



#Revisar que cumple el diseño 
if cumple_caso1:
	print(":)  El reticulado cumple todos los requisitos 1.4 D")
else:
	print(":(  El reticulado NO cumple todos los requisitos 1.4 D")

if cumple_caso2:
	print(":)  El reticulado cumple todos los requisitos 1.2 D + 1.6 L")
else:
	print(":(  El reticulado NO cumple todos los requisitos 1.2 D + 1.6 L")


PESO_TOTAL = ret.calcular_peso_total()

print(f"\nPESO_TOTAL = {PESO_TOTAL} kg\n")

CARGA_VIVA_TOTAL = -400*9.81*117.48*4 

print(f"CARGA_VIVA_TOTAL = {CARGA_VIVA_TOTAL} N ")

CARGA_VIVA_APLICADA = 0.
for  nodo in ret.cargas:
	for gdl, val in ret.cargas[nodo]:
		if gdl == 2:
			CARGA_VIVA_APLICADA += val


print(f"CARGA_VIVA_APLICADA = {CARGA_VIVA_APLICADA} N ")

if abs(CARGA_VIVA_APLICADA - CARGA_VIVA_TOTAL) > 1e-3:
	print(f"\n\n***** CARGA VIVA APLICADA NO CORRESPONDE ***")


if len(sys.argv) > 1:
	nombre_archivo = sys.argv[1]


print(f"Abriendo: {nombre_archivo}" )

ret.abrir(nombre_archivo)



opciones_nodos = {
	"ver_cargas": True,
	"ver_numeros_de_nodos": False,
}

#Visualizar y comprobar las secciones
opciones_barras = {
	# "ver_secciones_en_barras": True,
	"color_barras_por_seccion": True,
	"ver_numeros_de_barras" : False,
}
ver_reticulado_3d(ret,opciones_nodos=opciones_nodos,opciones_barras=opciones_barras)




#Resolver el problema peso_propio
ret.ensamblar_sistema(factor_peso_propio=[0.,0.,-1.], factor_cargas=0.0)
ret.resolver_sistema()
f_D = ret.obtener_fuerzas()


#Resolver el problema carga viva
ret.ensamblar_sistema(factor_peso_propio=[0.,0.,0], factor_cargas=1.0)
ret.resolver_sistema()
f_L = ret.obtener_fuerzas()



#Calcular carga ultima (con factores de mayoracion)
FU_caso1 = 1.4*f_D
FU_caso2 = 1.2*f_D + 1.6*f_L




cumple_caso1 = ret.chequear_diseño(FU_caso1, ϕ=0.9)
cumple_caso2 = ret.chequear_diseño(FU_caso2, ϕ=0.9)



#Revisar que cumple el diseño 
if cumple_caso1:
	print(":)  El reticulado cumple todos los requisitos 1.4 D")
else:
	print(":(  El reticulado NO cumple todos los requisitos 1.4 D")

if cumple_caso2:
	print(":)  El reticulado cumple todos los requisitos 1.2 D + 1.6 L")
else:
	print(":(  El reticulado NO cumple todos los requisitos 1.2 D + 1.6 L")


PESO_TOTAL = ret.calcular_peso_total()

print(f"\nPESO_TOTAL = {PESO_TOTAL} kg\n")

CARGA_VIVA_TOTAL = -400*9.81*117.48*4 

print(f"CARGA_VIVA_TOTAL = {CARGA_VIVA_TOTAL} N ")

CARGA_VIVA_APLICADA = 0.
for  nodo in ret.cargas:
	for gdl, val in ret.cargas[nodo]:
		if gdl == 2:
			CARGA_VIVA_APLICADA += val


print(f"CARGA_VIVA_APLICADA = {CARGA_VIVA_APLICADA} N ")

if abs(CARGA_VIVA_APLICADA - CARGA_VIVA_TOTAL) > 1e-3:
	print(f"\n\n***** CARGA VIVA APLICADA NO CORRESPONDE ***")


