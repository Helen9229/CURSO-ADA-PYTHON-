######################################################################################################################
#programador :Garcia Helen                                                                                           #
#lenguaje: python                                                                                                    #
#version:3.10.4                                                                                                      #
#curso:Introduccion al desarrollo con python en ADAITW                                                               #
######################################################################################################################
#objetivo: Crear un programa que pida al usuario un número, luego otro
#  y mostrar en un mensaje si el primer valor es múltiplo del segundo.
#  INVESTIGAR EL OPERADOR MÓDULO O DE RESTO % PARA HACERLO

num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese otro numero: "))

def multiplo (num1, num2):
        return num1 % num2 == 0 
print(multiplo(num1,num2))       
