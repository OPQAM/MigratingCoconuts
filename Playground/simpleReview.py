#!/usr/bin/python3

import sys

lista = []

counter = input("How many items do you want to append?\n")
try:
  numericalcounter = int(counter)
except:
  sys.exit("That's not a valid integer") # Using sys.exit here to actually stop the program

for i in range(numericalcounter):
  valuetolist = input("Tell me something you'd like to append to the list: ")
  lista.append(valuetolist)

print(lista)
