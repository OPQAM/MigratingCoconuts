#!/usr/bin/python3

# create a variable
x = 4

# create a list
listA = ["a", "b", 55, 34, 0]

listA.append(x)
listA.pop()
listA.append("3")


listaB = []



for i in range(5):
    user_input = input("Just enter a value, any value: ")
    listaB.append(user_input)               # This will always be a string. User input = strings

for i in range(5):
    print(listaB[i])
    print(type(listaB[i]))


theNewList = []

for item in listaB:
    try:
        as_int = int(item)
        theNewList.append(as_int)
    except ValueError:
        try:
            as_float = float(item)
            theNewList.append(as_float)
        except ValueError:
            theNewList.append(item)
print(theNewList)

for item in range(5):
    print(type(theNewList[item]))
