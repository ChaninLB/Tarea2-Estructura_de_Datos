lista = [1, 2, 3, 4, 5]

# Con bucle
invertida = []
for i in range(len(lista) - 1, -1, -1):
    invertida.append(lista[i])
print(invertida)

# Con slicing (pythonic)
print(lista[::-1])

# Con reversed
print(list(reversed(lista)))