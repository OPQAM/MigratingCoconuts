#!/usr/bin/python3

# We're doing the same as with the previous version, but now with a function

def reversi(listA):
    sizeA = len(listA) - 1

    tempVal = listA[0]
    listA[0] = listA[sizeA]
    listA[sizeA] = tempVal

    return listA


listA = [1, "a", 0, "bingo"]
print(f"Old List: {listA}")

print(f"New List: {reversi(listA)}")
