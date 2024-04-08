#!/usr/bin/python3


# Another catching up exercise. Mostly to reming myself of how functions work in py

def add_my_nums(x):
    try:
        counter = int(x)
    except ValueError:
        print("Error: Please enter a valid integer.")
        return None

    final_value = 0
    while counter != 0:
        final_value += counter
        counter -= 1
    return final_value





da_number = input("What number would you like to use?\n")
result = add_my_nums(da_number)
if result is not None:
    print(f"the sum of numbers up to {da_number} is:", result)

