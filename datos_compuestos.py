# los datos compuestos son datos que adentro tienen otros datos
#----------------------------------------
#list es un conjunto de datos organizados con un indice el cual empiaza en cero.
#se crea con []
#y se accede a sus datos usando "nombre de la lista[nro de indice]" lo cual trabaja sobre el dato alojado en el [indice] indicado
lista = ["Mauro, De Doná", "31/5/1989", 1.85, 110]
print(lista[0]) #muestra solo el elemento indicado con []
print(lista) #muestra la lista entera
#pueden ser modificadas utilizando el indice por ej:

lista[1]= "31 de mayo de 1989" #modifico la fecha de nacimiento indicando su indice entre[]
print(lista)
#-----------------------------------------
#tuple o tupla es un conjunto de datos que no se puede modificar.
# Se crea con () y tambien posee [indice]

tupla = ("Mauro, De Doná", "31/5/1989", 1.85, 110)
#-----------------------------------------
#el set o conjunto es otro tipo de dato compuesto. se crea con {}
# No tienen orden, no repite los datos dupliados, no se pueden cambiar los elementos y no tiene indie a diferencia de las tuplas y las listas

conjunto = {"Mauro, De Doná", "31/5/1989", 1.85, 110}

#------------------------------------------

#el dict o diccionario es un conjunto similar a una lista solo q el indice lo creamos nostros
#Se crea con {} separando los elementos con coma ",":
#dict = {"key" : "dato"}
diccionario ={
    "nombre" : "Mauro, De Doná",
    "fecha_de_nacimiento" : "31/05/1989",
    "altura" : 1.85,
    "peso" : 110,
    "estudia_python" : True  
}

print(diccionario["fecha_de_nacimiento"])