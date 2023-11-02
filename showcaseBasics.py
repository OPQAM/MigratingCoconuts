#!/usr/bin/env python3

# Rememberin certain Python Basics - long time no real use of the language

# Initializing different variables

age = 33                                              # integer
name = "Ricardo"                                        # string

listA = [2, "33", "Mike"]                             # list

dictA = {                                             # dictionaries
        "name": "Sarah",
        "age": 33,
        "city": "Marid"
}


counter = 1

while counter <= 5:                                   # while loops
	print(counter)
	counter += 1

for item in listA:                                    # for loops
	print(item)


if age % 2 == 0:                                      # if-else
	print("Age is even")
else:
	print("Age is odd")

def helloWorlder(name):                               # functions
	print(f"Hello, {name}")

helloWorlder("Ricardo")

# string manipulation

name2 = "Maria"

message = name + " and " + name2 + " are friends."

length = len(message)

print("Message length:", length)

# writing to a file

with open("example.txt", "w") as file:
	file.write("Hello, world!")

# reado from a file

with open("example.txt", "r") as file:
	content = file.read()
print(content)
