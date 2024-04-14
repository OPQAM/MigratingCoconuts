#!/usr/bin/python3

# Number palindrome checker.
# The original exercise only accepted integers, but that's too easy, and only requires a simple Try-Except.
# We'll allow all symbols

while True:
    test_value = input("Checking number: ")
    if len(test_value) > 0:
        break
    else:
        print("Please enter at least one character.\n")

listA = []
for item in test_value:
    listA.append(item)

result = True

count = len(test_value) - 1

for i in range(count):
    if listA[i] != listA[count]:
        result = False
    count -= 1

if result == True:
    print(f"{test_value} is a palindrome.\n")
else:
    print(f"{test_value} isn't a palindrome.\n")
