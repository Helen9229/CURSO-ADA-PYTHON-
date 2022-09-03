#sumar_porcentaje(numero, porcentaje)

#Crear una función sumar_porcentaje que tome como argumentos
#  un número y un porcentaje y devuelva la suma de dicho número
#  con la de su porcentaje.
#  Usar la función calcular_porcentaje para obtener el porcentaje a sumar

#sumar_porcentaje(100, 15) # 115
#sumar_porcentaje(10, 50) # 15
#sumar_porcentaje(200, 10) # 220

def sumar_porcentaje(num,porcen):
    porcentaje =(porcen * num) / 100
    suma = num + porcentaje
    print("la suma del nummero con la del porcentaje es : {} ".format(suma))


sumar_porcentaje(100,15) 
sumar_porcentaje(10,50) 
sumar_porcentaje(200,10) 
