#hace_calor(temperatura)

#Crear una función hace_calor que 
# tome como argumento un número temperatura y
#  devuelva True si hace calor (22 grados o más) o False de lo contrario

#hace_calor(12) # False
#hace_calor(22) # True
#hace_calor(32) # True

def hace_calor(temperatura):
    if temperatura >= 22 :
        print("true")
    else:
        print("false")    


hace_calor(12)
hace_calor(22)
hace_calor(32) 