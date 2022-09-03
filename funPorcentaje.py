#Crear una función calcular_porcentaje que tome 
# como argumentos un número y un porcentaje y devuelva el valor del porcentaje
# correspondiente al número

#calcular_porcentaje(100, 15) # 15
#calcular_porcentaje(10, 50) # 5
#calcular_porcentaje(200, 10) # 20
def calcular_porcentaje(num,porcen):
    porcentaje =(porcen * num) / 100
    print("El {} % de {} es: {} ".format(porcen, num ,porcentaje) )

calcular_porcentaje(100,15)  
calcular_porcentaje(10,50)
calcular_porcentaje(200,10)
