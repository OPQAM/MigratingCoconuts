#!/usr/bin/env python3

import subprocess

# We're now executing the 'fd' alias in an interactive bash shell
lazy_jump_command = subprocess.run(['bash', '-i', '-c', 'a famili 34'], capture_output=True, text=True)

print(fd_command.stdout)
