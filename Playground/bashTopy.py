#!/usr/bin/env python3

import subprocess

# We can print this directly to stdout, without the subprocess library
print("Hello world!")


# In here, I can't use the actual 'fd' alias directly. Instead, I point to it's full path
fd_command = subprocess.run(['~/fd_script.sh'], capture_output=True, text=True, shell=True)

# We're using the shell=True because the ~ expansion is happening in the shell

print(fd_command.stdout)
