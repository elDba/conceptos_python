# creación listas
lista1 = list()
lista2 = []

# creación de listas con valores
lista4 = [1, 'a', 'casa', 3.14]

# creación de listas con rango
lista3 = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista3)
lista3a = [range(10)] # no se puede, porque range(10) es un objeto iterable, no una lista
print(lista3a)

# creación de listas con rango y paso
lista3b = list(range(0, 10, 2))  # [0, 2, 4, 6, 8]

# creación de listas con comprensión
lista6 = [x for x in range(10)]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# creación de listas con comprensión y condición
lista7 = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# creación de listas con comprensión y condición
lista8 = [x for x in range(10) if x % 2 == 0 and x > 5]  # [6, 8]

# creación de listas con comprensión y condición
lista9 = [x for x in range(10) if x % 2 == 0 and x > 5 and x < 8]  # [6]

# las listas pueden tener sublistas
lista5 = [1, 2, 3, ['a', 'b', 'c'], 'casa', 3.14]

