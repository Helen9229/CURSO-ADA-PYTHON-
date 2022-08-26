#objetivo:Crear un programa que pida ingresar una cantidad de grados Celsius 
# y muestre un mensaje con el resultado de la conversión a grados Fahrenheit.
#formula : ºF = ºC x 1.8 + 32.
grados_celsius= int(input("ingrese una cantidad de grados celsius:"))
grados_fahrenheit = grados_celsius * 1.8 + 32

print("La conversion a grados fahrenheit es ", grados_fahrenheit,"F")