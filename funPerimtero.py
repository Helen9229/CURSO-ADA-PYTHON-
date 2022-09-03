#calcular_perimetro_rectangulo(ancho, alto)

#Crear una función calcular_perimetro_rectangulo que tome como argumentos el ancho y el alto de un rectángulo y devuelva su perímetro

#calcular_perimetro_rectangulo(3.2, 5) # 16.4
#calcular_perimetro_rectangulo(10, 20) # 60

def calcular_perimetro_rectangulo(ancho, alto):
    perimetro = 2 * ancho + 2 * alto
    print("el perimetro es: {} ".format(perimetro) )

calcular_perimetro_rectangulo(3.2,5)  
calcular_perimetro_rectangulo(10,20)    
