#convertir_horas_en_segundos(horas)

#Crear una función convertir_horas_en_segundos que tome como argumento un número de horas y devuelva la conversión a segundos de dicha cantidad de horas

#convertir_horas_en_segundos(1) # 3600
#convertir_horas_en_segundos(3) # 10800
#convertir_horas_en_segundos(4.5) # 16200
def convertir_horas_en_segundos(cantidad_convertir):
    segundos= cantidad_convertir * 3600
    print("las horas que ingreso son {} segundos ".format( segundos) )

convertir_horas_en_segundos(1)    
convertir_horas_en_segundos(3)    
convertir_horas_en_segundos(4.5)    
