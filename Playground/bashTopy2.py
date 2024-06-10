#!/usr/bin/env python3

import subprocess

# We're now executing the 'fd' alias in an interactive bash shell
fd_command = subprocess.run(['bash', '-i', '-c', 'fd'], capture_output=True, text=True)

print(fd_command.stdout)
