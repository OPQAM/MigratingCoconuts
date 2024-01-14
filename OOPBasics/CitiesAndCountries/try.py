lista = []

x = 1
y = "a"
z = ("The rain in spain", 9)


lista.append(x)
lista.append(y)
lista.append(z)

for item in lista:
    print(item)
print(lista)
count = 0
for item in lista:
    if item == "a":
        print(f"Your item: {item} is positioned on index: {count}.")
    count += 1
exit(0)