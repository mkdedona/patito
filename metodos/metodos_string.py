string_1 = "hOla Q tal"
string_2 = "asd"
string_3 = "asd 123"
string_4 = "pato, pato, pato, pato, gato, perro, perro"
# LA ESTRUCTURA DE LOS METODOS ES DATO.METODO(PARAMETRO DE CORRESPONDER)
# dir (funcion) devuelve la lista de atributos válidos del objeto, todo lo q se puede hacer.
# Ej: print(dir(string_1)) devuelve lo q se puede hacer con esa cadena

# upper convierte a mayuscula
# Ej: string_1.upper() == "HOLA Q TAL"

# lower convierte a minuscula
# Ej: string_1.lower() == "hola q tal"

# capitalize primera en mayuscula
# Ej: string_1.capitalize() == "Hola q tal"

# find busca el valor especificado y deveulve el indice, sino devuelve -1 
# Ej: string_1.find(h) == 0
# Ej: string_1.find(k) == -1

# index busca el valor especificado con la diferencia que devuelve error
# Ej: Ej: string_1.index(h) == 0
# Ej: string_1.index(k) == error

# isnumeric verifica si en la string el valor es unicamente numerico
# Ej: string_1.isnumeric() == falso

# isalpha verifica si en la string el valor es unicamente alfabetico 
# Ej: asd = string_2.isalpha() == True

# isnumeric isalpha en ambos casos devuelve False si hay caracteres especiales como espacio coma etc
# Ej: string_3.isalpha() == False

# count cuenta la catidad de veces q aparece el valor q buscas exactamente como lo pedis incluyendo todo tipo de caracter especial
# Ej: string_4.count("loro") == 0, string_4.count("pato") == 4, string_4.count("o") == 7

# len(funcion) cuenta los caracteres de una cadena 
# asd= len(string_2) == 3

# startswith verifica si la cadena empieza con el valor dado
# Ej: string_4.startswith("pato") == True

# endswith verifica si la cadena termina con el valor dado
# Ej: string_4.endswith("perro") == True

# replace si encuentra una coincidencia la reemplaza con el valor dado
# Ej: string_4.replace("perro" , "ñato") == pato, pato, pato, pato, gato, ñato, ñato

# split separa la cadena con la cadena q le pasemos y devuelve una lista
# Ej: string_4.split(",") == ['pato', ' pato', ' pato', ' pato', ' gato', ' perro', ' perro']