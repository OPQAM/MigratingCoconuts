#!/usr/bin/env python

import sys
import json
from elftools.elf.elffile import ELFFile
from elftools.elf.sections import SymbolTableSection

def parse_elf(file_path):
    result = {"file": file_path, "status": "ok", "symbols": []}

    try:
        with open(file_path, 'rb') as f:
            elffile = ELFFile(f)
            result["class"] = elffile.elfclass
            result["entry_point"] = hex(elffile.header.e_entry)
            
            if not elffile.has_dwarf_info():
                result["dwarf_info"] = "absent"

            for section in elffile.iter_sections():
                if isinstance(section, SymbolTableSection):
                    symbols = extract_symbols(section)
                    result["symbols"].extend(symbols)
                    break
            else:
                result["status"] = "error"
                result["error"] = "No symbol table found"
    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)

    print(json.dumps(result, indent=4))


def extract_symbols(section):
    symbols = []
    for symbol in section.iter_symbols():
        symbols.append({
            "name": symbol.name,
            "type": symbol["st_info"]["type"],
            "bind": symbol["st_info"]["bind"],
            "visibility": symbol["st_other"]["visibility"],
            "section_index": symbol["st_shndx"],
            "size": symbol["st_size"],
            "value": hex(symbol["st_value"])
        })
    return symbols


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python read_elf.py <path_to_elf_file>")
        sys.exit(1)
    
    parse_elf(sys.argv[1])

