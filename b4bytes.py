#!/usr/bin/python3


#Doesn't work - print doesn't accept a 'b'
print(b"Hello World!")

#Works

raw_Hello = "Hello World"
for byte in raw_Hello:
    print(byte)

# We can use repr to convert back into characters (string representation)
print(repr(raw_Hello))
