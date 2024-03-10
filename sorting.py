#!/usr/bin/python3

size_of_list = int(input("What's the size of the list? "))
numberList = []
print("Let's have the list only containg integers, ok?\n")

for i in range(size_of_list):
    while True:
        try:
            number = int(input("Enter number: "))
            break
        except ValueError as e:
            print(f"{e} is not an integer!")
    
    numberList.append(number)

print("Added values:")
for num in numberList:
    print(num)
print(f"Our list:\n{numberList}")
