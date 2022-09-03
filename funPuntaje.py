#calcular_puntaje(facil, normal, dificil)

#Crear una función calcular_puntaje que calcule el puntaje de un examen 
# que consiste en ejercicios de distinto nivel.
#  Debe tomar como argumento
#  tres que consisten en la cantidad de ejercicios resueltos en cada nivel 
# y devolver un número con el puntaje correspondiente.
#  El puntaje se calcula de la siguiente forma:

#facil: 3 puntos
#normal: 5 puntos
#dificil: 10 puntos

#calcular_puntaje(3, 0, 0) # 9
#calcular_puntaje(0, 2, 1) # 20
#calcular_puntaje(5, 1, 2) # 40

def calcular_puntaje(nivel1,nivel2,nivel3):
    facil = nivel1  * 3 + nivel2 * 5 + nivel3 * 10
    normal = nivel2 * 5
    dificil = nivel3 * 10
    print(facil, normal, dificil)

calcular_puntaje(3,0,0)   
calcular_puntaje(0,2,1)   
calcular_puntaje(5,1,2)   