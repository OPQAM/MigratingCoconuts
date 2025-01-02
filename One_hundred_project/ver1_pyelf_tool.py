#!/usr/bin/env python


from elftools.elf.elffile import ELFFile

with open('simple_elf', 'rb') as f:
    elf = ELFFile(f)
    
    # Print ELF header information
    print("ELF Header:")
    print(elf.header)
    
    # Iterate through section headers
    print("\nSections:")
    for section in elf.iter_sections():
        print(f"Name: {section.name}, Type: {section['sh_type']}")
    
    # Iterate through program headers
    print("\nProgram Headers:")
    for segment in elf.iter_segments():
        print(f"Type: {segment['p_type']}, Size: {segment['p_memsz']} bytes")

