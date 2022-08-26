####################################################################################
#programadora: Helen Garcia                                                        #
#e-mail: garcia.helen14@yahoo.com.ar                                               #
#celular: 156379648                                                                #
####################################################################################
#fecha:04/08/2022
#lenguaje:python
#version:3.10.4
#curso: programacion python en ADAITW

#objetivo:Crear un programa que pida al usuario cuanto dinero disponible tiene,
#  y vaya preguntando cuánto tiene que pagar por cada servicio,
#  pidiendo el nombre del servicio y el monto a pagar, uno a la vez.
#  Cada vez que pide ingresar un nuevo servicio, el mensaje debe mostrar cuántos servicios quedan por ingresar,
#  utilizando una variable, y mostrar cuánto dinero disponible queda. 
# Al final debe mostrar una lista con todos los servicios a pagar y el monto de cada uno,
#  además del dinero disponible que le queda. Hacerlo con 3 servicios.


dinero_disponible = int(input("ingrese cuanto dinero tiene disponible : "))
servi1 =input("ingrese el nombre del servisio: ")
monto1 = int(input("ingrese el monto a pagar : "))
servisios_restantes = 2
saldo_restante = dinero_disponible - monto1 
print("te quedan servisios por pagar {} ". format(servisios_restantes))
print("quedan de saldo ${} disponible ". format(saldo_restante))

servi2 =input("ingrese el nombre del siguiente servisio: ")
monto2 = int(input("ingrese el monto a pagar : "))
servisios_restantes = 1
saldo_restante = dinero_disponible - monto1 - monto2
print("te quedan servisios por pagar {} ". format(servisios_restantes))
print("quedan de saldo ${} disponible ". format(saldo_restante))

servi3 =input("ingrese el nombre del siguiente servisio: ")
monto3 = int(input("ingrese el monto a pagar : "))
servisios_restantes = 0
saldo_restante = dinero_disponible - monto1 - monto2 - monto3
print("te quedan servisios por pagar {} ". format(servisios_restantes))
print("quedan de saldo ${} disponible ". format(saldo_restante))

print("el dinero total disponible fue de: $" ,dinero_disponible)
print("Pago por" ,servi1, "$" ,monto1)
print("pago por" ,servi2, "$" ,monto2)
print("pago por" ,servi3, "$" ,monto3)
print("El dinero que le queda en su cuenta es de : $" ,saldo_restante)