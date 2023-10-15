#!/usr/bin/env python3

import time             # for the timeouts
import subprocess       # for user input to be sent to the terminal

'''So, I'm starting my Python journey once again, this time with a purpose. The idea is to, once again, become somewhat proficient, so that I canstart learning some more advanced features (hopefully master OOP, to then apply said knowledge to my field of work Let us start by trying to create a menu, that the user can interact with'''


while True:

    time.sleep(0.5)

    print('''    *********************************************
    *** Welcome to our very own homely menu! ****
    ***** Please make your most wise choice. ****
    *********************************************
    ****** 1. Welcome!            ***************
    ****** 2. Do you like clams?  ***************
    ****** 3. Init 0              ***************
    ****** 4. Init 6              ***************
    ****** 5. Big Badabum         ***************
    ****** 0. Exit the program    ***************
    ******                        ***************
    *********************************************''')

    selection = input("\nSelection: ")

    if selection == '1':
        time.sleep(0.5)
        print("You are very welcome, indeed! What is your name, friend?\n")
        userName = input()
        print(f"We'll be good friends, {userName}!\n")
    
    elif selection == '2':      
        time.sleep(0.5)
        liking = input("Well, do you? ").strip().lower()
     
        if liking == 'yes' or liking == 'y':
            time.sleep(2)
            print("Well, bless your weary soul, you poor thing.")
            time.sleep(2)
            print("\n")
        elif liking == 'no' or liking == 'n' or liking == 'nope':
            print("Phew, that's a relief. Clams are disgusting.\n")
        else:
            print("You need to speak up. I didn't get that. But let's just assume you are mentally fit and answered 'no'. ;)\n")
            time.sleep(0.5)

    elif selection == '3':
        time.sleep(0.5)
        print('''Are you sure? Look... you might not be able to do this if you aren't root user.)   
                Should I give the go ahead? (y/n)\n''')                                             # this will still run for users in the sudoers group
        reply = input()
        if reply == 'y':
            time.sleep(0.5)
            print("Your call.")
            time.sleep(1)
            
            try:
                subprocess.run('init 0', shell=True)
            except Exception as e:
                print(f"that wasn't possible. Error: {e}")
        else:
            time.sleep(0.5)
            print("Phew! Ok. That's a relief. No-one should have that much power. Bye!")
            time.sleep(1)
            break
    
    elif selection == '4':
        time.sleep(0.5)
        print('''Init 6? Look... you might not be able to do this if you aren't root user.\n
                Should I give the go ahead? (y/n)\n''')
        reply = input()
        if reply == 'y':
            time.sleep(0.5)
            print("Your call.")
            time.sleep(1)

            try:
                subprocess.run('init 6', shell=True)
            except Exception as e:
                print(f"that wasn't possible. Error: {e}")

        else:
            print("I knew, you wouldn't let that type of power get to your head. Bye!")
            time.sleep(1)
            break

    elif selection == '5':
        print("\n")
        time.sleep(1)
        print("*******BOOM!!!!!*******")
        time.sleep(1)

    elif selection == '0':
        time.sleep(0.5)
        print("\nThanks for playing. See you soon.\n")
        time.sleep(1)
        break
