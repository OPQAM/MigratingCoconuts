#!/usr/bin/env python3

import random
import re # this to add some letters (see below)
num_digits = 3
max_guesses = 10

# TPC: created a version with letters as well as numbers

def main():
    print(f'''Bagels, a deductive logic game.
 By Al Sweigart al@inventwithpython.com
 
 I am thinking of a {num_digits}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
   Pico         One digit is correct but in the wrong position.
   Fermi        One digit is correct and in the right position.
   Bagels       No digit is correct.

Note that we're also allowing for the characters' a', 'b' and' c'.
 For example, if the secret number was b48 and your guess was c43, the
 clues would be Fermi Pico.''')
    
    while True:
        # Storing the secret number that we need to guess
        secretNum = getSecretNum()
        print("I have thought up a number.")
        print(f"You have {max_guesses} guesses to get it.")

        numGuesses = 1
        while numGuesses <= max_guesses:
            guess = ''
            # Looping until a valid guess is entered
            while len(guess) != num_digits or not re.match("^[a-c0-9]{3}$", guess): # abc allowed
            # Note that we're allowing for a, b and c. Nothing else on those 3 positions
                # or not guess.isdecimal(): REMOVED - to allow letters
                print(f"Guess #{numGuesses}")
                guess = input("> ")
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break # Leave loop. Guess is correct
            if numGuesses > max_guesses:
                print("You ran out of guesses.")
                print(f"The answer was {secretNum}")
        
        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing!")

def getSecretNum():
    numbers = list("0123456789abc")
    random.shuffle(numbers)

    # Getting the first num_digits in the list for the secret number
    secretNum = ''
    for i in range(num_digits):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    # Pico, Fermi, Bagels -> clues
    if guess == secretNum:
        return "You got it!"
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        # sorting clues into alphabetical order - not to give info away
        clues.sort()
        return ' '.join(clues)
    
# Ifa game is run (instead of imported) run the game
if __name__ == '__main__':
    main()
