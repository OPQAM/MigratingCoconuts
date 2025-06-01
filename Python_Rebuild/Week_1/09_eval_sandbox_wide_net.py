'''
Exercise: Controlled eval sandbox (read-only math)

Write a script that:

    Asks the user for a math expression (e.g., 2 + 2, 5 * (9 - 1)).

    Uses eval() but restricts it to only allow math, nothing else.

    Blocks access to __import__, open, or anything dangerous.
'''

while True:
    try:
        user_value = eval(input("Enter math expression: "), {"__builtins__": None}, {})
    except:
        print("Dangerous expression detected!")
        continue
    else:
        print(f"Result: {user_value}")
    break


# {"__builtins__": None} removes access to all built-in functions like open, eval, exec, ..
# By adding {} as the local namespace, it provides no symbols (no variables or functions).

# Note that we still can have tuples or dicts, for example. We can add, for example 'a' + 'b' and get 'ab'
