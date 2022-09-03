#hace_frio(temperatura)

#Crear una función hace_frio que tome como argumento
#  un número temperatura y devuelva True si hace frio (12 grados o menos) o False de lo contrario

#hace_frio(12) # True
#hace_frio(22) # False
#hace_frio(3) # True
#hace_frio(-2) # True

def hace_frio(temperatura):
    if temperatura <= 12 :
        print("true")
    else:
        print("false")    

hace_frio(12)
hace_frio(22)
hace_frio(3)
hace_frio(-2)   