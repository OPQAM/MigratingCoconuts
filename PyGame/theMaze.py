#!/usr/bin/env python3

import random

def outer_maze_creator(maze, maze_width, maze_length):

    # Adding empty spaces to the maze list:
    for row in range(maze_length):
        maze.append([])
        for col in range(maze_width):
            maze[row].append(" ")

    #filling the outside with walls
    for row in range(maze_length):
        for col in range(maze_width):
            if row == 0 or col == 0 or row == maze_length - 1 or col == maze_width - 1:
                maze[row][col] = "▓"

    # Temp: Let's see it
    for row in range(maze_length):
        for col in range(maze_width):
            print(maze[row][col], end="")
        # newline after each row
        print()

    return maze

'''This is for later:
║ ═ ╔ ╗ ╚ ╝╠ ╣ ╦ ╩ ╬ '''

def room_creator():
    max_room_width = 8
    min_room_width = 2
    max_room_length = 8
    min_room_length = 2

    room_width = random.randint(min_room_width, max_room_width)
    room_length = random.randint(min_room_length, max_room_length)

    return room_width, room_length

def add_rooms_to_maze(the_maze, number_of_rooms):

    return the_maze

def main():
    maze_width = 26
    maze_length = 26
    min_rooms = 4
    max_rooms = 10
    number_of_rooms = random.randint(min_rooms, max_rooms)
    the_maze = []

    outer_maze_creator(the_maze, maze_width, maze_length)
    add_rooms_to_maze(the_maze, number_of_rooms)
    
    return 0


if __name__ == "__main__":
    main()
