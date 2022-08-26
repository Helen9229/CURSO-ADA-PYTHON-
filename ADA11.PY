######################################################################################################################
#programador :Garcia Helen                                                                                           #
#lenguaje: python                                                                                                    #
#version:3.10.4                                                                                                      #
#curso:Introduccion al desarrollo con python en ADAITW                                                               #
######################################################################################################################

#objetivo:Crear un programa que pida al usuario ingresar el valor de la altura y
#  el valor del ancho de un rectángulo, calcular su perímetro y mostrarlo en un mensaje.

altura = int(input("ingrese el valor para la altura del rectangulo: "))
ancho = int(input("ingrese el valor para el ancho del rectangulo: "))

perimetro = (2*altura) + (2*ancho)
print("el perimetro del rectangulo es : ", perimetro)