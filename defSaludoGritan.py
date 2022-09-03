#saludar_gritando(nombre, apellido)

#Usando las funciones anteriores (obtener_nombre_completo, saludar y gritar), crear una función saludar_gritando que tome como argumentos 
# un nombre y un apellido y devuelva un saludo con signos de exclamación.

#saludar_gritando('Ada', 'Lovelace') # ¡Hola Ada Lovelace, un gusto conocerte!

#TIP: recordá que los resultados de funciones se pueden guardar en variables para usarlos más adelante

# nombreCompleto = obtener_nombre_completo('Ada', 'Lovelace')
#saludo = saludar(nombreCompleto)
#grito = gritar(saludo)
#print(grito) # ¡Hola Ada Lovelace, un gusto conocerte!

def saludar_gritando(nombre, apellido):
    print(" ¡ hola {},{}, un gusto en conocerte !".format(nombre,apellido))

saludar_gritando("helen","garcia" )    