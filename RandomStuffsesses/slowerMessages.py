#!/usr/bin/env python3


import time

message = "Let's see how slow we can get with our pythonic messages..."

for char in message:
    print(char, end='', flush=True)                  # (1) (2) (3)
    time.sleep(0.1)


print()                                              # to create a new line

'''Notes:

    (1) We're printing a character at a time, by using 'char'

    (2) We're making sure there are no empty spaces after each character

    (3) 'flush=True' makes sure that the character is immediately displayed.
        If set to 'False' the sentence will appear all at once in the end

'''
