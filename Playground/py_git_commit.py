#!/usr/bin/python3

import subprocess
selection = ""

while True:
    choice = input(f"Is this commit a new feature(f), a doc(d), beautification(b), or a test(t)?")
    if choice == "f":
        selection = "Feature"
        break
    elif choice == "d":
        selection = "Documentation"
        break
    elif choice == "b":
        selection = "Style"
        break
    elif choice == "t":
        selection = "Test"
        break
    else:
        print("Please make an appropriate choice.")

goal = input("What was the issue that you were trying to address?\n")
action = input(f"What have you accomplished with this particular {selection} commit?\n")

standard_commit = '''git commit -m "Type: '{}'" -m "Objective: '{}'" -m "Fixes: '{}'"'''.format(selection, goal, action)

subprocess.run(standard_commit, shell=True)

