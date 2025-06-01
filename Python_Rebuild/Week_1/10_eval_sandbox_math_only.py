'''
Only allow expressions made of:

    digits: 0-9

    operators: + - * / ( ) %

    optionally spaces

Block everything else before calling eval()
'''

allowed_chars = "0123456789+-/().&* "

while True:
    user_input = input("Enter a math expression: ")

    for char in user_input:
        if char not in allowed_chars:
            print("Invalid character detected!")
            break
    else:
        try:
            user_value = eval(user_input, {"__builtins__": None}, {})
        except:
            print("Dangerous expression detected!")
            continue
        else:
            print(f"Result: {user_value}")
            break

# Note that the 'else' is after the for loop and runs if the loop wasn't exited by break. Rather useful.
