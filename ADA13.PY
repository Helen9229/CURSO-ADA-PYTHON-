######################################################################################################################
#programador :Garcia Helen                                                                                           #
#lenguaje: python                                                                                                    #
#version:3.10.4                                                                                                      #
#curso:Introduccion al desarrollo con python en ADAITW                                                               #
######################################################################################################################


#objetivo:Crear un programa que pida al usuario la distancia de su recorrido y
#  mostrar en un mensaje cuánto tiempo tardaría en completar el recorrido en distintos medios de transporte,
#  definiendo de antemano distintas velocidades para distintos medios de transporte 
# (p. ej.: a pie: 5 km/hora, bici 10km/hora, etc.).

recorrido =int(input("ingrese la distancia de su reccorrido en km: ")) 
pie = 5
bici= 10
auto =100 

tiempo_pie = 5 * 60 * recorrido 
tiempo_bici = 10 * 60 * recorrido
tiempo_auto = 100 * 60 * recorrido

print("si recorre {} km a pie son {}km en bici son {} y en auto son {} ".format( recorrido,tiempo_pie , tiempo_bici, tiempo_auto))