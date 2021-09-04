#Si gasto hasta $100, pago con dinero en efectivo. Si no, si gasto más de $100 pero menos de $300, pago con tarjeta de débito. Si no, pago con
#tarjeta de crédito

#obtencion de datos
compra= int(input("coloque el dato de su compra"))
#en el primer if estamos comparando todos quellos datos
#que sean menores o iguales a 100
if compra <= 100: 
 print ("Pago en efectivo")
#elif significa que vamos a evaluar otra condicion
#and significa que vamos a evaluar 2 condiciones o 2 resultados
elif compra > 100 and compra < 300: 
 print ("Pago con tarjeta de débito")
#else significa un mensaje de error
else: 
 print ("Pago con tarjeta de crédito")