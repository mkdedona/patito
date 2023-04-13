#crear conjunto con set()
conjunto = set(["dato1", "dato2"])

#conjunto dentro de otro
conjun1 = frozenset(["dato1","dato2"])
conjun2 = {conjun1, "dato3"}
print(conjun2)

# Teoria de conjuntos
conj_1 = {1,3,5,7,9}
conj_2 = {1,3,7}

#verificando si es un subconjunto
resul = conj_2.issubset(conj_1)
resul_2 = conj_2 <= conj_1
veri_1 = resul == resul_2
print(veri_1)

#verificando si es un superconjunto
resul_3 = conj_2.issuperset(conj_1)
resul_4 = conj_2 > conj_1
veri_2 = resul_3 == resul_4
print(veri_2)

#verificar si hay algun nro igual con q haya uno solo da False
resul_5 = conj_1.isdisjoint(conj_2)
print(resul_5)