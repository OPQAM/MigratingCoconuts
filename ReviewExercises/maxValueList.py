#!/usr/bin/python3


def findMax(listA):
    count = 0

    # Improvised method to set apart the first value as a 'maxVal' placeholder
    for element in listA:
        if isinstance(element, (int, float)):
            count += 1
            maxVal = element
            break

    # Checking if we have a valid list
    if count == 0:
        print(f"Error! Invalid List.")
        return None
    else:
        for element in listA:
            if isinstance(element, (int, float)):
                if element > maxVal:
                    maxVal = element
        return maxVal

# We're purposefully feeding the list with unwanted values (characters).
# We want the program to still be able to run
# listA = [1, 2, 0, "i", -12, 12, 9, "a", "-2", -2]
listA = ["a", "b", "c"]
print(f"Maximum Value of {listA}: {findMax(listA)}")
