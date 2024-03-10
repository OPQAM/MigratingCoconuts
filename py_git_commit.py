#!/usr/bin/python3

# Re-adding this file on github. For some reason, it got deleted. Need to figure out why

import subprocess

print('Standardized commit message (substituting commit -m "message_here")\n')

issue = {'f': 'Feature', 'd': 'Doc', 'b': 'Style', 't': 'Test'}

while True:
    choice = input(f"Is this commit a new Feature(f), Documentation(d), Beautification or Style(b), or a Test(t)?")
    if choice in issue:
        user_choice = issue[choice]
        break
    else:
        print("Please make an appropriate choice.")

goal = input(f"What was the aim of this {user_choice} change?\n")
action = input(f"What has actually been done?\n")

standard_commit = '''git commit -m "'{}': {}" -m "Objective: '{}'"'''.format(user_choice, action, goal)

subprocess.run(standard_commit, shell=True)
