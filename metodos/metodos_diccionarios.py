dicc = {
    "nombre": "mauro",
    "apellido" : "de doná",
    "edad" : 33
}
# keys devuelve las claves y sirve para iterar
# ej: claves = dicc.keys() == nombre, apellido, edad

#get sirve para obtener el valor de una key si no encuentra nada NO tira error
#ej: claves = dicc.get("nombre") == mauro

# clear elimina todos los elementos del diccionario
# ej: dicc.clear() == elimina todo dicc= {}

#pop elimina un elemento
# ej: dicc.pop("nombre") == dicc{"apellido" : "de doná", "edad" : 33}

#items devuelve todo el diccionario como elementos iterables
# ej: dicc_iterable = dicc.items() == dict_items([('nombre', 'mauro'), ('apellido', 'de doná'), ('edad', 33)])

print(dicc)