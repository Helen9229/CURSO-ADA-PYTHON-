#objetivo:Crear un programa que pida ingresar 
# una número de partida y una cantidad a ir incrementando y mostrar cinco mensajes seguidos que muestren el número del mensaje y 
# el total incrementado hasta el momento
# (p. ej.: empezando con 5 e incrementando 5, "Incremento 1) Total: 10", "Incremento 2) 
# Total: 15", "Incremento 3) Total: 20", etc.).

num = int(input("ingrese un numero de partida: "))
incremento= 5

contador = num + incremento

print(contador+1)