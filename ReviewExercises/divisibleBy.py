#!/usr/bin/python3


# Take a list and find all numbers divisible by 5.

while(True):
    size = input("Number of items in this list: ")
    try:
        size = int(size)
        if size > 0:
            break
        else:
            print(f"Please enter a positive integer. '{size}' isn't an acceptable value.")
    except ValueError:
        print(f"Please enter a valid integer. '{size}' isn't an acceptable value."
)

print(f"Let's populate this list with integers.\n")

myList = []

for i in range(size):
    while True:
        try:
            element = int(input(f"please enter element {i + 1}: "))
            myList.append(element)
            break
        except ValueError:
            print(f"Please enter a valid integer.")

print("\nThe list has been correctly populated:", myList)

divisibles = []
count = 0

for num in myList:
    if num % 5 == 0:
        divisibles.append(num)
        count+= 1

print(f"\nNumber of items divisible by zero: {count}")
print(f"The list of numbers divisible by 5:", divisibles)

