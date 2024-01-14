#!/usr/bin/python3
def LongANDShort(listA):
    greaterVal = 0
    theHighIndex = 0
    lowerVal = 0
    theLowIndex = 0

    for i in range(len(listA)):
        tempCount = len(listA[i])
        if tempCount > greaterVal:
            greaterVal = tempCount
            theHighIndex = i
    
    for i in range(len(listA)):
        tempCount = len(listA[i])
        if tempCount < lowerVal:
            lowerVal = tempCount
            theLowIndex = i

    # Get tuple
    finalTuple = (listA[theHighIndex], listA[theLowIndex])
    print("test")
    print(f"{finalTuple}")

# Unresolved issues, ofc. There are problems with words with the same character count, etc

def main():
    listA = ["scrary", "mike", "barristan", "peter"]
    LongANDShort(listA)
main()
