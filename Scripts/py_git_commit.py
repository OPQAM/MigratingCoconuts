#!/usr/bin/python3

import subprocess

print('''\n We're using a standardized version of the commit command (commit -m "message_here")\n''')

issue = {'f': 'Feature', 'd': 'Doc', 'b': 'Style', 't': 'Test'}

while True:
    choice = input(f"Is this related to a Feature(f), a Document(d), a Style or Beautification(b) change, or a Test(t)?")
    if choice in issue:
        user_choice = issue[choice]
        break
    else:
        print("Please make an appropriate choice.")

goal = input(f"What was the aim of this {user_choice} change?\n")
action = input(f"What has actually been done?\n")

standard_commit = 'git commit -m "{}: {}" -m "Objective: {}"'.format(user_choice, action, goal)

subprocess.run(standard_commit, shell=True)
