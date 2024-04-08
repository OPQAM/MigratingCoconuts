#!/usr/bin/python3


# Another catching up exercise. Mostly to reming myself of how functions work in py

def add_my_nums(x):
    counter = x
    final_value = 0
    while counter != 0:
        final_value += counter
        counter -= 1
    return final_value




while True:
    da_number = input("What number would you like to use?\n")
    try:
        da_number = int(da_number)
        if da_number >= 0:
            break
        else:
            print("Please enter a non-negative integer.")
    except ValueError:
        print("Error: Please enter a valid integer.")

result = add_my_nums(da_number)
print(f"\nThe sum of numbers up to {da_number} is {result}.")

