import os
from math import sqrt


def clear_terminal():
    os.system('clear')  # Clear the terminal screen (this is not working)


class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        if self.x is None or self.y is None:
            return "The point in question has been deleted!"
        else:
            return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))


class Line:

    def __init__(self, slope, y_intercept):
        self.slope = slope
        self.y_intercept = y_intercept

    def slope_as_str(self):
        return str(self.slope)

    def y_intercept_as_str(self):
        return str(self.y_intercept)

    def __str__(self):
        if self.slope is None or self.y_intercept is None:
            return "The line in question has been deleted!"
        else:
            if self.y_intercept < 0:
                return f"y = {self.slope}x {self.y_intercept}"
            elif self.y_intercept > 0:
                return f"y = {self.slope}x + {self.y_intercept}"
            elif self.y_intercept == 0:
                return f"y = {self.slope}x"
            else:
                return f"Error: {self.y_intercept} value is invalid."

    def __hash__(self):
        return hash((self.slope, self.y_intercept))



# The Main Factory Floor
class TheMachine:
    def __init__(self):
        self.points = []
        self.lines = []
        self.saved_points = set()  # Keep track of saved points
        self.saved_lines = set()

    # Point Creation
    def create_point(self):
        try:
            x = int(input("X-Value: "))
            y = int(input("Y-Value: "))
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")
            return

        point = Point(x, y)
        if point not in self.points and point not in self.saved_points:
            self.points.append(point)
            print("Point Created!\n")
        else:
            print("Point already exists in the list.")

    # Display Points
    def display_points(self):
        if not self.points:
            print("No points to display.")
        else:
            print("List of Points:")
            for i, point in enumerate(self.points, start=1):
                print(f"Point {i}: {point}")

    # Removing Points
    def remove_point(self):
        try:
            point_to_remove = int(input("Enter the Point number you want removed: "))
            if 1 <= point_to_remove <= len(self.points):
                self.points.pop(point_to_remove - 1)
                print("Point successfully removed!")
            else:
                print("Invalid Point number!")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Find the Distance Between Points
    def distance_between_points(self):
        try:
            entry_a = int(input("Please select your first Point: \n"))
            entry_b = int(input("Please select your second Point: \n"))
        except ValueError:
            print("Invalid input. Please enter a valid value.")
            return
        if 1 <= entry_a <= len(self.points) and 1 <= entry_b <= len(self.points):
            point_a = self.points[entry_a - 1]
            point_b = self.points[entry_b - 1]
            distance = round(sqrt((point_a.x - point_b.x) ** 2 + (point_a.y - point_b.y) ** 2), 2)
            print(f"Distance Between Points: {distance} units.")
        else:
            print("Invalid point numbers")

    # Saving Points to File
    def save_points_to_file(self, saved_points):
        try:
            with open(saved_points, 'w') as file:
                for point in self.points:
                    file.write(f"{point.x},{point.y}\n")
            print("Points saved successfully.")
        except Exception as e:
            print(f"Error saving points: {e}")

    #Loading Points from File
    def load_points_from_file(self, saved_points):
        self.points = []  # Clear existing points
        try:
            with open(saved_points, 'r') as file:
                for line in file:
                    x, y = map(int, line.strip().split(','))
                    point = Point(x, y)
                    if point not in self.points:
                        self.points.append(point)
        except FileNotFoundError:
            print("No points file found.")
        except Exception as e:
            print(f"Error loading points: {e}")

    # Line creator
    def create_line(self):
        try:
            entry_a = int(input("First Point: \n"))
            entry_b = int(input("Second Point: \n"))

            if entry_a == entry_b:
                print("Cannot create a line using the same point twice.")
                return

            if entry_a <= 0 or entry_b <= 0 or entry_a > len(self.points) or entry_b > len(self.points):
                print("Invalid point numbers.")
                return

            point_a = self.points[entry_a - 1]
            point_b = self.points[entry_b - 1]

            if point_a.x == point_b.x:
                print("Cannot create a line with vertical slope (division by zero).")
                return

            slope = (point_a.y - point_b.y) / (point_a.x - point_b.x)
            y_intercept = (point_a.y - slope * point_a.x)
            line = Line(slope, y_intercept)

            if any(line.slope_as_str() == l.slope_as_str() and line.y_intercept_as_str() == l.y_intercept_as_str() for l
                   in self.lines):
                print("Line already exists in the list.")
            else:
                self.lines.append(line)
                print("Line Created!\n")

        except ValueError:
            print("Invalid input. Please enter valid numeric values.")
        except ZeroDivisionError:
            print("Cannot create a line with vertical slope (division by zero).")

    # Display Line
    def display_lines(self):
        if not self.lines:
            print("No lines to display.")
        else:
            for i, line in enumerate(self.lines, start=1):
                print(f"Line: {i}: {line}")

    # Remove Line
    def remove_line(self):
        try:
            line_to_remove = int(input("Enter the Line number you want removed: "))
            if 1 <= line_to_remove <= len(self.lines):
                self.lines.pop(line_to_remove - 1)
                print("Line successfully removed!")
            else:
                print("Invalid Line number!")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    #Saving Lines to File
    def save_lines_to_file(self, saved_lines):
        try:
            with open(saved_lines, 'w') as file:
                for line in self.lines:
                    file.write(f"{line.slope},{line.y_intercept}\n")
            print("Lines saved successfully!")
        except Exception as e:
            print(f"Error saving points: {e}")

    # Loading Lines from File
    def load_lines_from_file(self, saved_lines):
        self.lines = []  # Clear existing lines
        try:
            with open(saved_lines, 'r') as file:
                for line in file:
                    slope_str, y_intercept_str = line.strip().split(',')
                    slope = float(slope_str)
                    y_intercept = float(y_intercept_str)
                    line = Line(slope, y_intercept)
                    if line not in self.lines:
                        self.lines.append(line)
            print("Lines loaded successfully.")
        except FileNotFoundError:
            print("No lines file found.")
        except Exception as e:
            print(f"Error loading lines: {e}")



# The Main User Screen
def main_menu(machine):
    clear_terminal()
    while True:
        print("\n**********************************")
        print("*** 1. Create Point **************")
        print("*** 2. Display Points ************")
        print("*** 3. Remove Point **************")
        print("*** 4. Distance Between Points ***")
        print("*** 5. Create Line ***************")
        print("*** 6. Display Lines *************")
        print("*** 7. Remove Line ***************")
        print("*** 8. Line Intercept (TBA)  *****")
        print("*** 0. Save and Exit *************")
        print("**********************************\n")

        choice = input("Pick a value, from 1 to 8 (0 to exit):\n")

        if choice == "1":
            machine.create_point()
        elif choice == "2":
            machine.display_points()
        elif choice == "3":
            machine.remove_point()
        elif choice == "4":
            machine.distance_between_points()
        elif choice == "5":
            machine.create_line()
        elif choice == "6":
            machine.display_lines()
        elif choice == "7":
            machine.remove_line()
        elif choice == "8":
            continue
        elif choice == "0":
            machine.save_points_to_file("points.txt")
            machine.save_lines_to_file("lines.txt")
            print("\nBye, bye!\n")
            break

# Automatically Running the Program
def main():
    machine = TheMachine()
    machine.load_points_from_file("points.txt")
    machine.load_lines_from_file("lines.txt")
    main_menu(machine)


if __name__ == "__main__":
    main()
