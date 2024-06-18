#!/usr/bin/env python3

import pdb


def factorial(n):
    pdb.set_trace()      # DEBUGGING: breakpoint 1
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    pdb.set_trace()      # DEBUGGING: breakpoint 2
    number = 5
    result = factorial(number)
    print(f"The factorial of {number} is {result}.")

if __name__ == "__main__":
    main()
