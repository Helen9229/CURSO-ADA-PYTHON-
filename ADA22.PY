
###################################################################################################
#programadora: helen garcia                                                                       #
#email: garcia.helen14@yahoo.com.ar                                                               #
#cel:3816379648                                                                                   #
###################################################################################################

#objetivo: Crear un programa que tome la orden de compra de un local.
#  Pedir al usuario que ingrese la cantidad que desea comprar de tres productos distintos,
#  uno por uno,
#  mostrar el valor total de la compra y preguntar en cuántas cuotas desea realizar el pago.
#  Mostrar un mensaje final con el detalle y el valor total la compra,
#  cantidad de cuotas y valor de cada una de las cuotas. Los precios de los productos deben estar
#  definidos de antemano en variables.


nombre_1= input("ingrese el nombre del producto uno:")
producto1 = int(input("ingrese catidad del primer producto:"))
presio1 = int(input("ingrese el precio del primer producto:"))

nombre_2= input("ingrese el nombre del producto dos:")
producto2 = int(input("ingrese la cantidad del segundo producto:"))
presio2 =int(input("ingrese el precio del segundo producto:"))

nombre_3= input("ingrese el nombre del producto tres:")
producto3 = int(input("ingrese la cantidad del terecer producto:"))
presio3 =int(input("ingrese el precio del tercer producto"))

valor_total_de_compra = (producto1* presio1)+( producto2* presio2) + (producto3* presio3)
pregunta= input("en cuantas cuotas desesa realizar el pago: ")
cantidad_de_cuota = pregunta

mensaje = "El detalle de su compra es:{}, {} , {} , {} , {} , {}  , y el valor total de su compra es de $ {} ".format(producto1 ,nombre_1,producto2 ,nombre_2,producto3, nombre_3, valor_total_de_compra)
mensaje2 =" la catidad de cuotas es: {} y el valor de cada cuota es:{} ".format(cantidad_de_cuota)
print(mensaje)