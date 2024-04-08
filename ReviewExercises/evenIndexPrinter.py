#!/usr/bin/python3

print(f"The Amazing Even Index String Printer (tm)!\n")

the_string = input("Please enter your amazing string:\n")


# Let's use list comprehension. Long time no use.


first_list = [char for char in the_string]


for i, char in enumerate(first_list):
    if i % 2 == 0:
        print(char)


