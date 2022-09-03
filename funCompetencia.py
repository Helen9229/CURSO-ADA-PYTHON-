#obtener_competencia(a, b)

#Crear una función obtener_competencia que tome como argumentos
#  dos strings a y b y devuelva un string con el formato a vs. b

#obtener_competencia('JavaScript', 'Python') # `JavaScript vs. Python`
#obtener_competencia('Coca', 'Pepsi') # `Coca vs. Pepsi`
#obtener_competencia('Perros', 'Gatos') # `Perros vs. Gatos`

def obtener_competencia(a, b):
    print("{} vs {} ".format(a,b))

obtener_competencia('JavaScript', 'Python')
obtener_competencia('coca', 'pepsi')
obtener_competencia('perros', 'gatos')


