#generar_email(usuario, dominio)

#Crear una función generar_email que
#  tome como argumentos dos string usuario y dominio y
#  el un string email con el formato usuario@dominio.com

#generar_email('adalovelace', 'gmail') # 'adalovelace@gmail.com'
def generar_email(usuario, dominio):
    print("{}@{}.com ".format(usuario,dominio))

generar_email("adacurso","gmail")    