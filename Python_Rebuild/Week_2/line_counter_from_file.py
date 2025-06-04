'''
Objective:
Create a Python script that counts the number of lines in 
a text file provided by the user.

Instructions:
    Prompt the user to enter the path to a text file.
    Open the file in read mode.
    Read the file line by line and count the total number 
    of lines.
    Handle exceptions gracefully, such as when the file 
    does not exist or cannot be opened.
    Display the result to the user.

Sample Output:
Enter the path to the text file: example.txt
The file 'example.txt' has 42 lines.
'''

file_path = input("Please introduce the path to your file (ex: my_file.txt): ")

try:
    with open(file_path, 'r') as f:
        line_count = 0
        for line in f:
            line_count += 1
    print(f"Number of lines in file '{file_path}: {line_count}.")
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")




