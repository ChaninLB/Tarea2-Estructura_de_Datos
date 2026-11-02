lista = [1, 3, 2, 3, 4, 3, 5]
v = 3

# Manual
count = 0
for x in lista:
    if x == v:
        count += 1
print(f"{v} aparece {count} veces")

# Pythonic
print(f"{v} aparece {lista.count(v)} veces")