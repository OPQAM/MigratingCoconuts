#!/usr/bin/python3

try:
    print(x)
except Exception as e:
    print(f"A Mess. Specifically: {e}")
y = "a"

try:
    int(y)
except Exception as b:
    print(f"And this was another mess. Specifically: {b}")

try:
    int(z)
except NameError:               # (1)
    print("Oops! ")

# NOTES: 
#
# (0) Note that if we force a SyntaxError, it won't be caught by try-except
#     The error will occur before the program fully loads, and the script
#     will break.
#  
# (1) Note that on a CLI we won't see any system information on the error.
#     On the IDE we'll see it.
#

