#!/usr/bin/python3

# The idea is to find a certain word within a sentence (number of times).
# This way I can check once again how to open files, read them, etc.

print("\nWelcome to the WordFinder.\nWe'll open a text and find the number of times a certain word appears.")

fileName = input("\nPlease enter the (complete) file name: ")

readableFile = open(fileName, "r")
counter = 0

userVal = input(f"Word you're searching for inside {fileName}: ")
userVal = userVal.lower()

for line in readableFile:
    words = line.split()
    for i in range(len(words)):
        words[i] = words[i].lower()
    for word in words:
        if word == userVal:
            counter += 1

readableFile.close()
print(f"\nNumber of times '{userVal}' appears inside {fileName}: {counter}.\n\nBye!")
