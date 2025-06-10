# .ppm image file

file = "image.ppm"
binary_file = "binary.txt"

def get_message_and_check_capacity(max_character_count):
    message = input(f"\nEnter a message to embed (max {max_character_count} characters): ")
    if len(message) > max_character_count:
        raise ValueError("Message too long.")
    return message

def embed_message(pixels, message):
    bitstream = ''.join(f'{ord(c):08b}' for c in message)
    for i, bit in enumerate(bitstream):
        pixels[i] |= int(bit)
    print("Message successfully embedded.\n")


with open(file, 'rb') as f:
    header = b""
    newline_count = 0
    while newline_count < 3:
        byte = f.read(1)
        if byte == b'':
            raise Exception("Unexpected end of file.")
        header += byte
        if byte == b'\x0A':
            newline_count += 1
    
    header_str = header.decode("ascii")  # PPM headers are ASCII
    parts = header_str.strip().split('\n')
    magic_number = parts[0]         # P6, hopefully
    dimensions = parts[1]
    max_color = parts[2]
    

    width, height = map(int, dimensions.strip().split())
    
    print(f"Width: {width}\nHeight: {height}\n")

    pixel_data = f.read()
    pixels = bytearray(pixel_data)

    max_character_count = (width * height * 3) // 8

    print(f"Pixels saved and ready for editing.")
    print(f"Maximum number of character to be written: {max_character_count}")

    for i in range(len(pixels)):
        pixels[i] &= 0xFE  

    print("We can now write inside the pixels")


message = get_message_and_check_capacity(max_character_count)
embed_message(pixels, message)

output_file = "output.ppm"
with open(output_file, 'wb') as out:
    out.write(header)
    out.write(pixels)

print(f"Output writen to {output_file}")
