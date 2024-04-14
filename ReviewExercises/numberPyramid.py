#!/usr/bin/python3


# Started as a simple pyramid, then a complete pyramid, then Sudan
# Different versions in github, 12/04/2024:
# https://github.com/OPQAM/MigratingCoconuts/tree/master/ReviewExercises

while True:
    pyramidValue = input("Gimme a positive integer: ")
    try:
        pyramidValue = int(pyramidValue)
        if pyramidValue > 0:
            break
        else:
            print(f"'{pyramidValue}' isn't a positive integer.")
    except ValueError:
        print(f"'{pyramidValue}' isn't a valid number.")
while pyramidValue != 0:
    counter = 1
    for i in range(pyramidValue):
        print((str(counter) + ' ') * (i+1))
        counter += 1

    pyramidValue -= 1
    inverseCounter = pyramidValue
    if pyramidValue != 0:
        for i in range(pyramidValue):
            print((str(inverseCounter) + ' ') * (inverseCounter))
            inverseCounter -= 1
