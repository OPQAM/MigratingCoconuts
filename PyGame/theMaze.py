#!/usr/bin/env python3

''' I'm starting afresh my maze game project
    The idea is to have a system that creates mazes
    and another one that lets the user traverse those locations
    Then I might want to add perhaps an AI generative element
    to the maze creation, game elements, etc.
'''
import random

# Rules for creation:
# - if diagonal has empty space, this must be filled (or we're in a room - rooms later)
# - rooms are created beforehand in separate function.
# - maze adds rooms (x for a n times m maze), then the corridors get added
# - If two big enough rooms in straight line we can have double corridors
# - rather have a dungeon than a maze (maze-ey dungeon)
# - if big enough map, small change entry point or exit point is double door
# - when rooms added, move on to create hallways
# - on rooms. How much room a romm does take? Conside this in calculations.

def create_maze(maze):
    width = random.randint(10,30)
    length = random.randint(10,30)
    print(f"Test: Length is {length}; width is {width}")

    # Initialize the maze with blocks
    for i in range(length):
        row = ["■"] * width
        maze.append(row)

    # DEBUG: see maze
    for row in maze:
        print("".join(row))

    return maze 

def create_room


# def player_movement():



def main():
    
    maze = []
    create_maze(maze)


if __name__ == "__main__":
    main()