#!/usr/bin/python3

# The idea is to find a certain word within a sentence (number of times).
# This way I can check once again how to open files, read them, etc.

print("Welcome to the WordFinder. We'll open a text and fint the number of times a certain word appears.")

fileName = input("Please enter the (complete) file name: ")

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
print(f"Number of times {userVal} appears inside {fileName}: {counter}.\nBye!")
