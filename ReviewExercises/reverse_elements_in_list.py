#!/usr/bin/python3

listA = [1, "a", 0, "bingo"]

print(f"Old List: {listA}")

lengthA = len(listA) - 1

tempVal = listA[0]

listA[0] = listA[lengthA]
listA[lengthA] = tempVal

print(f"New List: {listA}")

