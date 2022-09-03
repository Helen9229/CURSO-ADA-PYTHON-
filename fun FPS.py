#FPS son cuadros por segundo (frames per second).
#  Crear una una función calcularFPS que tome como argumentos
#  una cantidad de cuadros por segundo y una cantidad de minutos, 
# y devuelva cuántos cuadros hubo en esa cantidad de minutos

#calcularFPS(1, 1) # 60
#calcularFPS(10, 2) # 1200
#calcularFPS(2, 3) # 360
def calcularFPS(cantidad_cuadros_seg,cantidad_minu):
    minutos = (cantidad_cuadros_seg * 60) * cantidad_minu
    print("{} cuadros hubo en {} minutos" .format(cantidad_cuadros_seg, minutos))


calcularFPS(1, 1)  
calcularFPS(10, 2)  
calcularFPS(2,3)  
