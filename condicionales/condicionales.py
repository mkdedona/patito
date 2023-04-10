# Se usan para determinar las acciones a seguir
# si se da o no una condición y actua dependiendo de la condicion


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


ingreso_mesual =ingreso / valor_dolar
gasto_mensual =gasto / valor_dolar
#print("el valor del dolar con impuestos es: ", valor_dolar)
print("ingresos en dolares: ", ingreso_mesual)
print("gastos en dolares: ",gasto_mensual)

#mundo
if ingreso_mesual >= 10000:
    if ingreso_mesual - gasto_mensual >= 3000:
        print("estas bien economicamente en todo el mundo")
    elif ingreso_mesual - gasto_mensual <= 0:
        print("estas en deficit mun")
    else: print("estas gastando mucho para el mundo")
        
# Latinoamerica
elif ingreso_mesual >= 1000:
    if ingreso_mesual - gasto_mensual >= 300:
        print("estas bien en latinoamerica")
    elif ingreso_mesual - gasto_mensual <= 0:
        print("estas en deficit lat")
    else: print("estas gastando mucho para latinoamerica")
        
        # Argentina
elif ingreso_mesual >= 500:
    if ingreso_mesual - gasto_mensual >= 150:
        print("estas bien en Argentina")
    elif ingreso_mesual - gasto_mensual <= 0:
        print("estas en deficit arg")
    else: print("estas gastando mucho para Argentina")
              
# venezuela
elif ingreso_mesual >= 200:
    if ingreso_mesual - gasto_mensual >= 60:
        print("estas bien en Venezuela")
    elif ingreso_mesual - gasto_mensual <= 0:
        print("estas en deficit ven")
    else: print("estas gastando mucho para venezuela")
# pobre
else: print("sos pobre")