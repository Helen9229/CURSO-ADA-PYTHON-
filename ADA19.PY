###################################################################################################
#programadora: helen garcia                                                                       #
#email: garcia.helen14@yahoo.com.ar                                                               #
#cel:3816379648                                                                                   #
###################################################################################################

#objetivo:Crear un programa que pida al usuario ingresar un texto
#y muestre un mensaje con la cantidad de caracteres que tiene ese texto. INVESTIGAR CÓMO HACERLO

#primero defino 
def contar_caracteres(cadena):
    contador = 0

    while cadena [contador:]:
        contador += 1
    return contador 

#defino una variable frase 

frase =input("ingrese una frase: ")

#ahora mostsrar por pantalla con el print , usaremos la funcion len que nos 
# devuelve un valor entero que indica la cantidad de caracteres en la cadena de entrada.

print("la cantidad de caracteres que tiene la frase es :" , len(frase))
