#!/usr/bin/env python3

import time             # for the timeouts
import subprocess       # for user input to be sent to the terminal

''' Just a classical, simple menu, for fun. Trying some stuff.
    Let's start by delaying the overall output, not just adding sleep time.
    Make it more human-readable and human-enjoyable. Sorry chatGPT, Pi, etc.'''

while True:

    time.sleep(0.1)

    intro= '''
    *********************************************
    *********************************************
    **    Welcome to our very own main menu    **
    **        Please make a wise choice        **
    *********************************************
    *********************************************
    **     1. Welcome!                         **
    **     2. Do you like clams?               **
    **     3. Init 0                           **
    **     4. Init 6                           **
    **     5. Big Badabum                      **
    **     0. Exit the program                 **
    *********************************************
    *********************************************
    '''

    # slow down main menu
    for char in intro:
        print(char, end='', flush=True)
        time.sleep(0.001)

    selection = input("\nSelection: ")

    if selection == '1':
        time.sleep(0.1)
        welcome = "You are very welcome, indeed! What is your name, friend?\n"

        for char in welcome:
            print(char, end='', flush=True)
            time.sleep(0.01)

        userName = input()
        time.sleep(0.1)
        greeting = "We'll be good friends," + userName + "!\n"
        for char in greeting:
            print(char, end='', flush=True)
            time.sleep(0.01)
    
    elif selection == '2':      
        time.sleep(0.1)

        confirmation = "Well, do you?"
        for char in confirmation:
            print(char, end='', flush=True)
            time.sleep(0.01)
        print()

        liking = input().strip().lower()
     
        if liking == 'yes' or liking == 'y':
            time.sleep(0.01)
            condolences = "Well, bless your weary soul, you poor thing."
            
            for char in condolences:
                print(char, end='', flush=True)
                time.sleep(0.01)

        elif liking == 'no' or liking == 'n' or liking == 'nope':
            relief = "Phew, that's a relief. Clams are disgusting."

            for char in relief:
                print(char, end='', flush=True)
                time.sleep(0.01)
            print()

        else:
            confusion = "You need to speak up. I didn't get that. Let's get back."
            
            for char in confusion:
                print(char, end='', flush=True)
                time.sleep(0.01)
            print()

    elif selection == '3':
        time.sleep(0.1)
        
        smasher = '''Are you sure? Look... you might not be able to do this if you aren't root user.
        Should I give the go ahead? (y/n)'''
        for char in smasher:
            print(char, end='', flush=True)
            time.sleep(0.01)
        print()
        
        reply = input()
        if reply == 'y':
            time.sleep(0.1)
            answer = "You're the boss, boss!"
            for char in answer:
                print(char, end='', flush=True)
                time.sleep(0.01)

            try:
                subprocess.run('init 0', shell=True)
            except Exception as e:
                errorMessage = "that wasn't possible. Error: " + e
                for char in errorMessage:
                    print(char, end='', flush=True)
        else:
            time.sleep(0.1)
            answer = "Phew! Ok. That's a relief. No-one should have that much power. Bye!"
            for char in answer:
                print(char, end='', flush=True)
                time.sleep(0.01)
            break
    
    elif selection == '4':
        time.sleep(0.1)

        smasher6 = '''Init 6? Look... you might not be able to do this if you aren't root user.
        Should I give the go ahead? (y/n)'''
        for char in smasher6:
            print(char, end='', flush=True)
            time.sleep(0.01)

        reply = input()
        if reply == 'y':
            time.sleep(0.1)
            answer = "Your call, boss."
            for char in answer:
                print(char, end='', flush=True)
                time.sleep(0.01)

            try:
                subprocess.run('init 6', shell=True)
            except Exception as e:
                errorMessate = "that wasn't possible. Error: " + e
                for char in errorMessage:
                    print(char, end='', flush=True)
                    time.sleep(0.01)
        else:
             time.sleep(0.1)
             answer = "Phew! Ok. That's a relief. No-one should have that much power. Bye!"
             for char in answer:
                 print(char, end='', flush=True)
                 time.sleep(0.01)
             break

    elif selection == '5':
        print("\n")
        time.sleep(0.1)
        badaBum = "*******BOOM!!!!!*******"
        for char in badaBum:
            print(char, end='', flush=True)
            time.sleep(0.01)
        print()


    elif selection == '0':
        time.sleep(0.1)
        goodbye = "Thanks for playing. See you soon."
        for char in goodbye:
            print(char, end='', flush=True)
            time.sleep(0.01)
        print()
        time.sleep(0.01)
        break
