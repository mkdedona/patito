# Se usan para determinar las acciones a seguir si se da o no una condición




# if: si esto se cumple hace esto
# if True:
    # hace esto
    # hace esto
    # hace esto
#if False:
    # si no se cumple:
    # pasa a la siguente condicion
    
# elif: se cumple esta? condicion extra
#si no se cumple el if ver si se cumple esta otra

#     Si no se cumple:
#else: entonces hace esto
# ejemplos:

ingreso = float(input("ingresos mensuales: "))
gasto = float(input("gastos mensuales: "))

dolar = float(input("dolar hoy sin impuestos: "))
impuesto = dolar * 0.65
valor_dolar = dolar + impuesto


ingreso_mesual = ingreso / valor_dolar
gasto_mensual = gasto / valor_dolar
print("el valor del dolar con impuestos es: ", valor_dolar)
print("ingresos en dolares: ", ingreso_mesual)
print("gastos en dolares: ",gasto_mensual)

if ingreso_mesual >= 10000:
    if gasto_mensual <= 7000:
        print("estas bien economicamente en todo el mundo")
    else:
        print("estas gastando mucho")

elif ingreso_mesual > 1000:
    if gasto_mensual < 700:
        print("estas bien en latinoamerica")
    else:
        print("estas gastando mucho para latinoamerica")
elif ingreso_mesual <= 500:
    if gasto_mensual <= 350:
        print("estas bien en Argentina")
    else:
        print("estas gastando mucho para Argentina")

elif ingreso_mesual >= 200:
    if gasto_mensual < 140:
        print("estas bien en Venezuela")
    else:
        print("estas gastando mucho para venezuela")

else:
    print("sos pobre")

