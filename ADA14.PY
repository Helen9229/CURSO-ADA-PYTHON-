#objetivo:Crear un programa que pida al usuario ingresar, por separado, 3 destinos de las escalas de un vuelo,
#  y la duración de cada uno de ellos. Al final debe mostrar un mensaje que liste todas las escalas con su duración y la duración total del vuelo.

destino1 = input("ingrese su primer destino:")
tiempo_vuelo1 =int(input("ingrese la duracio del primer destino: "))
destino2 = input("ingrese su segundo destino: ")
tiempo_vuelo2 =int(input(" ingrese la duracion del vuelo dos: "))
destino3 = input("ingrese su tercer destino: ")
tiempo_vuelo3 =int(input(" ingrese la duracion del vuelo tres: "))
duracion_total= tiempo_vuelo1 + tiempo_vuelo2+ tiempo_vuelo3
print("las escalas de duracion de cada vuelo son: {},{} dias ,{},{} dias ,{},{} dias y la duracion total de vuel es {} dias  ,".format(destino1,tiempo_vuelo1,destino2, tiempo_vuelo2,destino3, tiempo_vuelo3,duracion_total))