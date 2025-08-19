tupla = (1, 2, 3, 4, 5)
print("\033[32mTupla:", tupla, "\033[0m")  # Imprime la tupla

#operaciones con tuplas
print(f"\033[32mLa longitud de la tupla", len(tupla, "\033[0m"))  # Imprime la longitud de la tupla
print(f"\033[32mEl primer elemento de la tupla es: {tupla[0]}\033[0m")  # Imprime el primer elemento de la tupla
print(f"\033[32mEl último elemento de la tupla es: {tupla[-1]}\033[0m")  # Imprime el último elemento de la tupla
#buscar un elemento en la tupla
print(f"\033[32m¿el numero 3 está en la tupla?", 3 in tupla,"\033[0m")  # Verifica si el número 3 está en la tupla
#otra forma usando el metodo index
print(f"\033[32mEl índice del número 4 en la tupla es: {tupla.index(4)}\033[0m")  # Imprime el índice del número 4 en la tupla