#!/usr/bin/env python3

import argparse
import sys

def extract_strings(file_path, min_length=4, offsets=False, filter_word=None):
    """Extract strings from a file with optional filters."""
    strings = []

    try:
        with open(file_path, 'rb') as f:
            data = f.read()

        temp_str = ""
        for idx, byte in enumerate(data):
            if 32 <= byte <= 126:  # printable ASCII
                temp_str += chr(byte)
            else:
                if len(temp_str) >= min_length:
                    if not filter_word or filter_word in temp_str:
                        if offsets:
                            strings.append((idx - len(temp_str) + 1, temp_str))
                        else:
                            strings.append(temp_str)
                temp_str = ""

        if temp_str and len(temp_str) >= min_length:  # catch final string
            if not filter_word or filter_word in temp_str:
                if offsets:
                    strings.append((len(data) - len(temp_str), temp_str))
                else:
                    strings.append(temp_str)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    for entry in strings:
        if offsets:
            print(f"{entry[0]:08x}: {entry[1]}")
        else:
            print(entry)

def main(args):
    """Entry point for the tool, compatible with lazy_suite.py."""
    parser = argparse.ArgumentParser(description="Extract strings from binary files.")
    parser.add_argument("file_path", help="Path to the file to analyze")
    parser.add_argument("--min-length", type=int, default=4, help="Minimum string length")
    parser.add_argument("--offsets", action="store_true", help="Show offsets of extracted strings")
    parser.add_argument("--filter-word", type=str, help="Filter strings containing this word")

    parsed_args = parser.parse_args(args)

    extract_strings(
        file_path=parsed_args.file_path,
        min_length=parsed_args.min_length,
        offsets=parsed_args.offsets,
        filter_word=parsed_args.filter_word
    )

