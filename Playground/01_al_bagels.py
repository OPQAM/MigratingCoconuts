#!/usr/bin/env python3

import random
num_digits = 3
max_guesses = 10

def main():
    print(f'''Bagels, a deductive logic game.
 16. By Al Sweigart al@inventwithpython.com
 17. 
 18. I am thinking of a {num_digits}-digit number with no repeated digits.
 19. Try to guess what it is. Here are some clues:
 20. When I say:    That means:
 21.   Pico         One digit is correct but in the wrong position.
 22.   Fermi        One digit is correct and in the right position.
 23.   Bagels       No digit is correct.
 24. 
 25. For example, if the secret number was 248 and your guess was 843, the
 26. clues would be Fermi Pico.''')
    
    while True:
        # Storing the secret number that we need to guess
        secretNum = getSecretNum()
        print("I have thought up a number.")
        print(f"You have {max_guesses} guesses to get it.")

        numGuesses = 1
        while numGuesses <= max_guesses:
            guess = ''
            # Looping until a valid guess is entered
            while len(guess) != num_digits or not guess.isdecimal():
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
    numbers = list("0123456789")
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