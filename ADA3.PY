#OBJETIVO: Crear un programa que pida al usuario ingresar, por separado, nombre, apellido, edad, nacionalidad, documento, y 
# muestre luego un mensaje que diga: "Nuevo usuario agregado al sistema:" y liste todos los datos juntos.

Nombre = input("ingrese su nombre: ")
Apellido= input("ingrese su apellido: ")
Edad= input("ingrese su edad: ")
Nacionalidad= input("ingrese su nacionalidad: ")
Documento= input("ingrese su numero de documento: ")

mensaje= "Nuevo usuario agregado al sistema: " + " " + Nombre + " " + Apellido + " ," + Edad + " "+ " años " + " , "+ Nacionalidad + " , " +" DNI:" +  Documento
print(mensaje)