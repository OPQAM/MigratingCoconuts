# Stenograph hidden image within ppm file
# PPM is being chosen for its simplicity
# We need to start writing after the third new line '0a'
# Before that we get the header with the information:
# P6
# Height + Width
# Range of pixel colors (usually 0-255)
# This is followed by trios of pixels that represent their RGB values.

# The goal is to take a message and write it in the least significant bit
# of those bytes.

# Example: the message 'Hi' has 2 characters, meaning 2 bytes, or 16 bits (01001000 01101001) These need to be distributed through the bytes.
# So we need 16/3 = 5 pixels (+ 1) to appropriately write our message, like so:
'''
"yyyyyyy0 yyyyyyy1 yyyyyyy0 yyyyyyy0 yyyyyyy1 yyyyyyy0 yyyyyyy0 yyyyyyy0 yyyyyyy0 yyyyyyy1 yyyyyyy1 yyyyyyy0 yyyyyyy1 yyyyyyy0 yyyyyyy0 yyyyyyy1"
'''



# .ppm file to be worked on
file = "image.ppm"


# print file as a single binary string
with open(file, 'rb') as f:
    data = f.read()
bits = ''.join(f'{byte:08b}' for byte in data)
print(bits)
