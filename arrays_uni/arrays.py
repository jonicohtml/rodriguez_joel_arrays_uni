'''
Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido.

Escribir una función que permita ingresar la cantidad de números que reciba como parámetro.  Crear el array con la función del punto 1.

Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números. 

Escribir una función parecida a la anterior, pero la misma deberá calcular y devarolver el promedio de los números positivos.

5 - Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.

6 - Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.

7 - Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.

8 - Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:
Una lista de nombres (lista_nombres).
Un nombre a buscar en la lista (nombre_antiguo).
Un nombre de reemplazo (nombre_nuevo).
La función debe realizar las siguientes acciones:
Reemplazar todas las apariciones de nombre_antiguo en lista_nombres por nombre_nuevo.
Retornar la cantidad total de reemplazos realizados.

9 - Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la intersección de los dos arrays.

10 - Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la unión de los dos arrays.

11 - Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la diferencia de los dos arrays.
'''

'''
1 - Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido.
'''

lista = [256, 55, 256, 66, 256]

def crear_array(cantidad_elementos):
    for i in range(1, cantidad_elementos + 1):
        print(i)
        
'''
2 - Escribir una función que permita ingresar la cantidad de números que reciba como parámetro. Crear el array con la función del punto 1.'''

def ingresar_numero_array(cantidad_elemetos):
    
    for i in range(1, cantidad_elemetos + 1):
        ingreso_numeros = input("Ingrese un número: ")

'''
3 - Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números. '''


def promediar_numeros(lista: list) -> float:
    
    sumatoria = 0
    for i in lista:
        
        sumatoria += i
        
        promedio = sumatoria / len(lista)
        
    print(promedio)

'''
4 - Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.'''

def promediar_numeros_positivos(lista: list) -> float:
    
    sumatoria = 0
    promedio = 0
    cont = 0
    for i in range(len(lista)):
        if lista[i] > 0:
            cont += 1
            sumatoria += lista[i]
            promedio = sumatoria / cont
            
    print(f"{promedio:.2f}")
            
'''
Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.'''



def calcular_producto(lista: list) -> int:
    '''
    arg: lista -> recibe un elemento tipo lista
    return: int -> devuelve el producto, siendo este un número entero
    '''
    acumulador_producto = 1
    
    for i in range(len(lista)):
        acumulador_producto *= lista[i]
        
    return acumulador_producto

'''
6 - Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.
'''

def encontrar_valor_maximo(lista: list) -> int:
    maximo = 0
    posicion_maximo = 0
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
            posicion_maximo = i
    
    mensaje = f"El índice del valor máximo es: {posicion_maximo}"
    return mensaje

'''
7 - Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.
'''

'''
8 - Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:
a - Una lista de nombres (lista_nombres).
b - Un nombre a buscar en la lista (nombre_antiguo).
c - Un nombre de reemplazo (nombre_nuevo).

La función debe realizar las siguientes acciones:
Reemplazar todas las apariciones de nombre_antiguo en lista_nombres por nombre_nuevo.
Retornar la cantidad total de reemplazos realizados.
'''
nombres = ["jorge", "andres", "ruben", "andres", "jorge", "paula", "eliseo", "alejandra", "atilio", "juan", "andres"]

def reemplazar_nombres(lista_nombres: list, nombre_antiguo: str, nombre_nuevo: str) -> int:
    
    cantidad_reemplazos = 0
    
    for i in range(len(lista_nombres)):
        if nombre_antiguo == lista_nombres[i]:
            lista_nombres[i] = nombre_nuevo
            cantidad_reemplazos += 1
            
        print(lista_nombres[i])

    return f"La cantidad de reemplazos hechos es: {cantidad_reemplazos}"

print(reemplazar_nombres(nombres, "andres", "paparulo"))

'''
9 - Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la intersección de los dos arrays.
'''

lista_conjunto_m = ["a","b","c"]
lista_conjunto_n = ["g", "b", "l", "e"]

lista = 
def hallar_interseccion(lista_a: list, lista_b: list) -> None:
    
    
    for i in range(len(lista_conjunto_m)):
        for j in range(len(lista_conjunto_n)):
            if lista_conjunto_m[i] == lista_conjunto_n[j]:
                pass