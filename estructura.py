import random
import numpy as np

# Creacion Listas
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Imprimir la lista
print(lista)

#Listas acceso
print(lista[0])  # Accede al primer elemento

# Lista vacia
lista_vacia = []
print(lista_vacia)  # Imprime la lista vacía

# Añadir elementos a la lista
lista_vacia.append(1)
print(lista_vacia)  # Imprime la lista con un elemento

# Agregar un elemento tipo texto
lista_vacia.append("Hola")

print(lista_vacia)  # Imprime la lista con un elemento de texto
# Agregar un booleano en medio de la lista
lista_vacia.insert(1, True)
print(lista_vacia)  # Imprime la lista con un booleano en medio

# Mostrar el ultimo elemento de la lista
print(f" El ultimo elemento de la lista es: {lista_vacia[-1]}") # Imprime el último elemento de la lista

# Imprimir la longitud de la lista
print(f"La longitud de la lista es: {len(lista_vacia)}")  # Imprime la longitud de la lista

# Eliminar un elemento de la lista
lista_vacia.remove(1)
print(lista_vacia)  # Imprime la lista después de eliminar el elemento

# Eliminar el último elemento de la lista
lista_vacia.pop()
print(lista_vacia)  # Imprime la lista después de eliminar el último elemento

# Modificar un elemento de la lista
lista_vacia[0] = "Modificado"
print("\033[36mLista modificada:", lista_vacia, "\033[0m") 

# Extensión de la lista
lista_vacia.extend([1, 2, 3])
print("\033[32mLista extendida:", lista_vacia, "\033[0m")  # Imprime la lista después de extenderla

# Listas de listas
lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\033[34mLista anidada:", lista_anidada, "\033[0m")  # Imprime la lista anidada

# Llenar listas con valores aleatorios
lista_aleatoria = [random.randint(1, 100) for _ in range(10)]
print("\033[35mLista aleatoria:", lista_aleatoria, "\033[0m")  # Imprime la lista con valores aleatorios

# Usar numpy para el random
lista_numpy = np.random.randint(1, 100, size=10).tolist()
print("\033[33mLista con numpy:", lista_numpy, "\033[0m")  # Imprime la lista generada con numpy

# Operaciones de las listas
lista_numpy.sort()
print("\033[31mLista ordenada con numpy:", lista_numpy, "\033[0m")  # Imprime la lista ordenada

# Invertir una lista
lista_numpy.reverse()
print("\033[32mLista invertida con numpy:", lista_numpy, "\033[0m")  # Imprime la lista invertida

# Buscar un elemento en la lista
print("\33[36mBuscar elemento 50 en lista aleatoria:", 50 in lista_aleatoria, "\033[0m")  # Verifica si 50 está en la lista aleatoria

# Buscar en la lista vacia
print("\033[35mBuscar elemento 1 en lista vacia:", 2 in lista_vacia, "\033[0m")  # Verifica si 1 está en la lista vacía

# Contar cuantas veces aparece un elemento en la lista
print("\033[34mContar elemento 1 en lista aleatoria:", lista_aleatoria.count(1), "\033[0m")  # Cuenta cuántas veces aparece el número 1 en la lista aleatoria

# Copiar una lista
lista_copia = lista_aleatoria.copy()
print("\033[33mLista copiada:", lista_copia, "\033[0m")  # Imprime la copia de la lista aleatoria

# Sumar dos listas
lista_suma = lista + lista_copia
print("\033[35mSuma de listas:", lista_suma, "\033[0m")  # Imprime la suma de las dos listas

lista_numpy.clear()
print("\033[31mLista numpy Limpiada:", lista_numpy, "\033[0m")

#concatenar dos listas
lista_concatenada = lista_copia + lista_vacia
print("\033[36mLista concatenada:", lista_concatenada, "\033[0m")  # Imprime la lista concatenada

#sacar mayor valor de una lista
print("\033[32mMayor valor de la lista copiada:", max(lista_copia), "\033[0m")  # Imprime el mayor valor de la lista copiada

#tamaño de la lista copiada
print("\033[34mTamaño de la lista copiada:", len(lista_copia), "\033[0m")  # Imprime el tamaño de la lista copiada

