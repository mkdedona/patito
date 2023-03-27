# promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

# crudo duración
crudo_promedio = 5
crudo_dalto = 3.5

# diferencias de duración
diferencia_con_min = 100 - dalto_curso / otros_cursos_min*100
diferencia_con_max = 100 - dalto_curso*1000 // otros_cursos_max/10
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio*100

# diferencias de crudo
tiempo_vacio_promedio = 100 - otros_cursos_promedio *1000 // otros_cursos_max/10
tiempo_vacio_dalto = 100- dalto_curso * 1000 // crudo_dalto/10

#mostrando la duracion 
print("----------------------")

print(f'El curso dura un {diferencia_con_min} % menos que el más rapido')
print(f'El curso dura un {diferencia_con_max} % menos que el más lento')
print(f'El curso dura un {diferencia_con_promedio} % menos que el promedio')
print("----------------------")
# mostrando la cantidad de material eliminado
print(f'Un curso promedio elimana un {tiempo_vacio_promedio} % de tiempo vacio')
print(f'Este curso elimina un {tiempo_vacio_dalto} % de tiempo vacio' )
print("----------------------")

# mostrando diferencias si los cursos duran 10hs
print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_promedio*100// dalto_curso/10} horas de otros cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {dalto_curso*100// otros_cursos_promedio/10} horas de este curso')
print("----------------------")
