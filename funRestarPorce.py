#Crear una función restar_porcentaje que
#  tome como argumentos un número y un porcentaje y devuelva
#  la resta de dicho número con la de su porcentaje.
#  Usar la función calcularPorcentaje para obtener el porcentaje a restar

#restar_porcentaje(100, 15) # 85
#restar_porcentaje(10, 40) # 6
#restar_porcentaje(200, 10) # 180

def restar_porcentaje(num,porcen):
    porcentaje =(porcen * num) / 100
    resta = num - porcentaje
    print("la resta del nummero con la del porcentaje es : {} ".format(resta))

restar_porcentaje(100,15)    
restar_porcentaje(10,40)  
restar_porcentaje(200,10)  