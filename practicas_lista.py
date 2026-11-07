notas= [10, 9, 8, 5]
print(notas)
notas.append(7)
notas.insert(1, 10)
print(notas)
print(notas[1])
print(len(notas))
print(notas[-1])
print(sum(notas))
print(max(notas))
print(min(notas))
print(notas.remove(9))
notas.sort()
print(notas)
print(notas[2:])
print(notas[:2])
print(notas[::-1])

#tuplas
meses_del_año = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
print(meses_del_año[0])
print(meses_del_año[-1])

#diccionario
estudiante ={
"cedula" : "0150287894",
"nombre" : "Alexander Juela",
"correo" : "ajuelsdm@.com",
"celular" : "0912345678",
"notas" : [10, 9, 8, 5]
}
print(estudiante.get("nombre"))
print(estudiante.keys())

#conjuntos
conjunto_a={ 1, 1, 5, 4, 6, 8}
conjunto_b = {1, 9, 6, 5, 4}
print (conjunto_a & conjunto_b)
print (conjunto_a | conjunto_b)