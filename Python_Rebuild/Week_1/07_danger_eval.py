danger_entrypoint = eval(input("Please enter your dangercode here: "))

# Just as a case in point, when prompted, I ran:
# "__import__('os').system("sudo apt install sl")" which installed the app 'sl'

# Behind the curtain:
#
# ' 'eval()' evaluates the string that the user inputs as 'Python code'
# '__import__('os')' dynamically imports the built-in 'os' module,
# which in turn provides access to operating system functions.
# '.system(...) calls the shell to execute the respective command.
#
# Pretty nifty, actually

# TL;DR: 'eval' allows for remote execution. So don't do it, unless you reall know
# what you are doing.
