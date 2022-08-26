######################################################################################################################
#programador :Garcia Helen                                                                                           #
#lenguaje: python                                                                                                    #
#version:3.10.4                                                                                                      #
#curso:Introduccion al desarrollo con python en ADAITW                                                               #
######################################################################################################################

#objetivo: Crear un programa que pida al usuario ingresar un número,
# y luego el porcentaje que se desea obtener del mismo. 
# Devolver un mensaje muestre el porcentaje de dicho número.

num = int(input("ingrese un numero: "))
porcentaje = int(input("ingrese el porcentaje que desea obtener del numero que ingreso: "))

porcen_num = (num * porcentaje) / 100

print ("el {} porciento del numero que ingreso es:  {}".format(porcentaje, porcen_num) )