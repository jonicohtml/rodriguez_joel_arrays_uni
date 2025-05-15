from mis_funciones import * 

nombres = ["agustina", "zoe", "hernan","marcele","lautaro", "marcela", "franco", "brenda"]
edades =[9,40, 30,20,10,22, 25, 15]
generos =["F", "F", "M", "X", "M", "X", "M", "F"]


print("Datos Desordenados")
mostrar_datos(nombres, edades, generos)

ordenar_ascendente(nombres, edades, generos)
print("\n\nDatos Ordenados ASC")
mostrar_datos(nombres, edades, generos)

ordenar_descendente(nombres, edades, generos)
print("\n\nDatos Ordenados DESC")
mostrar_datos(nombres, edades, generos)

ordenar(nombres, edades, generos, 2)
print("\n\nDatos Ordenados DESC/ASC")
mostrar_datos(nombres, edades, generos)

ordenar(nombres, edades, generos, 2, 1)
print("\n\nDatos Ordenados DESC/ASC")
mostrar_datos(nombres, edades, generos) 


""" lista = [1, 6, 8, 0, 3]

print(lista)

lista.sort(reverse=True)

print(lista) """