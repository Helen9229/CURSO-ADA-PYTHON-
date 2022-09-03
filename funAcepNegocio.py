#acepta_deposito(monto)

#Crear una función acepta_deposito que tome como argumento un número monto y devuelva True
#  si el monto es divisible por 10 o False si no lo es

#acepta_deposito(440) # True
#acepta_deposito(123) # False
#acepta_deposito(500.50) # False
#acepta_deposito(1000) # True
def acepta_deposito(monto):
    if monto % 10 == 0:
        print("true")
    else:
        print("false")    

acepta_deposito(440)
acepta_deposito(123)
acepta_deposito(5000.50)
acepta_deposito(1000)
