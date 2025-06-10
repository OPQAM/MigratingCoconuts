def extract_message(ppm_file, max_chars=1024):
    with open(ppm_file, 'rb') as f:
        # Read and skip header (3 lines)
        header = b""
        newline_count = 0
        while newline_count < 3:
            byte = f.read(1)
            if byte == b'':
                raise Exception("Unexpected end of file.")
            header += byte
            if byte == b'\x0A':
                newline_count += 1

        # Read pixel data
        pixel_data = f.read()
    
    bits = []
    for byte in pixel_data:
        bits.append(str(byte & 1))  # Extract LSB

    chars = []
    for i in range(0, len(bits), 8):
        byte_bits = bits[i:i+8]
        if len(byte_bits) < 8:
            break
        byte = int(''.join(byte_bits), 2)
        if byte == 0:  # Null terminator
            break
        chars.append(chr(byte))
        if len(chars) >= max_chars:
            break

    message = ''.join(chars)
    print(f"Extracted message: {message}")
    return message

specific_file = input("Hello, user. Please state the name of the image file: ")
extract_message(specific_file)

