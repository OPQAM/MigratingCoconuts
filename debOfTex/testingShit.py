#!/usr/bin/env python3


'''If statements'''

x = "Ricardo"
listx = ["apples", "oranges", "mumps"]


if x == "Helena":
    print("Helena in da House")
elif x == "Re":
    print(f"{x} is in the house.")
else:
    print(f"\nRico's here!")



'''for loops'''

for i in listx:
    print(f"\nGot me some {i}!")

'''while loops'''
j = 1
while j < 6:
    print(j)
    j += 1

'''Nested loops of Dicts and Lists'''

listA = [
    {'DictB1': 1}, 
    {'DictB2': 2}, 
    {'DictB3': 3}, 
    {'DictB4': 4},
    ]

DictA = {
    'ListB1': ['000', '001', '010'],
    'ListB2': ['011', '100', '101'],
    'ListB3': ['110', '111', 'boop!'],
}

for i in listA:
    print(i)

print(" ")

for key in DictA:
    for item in DictA[key]:
        print(item)
    print(" ")

'''snip'''