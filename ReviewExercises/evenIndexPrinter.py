#!/usr/bin/python3

print(f"The Amazing Even Index String Printer (tm)!\n")

the_string = input("Please enter your amazing string:\n")

first_list = []

for element in the_string:
    first_list.append(element)

counter = len(the_string)

for i in range(counter):
    if i % 2 == 0:
        print(first_list[i])


