import os
class Player:
    def __init__(self, x, y, hp=5):
        self.x=x
        self.y=y
        self.hp = hp
    # position
    def __str__(self):
        return f"Current character position: ({self.x},{self.y})\nHealth: {self.hp}\n"

    # movement
    def move_north(self):
        self.y += 1
    def move_south(self):
        self.y -= 1
    def move_west(self):
        self.x -= 1
    def move_east(self):

        self.x += 1

def main():
    player1=Player(4,4)
    print("\n"
          "WELCOME TO THE DUNGEON!\n")

    print("You can escape the dungeon at any time by bashing your brains against the wall, or pressing '0'")
    print(player1)
    while True:
        if player1.hp == 0:
            print("You have died disgracefully from so much wall bonking!\nThe End.")
            break
        print(f"Move north (w)\n"
              f"Move south (s)\n"
              f"Move east (d)\n"
              f"Move west (a)")
        choice = input("What direction? ")

        if choice == "w":
            player1.move_north()
            if player1.y >= 9:
                player1.y -= 1
                print("\nBonk.\nOuch!")
                player1.hp -= 1
            elif player1.x == 4 and player1.y == 8:
                print(player1)
                exitchoice = input("There is a door hidden to the north. Would you like to open it? ")
                if exitchoice == 'y':
                    print("You go through the northern door, and escape your small cell.\nThe End.")
                    break
                else:
                    print("No? alright. Let's carry on.")
            print(player1)
        elif choice == "a":
            player1.move_west()
            if player1.x <= 0:
                player1.x += 1
                print("\nBonk.\nOuch!")
                player1.hp -=1
            elif player1.x == 4 and player1.y == 8:
                print(player1)
                exitchoice = input("There is a door hidden to the north. Would you like to open it? ")
                if exitchoice == 'y':
                    print("You go through the northern door, and escape your small cell.\nThe End.")
                    break
                else:
                    print("No? alright. Let's carry on.")
            print(player1)
        elif choice == "d":
            player1.move_east()
            if player1.x >= 9:
                player1.x -= 1
                print("\nBonk.\nOuch!")
                player1.hp -= 1
            elif player1.x == 4 and player1.y == 8:
                print(player1)
                exitchoice = input("There is a door hidden to the north. Would you like to open it? ")
                if exitchoice == 'y':
                    print("You go through the northern door, and escape your small cell.\nThe End.")
                    break
                else:
                    print("No? alright. Let's carry on.")
            print(player1)
        elif choice == "s":
            player1.move_south()
            if player1.y <= 0:
                player1.y += 1
                print("\nBonk.\nOuch!")
                player1.hp -= 1
            print(player1)
        elif choice == "0":
            print("Thanks for playing. Bái!")
            break
        else:
            print("Huh?! Speak up!\n")

main()
