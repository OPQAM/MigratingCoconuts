#!/usr/bin/python3

import subprocess

# Command
ssh_command = (
        "bash -i -c 'a preprod 13 && sudo su -c \\\"curl -X POST https://100.127.201.126:4434/reset_context_model\\\"'"
        )

#Running
subprocess.run(ssh_command, shell=True)


# Preprod xavier 5
# Installation ID:
# IP: 

# 100.127.201.126 apex-preproduction-13 tagged-devices linux   -
# 434 (4434)

'''
# This version is making use of my local .bashrc functions (a,f,x,as)
# -i is for an interactive bash shell
# -c allows passing command to be executed by the shell

# I'm keeping this here for now, but it might be better to fork in git
command = "bash -i -c 'a zel 40'"

subprocess.run(command, shell=True)
'''
'''

# Command
command1 = "bash -i -c 'a preprod 13'"
command2 = "bash -i -c 'sudo su'"
command3 = "bash -i -c 'curl -X POST https://100.127.201.126:4434/reset_context_model'"

#Running
subprocess.run(command1, shell=True)
subprocess.run(command2, shell=True)
'''
#Manual
'''
root@Apex-PreProduction-13:/home/rcosta# wget --method=POST https://100.127.201.126:4434/reset_context_model
--2024-05-30 09:16:20--  https://100.127.201.126:4434/reset_context_model
Connecting to 100.127.201.126:4434... connected.
GnuTLS: An unexpected TLS packet was received.
Unable to establish SSL connection.
'''
